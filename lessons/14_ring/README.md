# Mission 14: Buffer a burst of samples

A bursty producer must hand samples to a steady consumer without allocating in the hot path.

**Track:** Embedded C. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A ring buffer reuses fixed storage and wraps indices. This design stores a count to distinguish full and empty, with head=next write and tail=next read. A power-of-two capacity enables bitmask wrapping, but is not required: this mission deliberately uses capacity seven.

A fixed ring has predictable memory and usually good locality. Linked lists offer flexible insertion but add pointer chasing and allocation costs. This ring is single-threaded. Adding volatile does not make it safe across threads.

## Trace a small example

```text
capacity=3: push A,B,C → full; pop A; push D
logical order: B,C,D even though physical storage wrapped
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement ring_push/ring_pop returning 1 on success and 0 on full/empty/invalid pointers. A failed operation preserves the ring and output. Zero-initialized ring starts empty. Pop requires a non-NULL output. Do not allocate. Extension: implement and free a linked list, then compare allocation count and traversal locality (self-assessed).

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 14
./learn check 14
./learn quiz 14
./learn explain 14
./learn submit 14
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 14` reveals one hint at a time. `./learn solution 14` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain full/empty invariants, wrapping, FIFO ordering, and why a linked list may be worse for a sample stream.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
