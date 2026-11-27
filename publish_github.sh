#!/usr/bin/env bash
# Run from your own terminal; this agent session cannot write .git or use network Git.
set -euo pipefail

course_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$course_root"
target_owner='jaydaVis04'
target_repo='learn_c'
target_full="${target_owner}/${target_repo}"
target_url="https://github.com/${target_full}"

if [[ "${1:-}" == '--dry-run' ]]; then
    printf 'Publish plan:\n'
    printf '  Source: %s\n  Repository: %s\n  Visibility: public\n' "$course_root" "$target_url"
    printf '  Include: course, lessons, tools, tests, docs and root project files.\n'
    printf '  Exclude: .build, .progress, scratch and Python caches via .gitignore.\n'
    printf '  Create an initial commit on main, then push without force.\n'
    printf '  Make the matching existing repository public if needed.\n'
    printf '  Existing repositories with content are never adopted automatically.\n'
    exit 0
fi
if [[ $# -ne 0 ]]; then
    printf 'Usage: %s [--dry-run]\n' "$0" >&2
    exit 1
fi

for command_name in git gh; do
    if ! command -v "$command_name" >/dev/null 2>&1; then
        printf 'Missing command: %s\n' "$command_name" >&2
        exit 1
    fi
done

if ! gh auth status --hostname github.com >/dev/null 2>&1; then
    printf 'GitHub sign-in is needed. Starting the official GitHub CLI sign-in.\n'
    gh auth login --hostname github.com
fi
authenticated_owner="$(gh api user --jq .login)"
if [[ "$authenticated_owner" != "$target_owner" ]]; then
    printf 'Expected GitHub account %s; active account is %s. Switch accounts with gh auth switch.\n' \
        "$target_owner" "$authenticated_owner" >&2
    exit 1
fi

if existing_root="$(git rev-parse --show-toplevel 2>/dev/null)"; then
    if [[ "$existing_root" != "$course_root" ]]; then
        printf 'This directory belongs to another Git repository: %s. Stopping before staging files.\n' "$existing_root" >&2
        exit 1
    fi
else
    git init -b main
fi

if [[ "$(git branch --show-current)" != 'main' ]]; then
    printf 'Expected branch main. Stopping without renaming your branch.\n' >&2
    exit 1
fi
if [[ -n "$(git ls-files -- .build .progress scratch)" ]]; then
    printf 'Generated files or private progress are already tracked. Review them before publishing.\n' >&2
    exit 1
fi

existing_origin="$(git remote get-url origin 2>/dev/null || true)"
if [[ -n "$existing_origin" ]]; then
    case "$existing_origin" in
        "${target_url}"|"${target_url}.git"|"git@github.com:${target_full}.git") ;;
        *) printf 'An unrelated origin is configured: %s. Stopping without changing it.\n' "$existing_origin" >&2; exit 1 ;;
    esac
fi

# Stage the reviewed course paths explicitly; .gitignore still excludes generated data.
git add -- .clang-format .gitignore Makefile README.md learn publish_github.sh course docs lessons tests tools
if ! git diff --cached --quiet; then
    git commit -m 'Add interactive C, FPGA and RF learning course'
fi

ensure_public() {
    local repository_visibility
    repository_visibility="$(gh repo view "$target_full" --json visibility --jq .visibility)"
    if [[ "$repository_visibility" != 'PUBLIC' ]]; then
        gh repo edit "$target_full" --visibility public --accept-visibility-change-consequences
    fi
}

if [[ -n "$existing_origin" ]]; then
    ensure_public
    git push -u origin main
elif existing_metadata="$(gh repo view "$target_full" --json isEmpty --jq .isEmpty 2>/dev/null)"; then
    if [[ "$existing_metadata" != 'true' ]]; then
        printf '%s already exists and is not empty. Stopping without uploading.\n' "$target_url" >&2
        exit 1
    fi
    ensure_public
    git remote add origin "${target_url}.git"
    git push -u origin main
else
    gh repo create "$target_full" --public --source . --remote origin --push \
        --description 'Interactive C, FPGA and RF internship preparation: 36 missions, tests, quizzes and capstones'
fi

gh repo view "$target_full" --json url,visibility --jq '"Published: " + .url + " (" + .visibility + ")"'
