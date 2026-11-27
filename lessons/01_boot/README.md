# Mission 01: Bring the receiver console online

You have joined the fictional Signal Station lab. Its receiver console cannot boot until its first C program works. This story is independent of Battelle.

**Track:** C foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A C file is source text. Preprocessing expands includes and macros; compilation translates C; assembly produces object code; linking resolves names across objects and libraries. A declaration introduces a name and type. A definition supplies an object or function body. `main` returns an exit status; zero conventionally means success. Include `<stdio.h>` before using `printf`.

Build a habit now: read the first compiler error first. Fix it, rebuild, then read the next one. Warnings often expose mistakes before a program runs.

## Trace a small example

```c
#include <stdio.h>
int main(void) { printf("samples=%d\n", 16); return 0; }
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Create the console in `lab.c`: its `main(void)` must print exactly `SIGNAL STATION ONLINE` followed by a newline and return zero. Replace the placeholder, compile, and run it.

Then inspect the toolchain yourself (these exploration steps are not automatically graded):
```sh
cc -std=c17 -E lessons/01_boot/lab.c > /tmp/console.i
cc -std=c17 -S lessons/01_boot/lab.c -o /tmp/console.s
cc -std=c17 -c lessons/01_boot/lab.c -o /tmp/console.o
nm /tmp/console.o
```
Temporarily introduce an unknown variable, then a declared but undefined function you call. Compare the compiler and linker diagnostics, and undo your experiments.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 1
./learn check 1
./learn quiz 1
./learn explain 1
./learn submit 1
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 1` reveals one hint at a time. `./learn solution 1` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Describe source → preprocessor → compiler → assembler → linker. How does an unknown variable differ from an undefined external function?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
