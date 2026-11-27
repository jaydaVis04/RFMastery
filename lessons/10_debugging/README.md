# Mission 10: Fix the corrupted capture

A capture copier loses ownership and overwrites its last byte. Find the mistakes before relying on its output.

**Track:** C debugging. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Undefined behavior can appear to work. Common memory failures are out-of-bounds access, use-after-free, double free, uninitialized reads, and leaks. AddressSanitizer detects many invalid accesses; UBSan detects selected undefined operations. Neither proves correctness. Leak checking support varies by platform; this course also tracks ownership in allocation exercises.

Debug systematically: reproduce, minimize, read the first report, inspect the allocation and failing access, fix the cause, rerun. Build with debug information. LLDB is normally the convenient debugger on macOS; GDB is common on Linux. Use a separate unsanitized build for Valgrind.

## Trace a small example

```sh
cc -std=c17 -g -O1 -fsanitize=address,undefined demo.c -o /tmp/demo
# lldb /tmp/demo  (breakpoint set --name main; run; next; frame variable)
# Linux: gdb /tmp/demo (break main; run; next; print x; bt)
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Repair `copy_capture(src,n)` so it returns an owned, NUL-terminated copy of exactly n bytes (including any embedded zeros), or NULL on invalid input/allocation failure/size overflow. NULL src is valid only when n=0. Use lab_alloc/lab_release (not malloc/free) so the checker can detect leaks. The starter safely returns NULL; the bad copy is in comments for diagnosis. Do not uncomment it until you can predict its bugs. A standalone sanitizer demo is provided in tools/memory_bug.c for controlled experimentation.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 10
./learn check 10
./learn quiz 10
./learn explain 10
./learn submit 10
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 10` reveals one hint at a time. `./learn solution 10` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Diagnose the three commented bugs. Describe one sanitizer limitation and the difference between a leak and use-after-free.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [Clang AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)
