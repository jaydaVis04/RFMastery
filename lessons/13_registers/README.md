# Mission 13: Bring a simulated device out of reset

The receiver status register sometimes never becomes ready. Your host must time out cleanly.

**Track:** Embedded C. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

`volatile` makes specified accesses observable to the compiler; it does not make them atomic, synchronize threads, or provide every device-ordering guarantee. Actual MMIO requires platform accessors, barriers and documented semantics. Never guess a hardware register’s address.

Write-one-to-clear means writing a 1 clears the corresponding status bit. A read-modify-write based on a stale register read can clear the wrong events. Polling needs a bound. These APIs simulate those effects in ordinary memory; they do not access physical hardware.

## Trace a small example

```c
/* Simulated W1C model, not a real register write: */
status &= ~written_ones;
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `clear_events(status,ones)` to clear only the low four event bits selected by ones; preserve all other bits. NULL is a no-op. Implement `wait_ready(polls)` using device_status() at most polls times. Return 0 as soon as bit 0 is set, otherwise -1. polls=0 must make no reads.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 13
./learn check 13
./learn quiz 13
./learn explain 13
./learn submit 13
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 13` reveals one hint at a time. `./learn solution 13` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Compare volatile and atomic. Explain W1C and why bounded polling matters even when hardware usually works.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Linux device access documentation](https://docs.kernel.org/driver-api/device-io.html)
- [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)
