# Mission 06: Read text without losing binary samples

The telemetry packet contains zero bytes; treating it as a string would lose data.

**Track:** C memory. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A C string ends at its first zero byte. Binary buffers use explicit lengths and may contain zero anywhere. A nonterminated character array is not a string. `strlen` needs a valid terminator; a bounded scan limits access. `memcpy` requires non-overlap; `memmove` handles overlap.

An output string needs room for its terminator. `snprintf` returns the number of characters that would have been written, excluding that terminator; a negative return means an encoding error, and a nonnegative result >= capacity means truncation. Cast to unsigned char for byte interpretation.

## Trace a small example

```c
unsigned char b[] = {0x41,0x00,0x42};
/* Binary length: 3 bytes. A string scan stops after A. */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `bounded_len(s,max)` (stop at NUL or max, NULL allowed at max=0) and `hex_encode(src,n,dst,cap)`. Hex output uses lowercase, two chars per byte and a final NUL. Return 0 on success, -1 on insufficient capacity or invalid pointers. On error preserve the destination. Reject size overflow; NULL src is allowed only at n=0; dst must always be non-NULL. Inputs and output do not overlap.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 6
./learn check 6
./learn quiz 6
./learn explain 6
./learn submit 6
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 6` reveals one hint at a time. `./learn solution 6` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain a string versus binary data, why embedded zeros matter, and the capacity contract for your hex encoder.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)
