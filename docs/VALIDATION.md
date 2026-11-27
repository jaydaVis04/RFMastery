# Validation record

Created and checked on November 26, 2026, on Apple Silicon macOS with Python 3.15.0 and Apple Clang 21.0.0.

## Executed successfully

- The C17 compiler built and ran both plain and AddressSanitizer/UBSan probes.
- All **29 executable C/Python reference missions** passed their behavioral tests. This includes 26 introductory/function C missions, two Python missions and the multi-file C capstone. C builds used `-Wall -Wextra -Wpedantic -Werror`, ASan and UBSan.
- All **29 corresponding unfinished starters** were rejected. Initial failure is expected and is not pre-earned progress.
- The C capstone was compared byte-for-byte against an independent Python formula for empty, impulse, zero, constant, extrema/alternating and 5,003 deterministic random I/Q samples. It also rejected malformed trailing lengths, bad arguments and file errors, and preserved identical-path input by rejecting before opening output.
- The C golden FIR used by mission 35 was compiled with sanitizers and compared against an independent Python integer formula on 512 deterministic samples, including negative rounding behavior.
- **31 course/tool regression tests** cover catalogue completeness, state roundtrips/corruption protection, quiz/flag gates, review scheduling, self-assessment, missing/broken HDL tools, Python-only setup defaults, setup error handling, capstone documentation, negative-frequency axes, binary generation, Rich color/plain output, literal text safety, narrow layouts, highlighted examples, and a real CLI journey in a disposable course copy.
- The CLI journey rejected the starter, accepted a reference implementation, completed quiz/explanation/submission, awarded a flag, suggested mission 2, and recognized a subsequent source change. Your actual learner files and flags were left unfinished.
- The signal sandbox was run for 850 Hz aliasing at 1 kS/s and a non-bin-centered complex spectrum with Hann window; CSV export and synthetic binary generation were exercised.
- The intentional sanitizer demo produced an out-of-bounds report and a use-after-free report in its respective modes. These expected failures illustrate diagnostics.
- Rich presentation was exercised using pip's bundled Rich 14.2.0 offline fallback. Wide (96-column) and narrow (52-column) previews were exported and visually inspected. `NO_COLOR`, plain output, forced color, and safe handling of literal markup were tested. The normal full Rich dependency is declared in requirements.txt; its package-server installation could not complete in this restricted session.

Reference validation runs in place against separate reference sources; it does not replace learner implementations or earn flags. Progress/state tests use temporary files, and the CLI journey uses a disposable course copy.

## Not executed here

**Five HDL missions (18, 19, 20, 21, 35) remain simulation-unverified in this environment because `iverilog` and `vvp` are not installed.** They contain reference RTL and self-checking testbenches, including deterministic backpressure scoreboards and a C golden-model comparison for the capstone. They are not reported as passes. Missing tools produce an explicit error in `./learn check`.

After installing Icarus, run:

```sh
./learn setup --fpga
python3 tools/validate_course.py --require-hdl
python3 tools/validate_course.py --starters --require-hdl
```

`--require-hdl` returns nonzero if the simulator is missing. This prevents a partial local validation from being mistaken for a verified HDL suite.

The default doctor verifies C readiness and reports FPGA availability without blocking C. `doctor --fpga` returns nonzero when the simulator is missing or its compile/run probe fails. Default setup installs Python packages only; `setup --fpga` additionally uses the correct Homebrew formula `icarus-verilog` and validates HDL references after tools work. A real Homebrew installation was attempted and denied writes to `/opt/homebrew` by this session; it was not treated as success and no system ownership changes were made. Run setup in a normal terminal to finish dependency installation.

The two writing missions (32, 36), explanations, transfer challenges and engineering report require self/human technical assessment. Length checks only establish that a substantive draft exists. Quiz correctness does not validate prose. No hardware synthesis, physical implementation, CDC analysis, timing closure, RF calibration, actual instrument communication or Battelle stack validation was performed.

## Reproduce

```sh
./learn doctor
python3 -m unittest discover -s tests -v
python3 tools/validate_course.py
python3 tools/validate_course.py --starters
```

Compiler diagnostics, first failing assertions and sanitizer reports are retained in command output on failure. Executables and simulation artifacts go to `.build/`. Benchmark results are generated from your own implementation with `./learn benchmark 34`; no reference benchmark is presented as your work or as hardware real-time performance.

Tests check a selected set of properties. Passing them is evidence for those properties, not proof of all behavior, race freedom, portable implementation on all systems, or engineering readiness.
