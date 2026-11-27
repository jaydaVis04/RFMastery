# Signal Station terminal design specification

The learner is preparing for an RF/software internship, moving between reading, coding, tests and recall in a terminal. The display should feel like a calm radio workbench: a clear next target, visible verification state, and restrained instrument-like color.

## Direction and hierarchy

- Domain: receiver channels, accepted samples, signal acquisition, calibration, verification, and mission flags.
- Color world: cyan instrument traces, green ready lamps, amber cautions, red faults, violet capture markers, neutral terminal text.
- Signature: mission acquisition progress beside the next receiver component to restore.
- Keep the terminal's native font and background. Use weight, spacing and semantic color for hierarchy.
- Use one rounded frame for a mission/dashboard or a meaningful result. Avoid boxing every sentence.
- Keep paragraphs neutral; code, actions and feedback supply color. Status also has a readable label.
- Use one blank line between sections, one cell of vertical panel padding, and two horizontal cells.
- No animation or screen clearing; history remains scrollable. At narrow widths, stack controls and shorten tables.

## Semantic tokens

| Token | Rich style | Meaning |
|---|---|---|
| station | bold cyan | Product name, mission and section headings |
| action | bold cyan | Keys, prompts and next commands |
| ready | bold green | Passing verification, correct recall and ready tools |
| caution | yellow | Hints, missing tools, partial recall and changed work |
| fault | bold red | Failed checks and errors |
| capture | bold magenta | Earned flags and milestones |
| secondary | dim | Supporting metadata and frame lines |
| body | default | Reading text, source input and explanations |

## Component registry

All presentation lives in `course/terminal.py`, using Rich's Console, Panel, Table, Text, ProgressBar, Syntax and Markdown where available. The engine retains all grading/state logic.

| Component | Purpose |
|---|---|
| `print` / `ask` | Safe literal text, semantic feedback and prompts; never interpret learner text as markup |
| `dashboard` | Actual flags, review count, progress meter and next target |
| `course_map` | Mission state table with width-aware columns |
| `menu` | Grouped keyboard actions, stacked on small terminals |
| `markdown` | Lesson prose and highlighted worked code |
| `hint` | One progressive hint with amber emphasis |
| `flag` | Verified milestone panel |
| `syntax` | Readable reference source with line numbers |

## Behavior and accessibility

Use normal installed Rich first. A pip-bundled Rich fallback may provide panels/tables/syntax offline; a plain-text fallback keeps learning commands usable without presentation dependencies. The normal supported install is `requirements.txt` into project-local `.deps`, excluded from Git.

Color is automatic for terminals. `--color always` explicitly enables styled output; `--color never` and `NO_COLOR` select plain output. Redirected output is plain by default. No meaning relies on color alone, and neither display rendering nor setup changes learner sources, flags or notes. Tests must cover escape-free output, literal brackets, narrow layouts, and unchanged grading.
