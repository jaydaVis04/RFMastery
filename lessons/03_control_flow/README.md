# Mission 03: Detect the threshold crossings

A noisy signal must be scanned without walking off the end of its sample buffer.

**Track:** C foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Integer division truncates toward zero: `7/2` is 3 and `-7/2` is -3. Unsigned arithmetic wraps; signed overflow is undefined. Small integer types undergo integer promotion. Mixed signed/unsigned expressions need care. `&&` and `||` short-circuit; `&` and `|` operate on bits. `switch` falls through without `break` or another transfer.

Use half-open ranges [0,n) for array loops. `for(size_t i=n-1; i>=0; --i)` fails: the comparison is always true and n-1 wraps for zero. Descend with i=n, i>0, and access i-1.

## Trace a small example

```c
for (size_t i = 0; i < n; ++i) {
    if (x[i] > threshold) ++hits;
}
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `count_above(x,n,threshold)` for strictly greater values. NULL is allowed only when n is zero; in that case return zero without dereferencing it. Equality does not count. Inputs may be negative.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 3
./learn check 3
./learn quiz 3
./learn explain 3
./learn submit 3
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 3` reveals one hint at a time. `./learn solution 3` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain unsigned countdown failure, signed overflow, and > versus >= with a concrete test case.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
