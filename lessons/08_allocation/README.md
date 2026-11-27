# Mission 08: Allocate the capture window

The receiver needs a capture window of a requested length, with a precise allocation contract.

**Track:** C memory. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

`malloc(bytes)` returns uninitialized allocated storage or NULL. `calloc(n,size)` allocates and zeroes its bytes; all-bits-zero is not a universal floating-point or null-pointer representation guarantee. For integer types used here it gives zero. `free(NULL)` is harmless. Free only the allocation’s base pointer, once.

Before malloc(n*sizeof *p), reject multiplication overflow with n > SIZE_MAX/sizeof *p. Use sizeof *p to match the element type. A returned pointer must be checked before access. Define the zero-size contract explicitly instead of depending on allocator-specific behavior.

## Trace a small example

```c
int *p = calloc(8, sizeof *p);
if (p != NULL) { p[0]=12; free(p); }
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `samples_new(n,zeroed)` returning NULL for n=0 or byte-count overflow. If zeroed!=0 use calloc so every int is zero; otherwise use malloc (tests initialize before reading). Return NULL on allocation failure. Caller owns a successful result.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 8
./learn check 8
./learn quiz 8
./learn explain 8
./learn submit 8
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 8` reveals one hint at a time. `./learn solution 8` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Compare malloc, calloc and free. Explain overflow-before-allocation and why uninitialized reads are invalid.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)
