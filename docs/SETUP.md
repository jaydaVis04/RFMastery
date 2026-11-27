# Setup and troubleshooting

Run commands from the repository root. The course itself uses only Python’s standard library.

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
brew install iverilog
./learn doctor
python3 tools/validate_course.py --require-hdl
```

These are setup instructions for you to run; this course does not install packages automatically. `iverilog` compiles testbenches and `vvp` executes them. GTKWave is optional for viewing VCDs; self-checking testbenches remain the source of pass/fail results. Follow [Icarus’s official installation guide](https://steveicarus.github.io/iverilog/usage/installation.html) for other installation methods.

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
