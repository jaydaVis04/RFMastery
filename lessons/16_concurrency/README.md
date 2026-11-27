# Mission 16: Count completions across workers

Several worker threads report finished sample blocks; the completion counter must never lose an increment.

**Track:** C systems. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A data race on an ordinary object is undefined behavior. A C11 atomic operation makes that operation indivisible with defined ordering. Mutexes protect multi-operation invariants. `volatile` is neither substitute. This lesson uses atomic_fetch_add with relaxed ordering for an independent event count; it does not publish any sample-buffer data.

DMA moves data between devices and memory, but ownership, completion and cache coherency still need platform APIs. Model buffers as FREE → FILLING → READY → PROCESSING → FREE. If a producer outruns a consumer, choose backpressure or a documented drop policy. Mean throughput and worst-case block latency both matter.

## Trace a small example

```c
atomic_uint count = 0;
atomic_fetch_add_explicit(&count, 1u, memory_order_relaxed);
/* This does not publish or synchronize an unrelated sample buffer. */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement complete(counter) as one atomic increment and completed(counter) as an atomic load. Pointers are always valid; the test runs four pthread workers and stays below unsigned overflow. Do not cast away atomic types. Then draw the four DMA ownership states and identify which transition requires completion synchronization (include in your explanation).

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 16
./learn check 16
./learn quiz 16
./learn explain 16
./learn submit 16
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 16` reveals one hint at a time. `./learn solution 16` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain a data race, volatile versus atomic, and why an atomic event count alone is not a DMA/cache-coherency API. Describe the buffer ownership state transitions.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [Linux device access documentation](https://docs.kernel.org/driver-api/device-io.html)
