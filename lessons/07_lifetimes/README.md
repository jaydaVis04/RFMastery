# Mission 07: Rescue the calibration lifetime

The calibration value must survive after its factory function returns.

**Track:** C memory. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

C defines automatic, static, thread, and allocated storage duration. A Linux process often has stack, heap, code, data, and mapped regions; those are implementation details rather than mandated C layouts. An automatic local’s lifetime ends when its block finishes. A static local persists across calls. Allocated storage lives until released.

A local pointer’s lifetime is independent of the object it points at. Returning &local is invalid because local dies; returning a pointer to an allocation may be valid with a documented owner. Setting one pointer to NULL after free does not repair aliases.

## Trace a small example

```c
static int boots; /* zero initialized, lasts for program */
/* int *bad(void) { int x=5; return &x; } is invalid. */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `calibration_new(value)` returning an independently owned int initialized to value, or NULL on allocation failure. Implement `calibration_destroy(int **owner)` to free once, clear *owner, and tolerate owner==NULL or *owner==NULL. Two calibrations must not share storage. The caller must not pass an alias that has already been freed elsewhere.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 7
./learn check 7
./learn quiz 7
./learn explain 7
./learn submit 7
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 7` reveals one hint at a time. `./learn solution 7` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Draw lifetimes for a local pointer, its allocated int, a static local and an automatic local. Identify exactly who frees your return value.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
