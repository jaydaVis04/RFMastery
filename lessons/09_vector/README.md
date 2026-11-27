# Mission 09: Grow telemetry without losing it

A dynamic event log must survive both growth and an allocator failure.

**Track:** C memory. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

`realloc(p,new_size)` may move an allocation. For nonzero sizes, failure returns NULL and leaves the old allocation valid. Store the result temporarily; update ownership and capacity only after success. On success stop using the old pointer and aliases, even if the address looks unchanged. Avoid zero-size realloc.

A vector maintains len<=cap, with data==NULL at cap=0. Doubling capacity improves amortized push cost, but doubling and byte multiplication can overflow. This lesson injects allocation failure through `lab_realloc` so recovery is actually tested.

## Trace a small example

```c
int *tmp = realloc(p, bytes);
if (tmp == NULL) { /* p still owned */ }
else { p=tmp; }
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `vec_push(v,x)` returning 0/-1, and `vec_destroy(v)`. Start capacity at 4, double only when full. Use lab_realloc instead of realloc and lab_free instead of free. Reject NULL v or impossible invariants; do not modify data/len/cap on failed growth. destroy is NULL-safe and resets all fields. Allocations are owned by the vector.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 9
./learn check 9
./learn quiz 9
./learn explain 9
./learn submit 9
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 9` reveals one hint at a time. `./learn solution 9` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain the vector invariant, temporary realloc pointer, failure recovery, and what happens to aliases after a successful resize.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)
