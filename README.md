# Signal Station

An interactive C, FPGA and RF training course, built in this directory for your internship preparation. You are the new software engineer at a fictional receiver lab. Each mission restores another part of an offline radio system, from the first C executable to a tested streaming filter.

**Start here in your terminal:**

```sh
./learn doctor
./learn
```

If your terminal cannot execute `learn`, use `python3 learn` with the same arguments. You need Python 3.10+ and a C17 compiler. The C compiler and sanitizers work on this Mac. FPGA simulation needs Icarus Verilog: see [setup](docs/SETUP.md). Everything runs locally; there is no account, cloud service, paid dependency, radio or FPGA board requirement.

## Your first mission

```sh
./learn lesson 1
```

Open [lessons/01_boot/lab.c](lessons/01_boot/lab.c), implement the requested console, then:

```sh
./learn check 1
./learn quiz 1
./learn explain 1
./learn submit 1
```

The first check **should fail before you edit the starter**. You earn a `SIGNAL{...}` flag when your implementation passes, you answer the recall questions correctly, and you save a self-assessed explanation. `submit` actually reruns the tests. Flags are generated from the mission and your source; they are not strings your program should print. Later missions use real function contracts, allocator failure injection, boundary tests, randomized vectors and streaming scoreboards.

All lesson folders are available immediately. Follow the suggested order, or inspect a later topic when you need context. The final interview flag requires all earlier flags. If you edit a completed implementation, the map marks it CHANGED until you submit again. Local flags are motivation and progress records, not secure examination credentials.

## The practice loop

1. Read the short lesson and predict the small example’s behavior.
2. Build the requested component in that lesson’s source files.
3. Run `check`. Read the first failing assertion or sanitizer report, fix the cause, repeat.
4. Take the closed-notes quiz. Wrong answers get feedback and enter your review queue.
5. Explain your mechanism, an example, a failure case and a limitation aloud. Save your explanation.
6. Submit for a flag. Return on another day and try the transfer challenge without your solution open.

`./learn hint N` reveals hints gradually. `./learn solution N` displays a reference without replacing your files, and marks the mission as assisted practice. That is useful when you are stuck; later rebuild a variation from memory. Tests and references are inspectable by design. Do not change them just to make a flag appear.

The explanations and architecture drafts are **self-assessed**. The runner checks that a substantial draft exists, but cannot judge whether your prose is technically correct. Ask for a review of your reasoning and capstones when ready. A passing suite also does not prove all possible code behavior or timing closure.

## Course route

| Missions | What you build and learn |
|---|---|
| 01–04 | Console, types/declarations, control flow, separate C interfaces |
| 05–10 | Pointer algorithms, binary/text buffers, storage lifetimes, malloc/calloc/free, realloc vector, debugging |
| 11–17 | Portable packets, bits/CRC, simulated registers, seven-slot ring, I/Q records, atomics, Q15 FIR |
| 18–22 | Mux, clocked counter, FSM, valid/ready stage, FPGA/CPU buffer ownership |
| 23–30 | RF units, link budget, aliasing, complex mixing, DFT, decimation, QPSK/EVM, beamforming |
| 31–33 | SDR throughput/loss, RU/DU/CU and RavenStar context, mock instrument automation |
| 34 | Multi-file C receiver pipeline with binary I/Q, queue, filter, power and benchmark |
| 35 | Streaming Verilog FIR checked against compiled C and an independent Python formula |
| 36 | Mock interview, mixed recall test and engineering evidence |

Use `./learn map` for the complete lesson list. [The 12-week plan](docs/ROADMAP.md) maps your study time to the missions. [C primer](docs/C_PRIMER.md) starts from syntax, compiling and reading errors. [Glossary](docs/GLOSSARY.md) supports the RF/FPGA conversation. [Extra problems](docs/PROBLEM_BANK.md) go further once the main route is comfortable.

## Useful commands

| Command | Purpose |
|---|---|
| `./learn` | Interactive terminal menu, defaults to your next unfinished mission |
| `./learn lesson N` | Read a lesson and its contract |
| `./learn check N` | Compile and run its tests; C uses ASan and UBSan by default |
| `./learn quiz N` | Recall check with shuffled choices; final mission has 12 mixed questions |
| `./learn explain N` | Save your own explanation and explicit self-assessment |
| `./learn notes N` | Revisit a saved explanation |
| `./learn submit N` | Recheck work and award a flag once all gates pass |
| `./learn review` | Free-response review of due questions, then compare/self-rate |
| `./learn review --all --limit 5` | Practice previously encountered cards early |
| `./learn map` / `./learn status` | Inspect route/progress |
| `./learn interview` | Draw five oral interview prompts |
| `./learn benchmark 34` | Validate, then measure the plain optimized C capstone |
| `python3 tools/signal_lab.py` | Explore sampling, complex spectra and constellations |

If sanitizers are unavailable on another platform, `./learn check N --plain` is an explicit fallback, also supported by submit. A plain submission is recorded as unsanitized. `CC=clang ./learn check N` chooses a compiler. C uses strict warnings as errors. A program stuck in a loop times out with a diagnostic.

## Files and progress

- `lessons/NN_topic/README.md`: lesson, example, exact task, transfer prompt and resources.
- `lab.c` + `lab.h`, `lab.v`, or `lab.py`: your code. Two writing missions use `design.md`.
- `tests.c`, `tb.v`, `test_lab.py`: visible behavioral checks.
- `course/`: runner, catalogue, independent oracles and references (spoilers).
- `.progress/state.json`: your flags, notes, attempts, hints and review schedule. Back it up.
- `.build/`: generated executables, VCDs, vectors and benchmark artifacts; safe to regenerate.
- `tools/`: synthetic data, spectrum explorer and course validation.

No existing project was replaced: this directory was empty when the course was created. No Git repository is initialized automatically. When useful, initialize your own repository and commit your lesson implementations and notes; `.gitignore` excludes generated artifacts and private progress.

## Why the course works this way

The design uses retrieval practice, spaced review, worked examples and explaining your reasoning. [Learning-method research and its limits](docs/LEARNING_METHOD.md) links the primary studies/review and explains which choices are course-design judgments. Default intervals are practical choices, not a personalized scientific optimum.

This is independent preparation. Public RavenStar context helps connect the subjects; Battelle’s actual internal stack and internship posting were not supplied. Product-specific facts are limited to the [public description](https://www.battelle.org/markets/industry/communications/ravenstar). Confirm role priorities with the team.

## Verification

See [VALIDATION.md](docs/VALIDATION.md) for what was run here and what remains dependent on an HDL simulator. You can rerun the checks without changing learner code or earning flags:

```sh
python3 -m unittest discover -s tests -v
python3 tools/validate_course.py
python3 tools/validate_course.py --starters
python3 tools/validate_course.py --require-hdl
```

The last command intentionally fails if HDL simulation cannot be verified. Prose accuracy and physical FPGA timing are outside automatic validation.
