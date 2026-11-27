# Setup and troubleshooting

Run commands from the repository root. Course logic uses Python's standard library; Rich supplies the terminal presentation.

## Automatic setup

```sh
./learn setup
```

This installs Rich from requirements.txt into `.deps` and verifies C. It does not install system packages or use sudo. Your Mac's C compiler is already working. It preserves lesson sources and progress. Python package installation needs access to the package server; use your normal terminal if the agent session cannot reach it.

The native Verilog simulator is only needed for the five FPGA missions. Add it when ready:

```sh
./learn setup --fpga
```

On macOS this uses Homebrew's `icarus-verilog` formula, then verifies the simulator and all five FPGA reference implementations. It needs permission to write Homebrew directories. Existing simulator tools are not reinstalled. Python packages provide the interface; C compilation and HDL simulation are external programs and cannot be replaced by installing Rich or other interface packages.

Rich can also render using the copy bundled with pip when a standalone installation is unavailable. That offline fallback provides panels, tables, progress and source highlighting; the normal Rich dependency provides complete Markdown/Pygments support. Plain output remains available with `--color never` or `NO_COLOR`.

To inspect tools without installing anything:

```sh
python3 --version
cc --version
./learn doctor
```

Python 3.10+ and a C17 compiler are required. This machine has Python 3.15 and Apple Clang 21; both plain and ASan/UBSan executables were successfully built and run. The prior conversation’s installation claims were not assumed: Icarus Verilog and Valgrind were absent when this directory was built.

## macOS

If missing, install Apple’s command-line tools from your terminal:

```sh
xcode-select --install
```

To enable the five HDL missions, install Icarus Verilog using your package manager, for example with Homebrew:

```sh
brew install icarus-verilog
./learn doctor --fpga
python3 tools/validate_course.py --require-hdl
```

`doctor` only inspects tools; the explicit `setup` command installs missing dependencies. The [Homebrew formula](https://formulae.brew.sh/formula/icarus-verilog) is named `icarus-verilog`; its executables are named `iverilog` and `vvp`. GTKWave is optional for viewing VCDs; self-checking testbenches remain the source of pass/fail results. Follow [Icarus’s official installation guide](https://steveicarus.github.io/iverilog/usage/installation.html) for other installation methods.

An installation attempted inside this restricted agent session was denied writes to `/opt/homebrew`, including its lock directory. The directory ownership already matched the local account. Homebrew's generic ownership advice was caused here by the session restrictions; the course does not run chown, chmod on system directories, or sudo to bypass them.

`doctor` runs the C probes and reports later FPGA tools separately. It returns nonzero for broken C setup. `doctor --fpga` additionally requires the Verilog compile/simulation probe to pass, returning nonzero for a missing or broken simulator. GTKWave and Valgrind are optional; neither is necessary to start learning. Full FPGA setup is verified only after the simulator and its reference tests execute successfully.

Use LLDB on macOS. Linux Valgrind instructions do not imply supported native operation on this Apple Silicon Mac.

## Linux

Install Python, GCC or Clang, and optionally Icarus using your distribution’s package manager. On Debian/Ubuntu an example is:

```sh
sudo apt install python3 build-essential iverilog gdb valgrind
```

Package availability and permissions depend on your machine. No hardware is needed. The FILE APIs are portable C; pthreads in lesson 16 are a POSIX addition. The course is tested on this Mac, not every distribution or Windows configuration. Windows users can use a Linux environment such as WSL.

## Compile one C exercise yourself

Mission 1 provides its own main. Most other C missions provide functions, while tests.c provides main:

```sh
cc -std=c17 -Wall -Wextra -Wpedantic -Werror -g -O1 \
  -fsanitize=address,undefined -fno-omit-frame-pointer \
  lessons/05_pointers/lab.c lessons/05_pointers/tests.c -lm -o /tmp/reverse_test
/tmp/reverse_test
```

The runner does this for you, including `-pthread` where needed. To inspect a debugger, make a separate plain build:

```sh
cc -std=c17 -g -O0 lessons/05_pointers/lab.c lessons/05_pointers/tests.c -lm -o /tmp/reverse_plain
lldb /tmp/reverse_plain
```

In LLDB: `breakpoint set --name reverse`, `run`, `frame variable`, `next`, `bt`. On Linux GDB: `break reverse`, `run`, `print n`, `next`, `bt`. A failed assertion can be expected until the learner implementation is complete.

## Read a sanitizer report

Use the controlled demo after mission 10:

```sh
cc -std=c17 -g -O1 -fsanitize=address,undefined tools/memory_bug.c -o /tmp/memory_bug
/tmp/memory_bug bounds
/tmp/memory_bug lifetime
```

Each mode intentionally fails. Read the first invalid access, allocation site and lifetime information, then repair a copy in your scratch directory. LeakSanitizer is not supported identically on every platform; Linux Valgrind on a separate plain build is an optional additional tool. The course’s allocator tests also count live allocations but do not prove every leak is impossible.

## Common problems

| Symptom | What to do |
|---|---|
| `./learn: permission denied` | Run `python3 learn`, or `chmod +x learn`. |
| Undefined reference to main | Compile with the mission’s test harness, except mission 1 and capstone CLI. |
| Undefined reference to math functions | Add `-lm` after source/object inputs on systems that require it. |
| Unused parameter warning treated as error | Use the parameter in your implementation; shipped stubs use `(void)x` temporarily. |
| First check fails | Expected until you implement the task. Read its README and first assertion. |
| Missing iverilog/vvp | Install Icarus; missing tools never award a passing HDL check. |
| C sanitizer unavailable | Try another GCC/Clang toolchain, or use `--plain` explicitly. |
| Timeout | Look for an unsigned countdown, infinite loop or testbench deadlock. |
| Corrupt progress file | Back up `.progress/state.json`; the runner refuses to overwrite unreadable JSON. |
| Flag becomes CHANGED | Your source changed. Recheck and resubmit to validate the new version. |

The course executes your local code. Its timeout is a debugging convenience, not a sandbox for untrusted downloaded programs. Keep the exercise inputs synthetic.
