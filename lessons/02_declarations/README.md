# Mission 02: Name the telemetry

The console needs types that describe sample counts and protocol fields accurately.

**Track:** C foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

`int`, `char`, `float`, `double`, `_Bool`, `size_t`, and fixed-width types solve different problems. Ordinary integer widths vary. A C byte has `CHAR_BIT` bits, which is not universally eight; this course’s packet format requires eight-bit bytes. `sizeof` returns `size_t`, measured in C bytes. `uint32_t` exists only when the implementation has an exact 32-bit unsigned type.

Read declarations from the name outward. `int *a[4]` is an array of pointers; `int (*a)[4]` is a pointer to an array. `const int *p` protects the pointed-to value through p; `int *const p` prevents changing p. Initialization creates the initial value; assignment updates it.

## Trace a small example

```c
int a = 3;
int *p = &a, q = 0; /* q is int */
size_t bytes = sizeof a;
/* printf("%zu\n", bytes); requires stdio.h */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `sample_bytes(n)` as the storage needed for n `uint16_t` objects. For this first exercise n is guaranteed small enough that multiplication fits `size_t`. Implement `apply(fn,x)` by calling the supplied function pointer. fn is guaranteed non-NULL. Read and annotate both declarations in lab.h.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 2
./learn check 2
./learn quiz 2
./learn explain 2
./learn submit 2
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 2` reveals one hint at a time. `./learn solution 2` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain int *a[4], int (*a)[4], const int *p, and int *const p. Why is sizeof measured in bytes rather than bits?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
