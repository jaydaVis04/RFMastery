# Mission 17: Filter samples in Q15

You need a deterministic integer reference before describing the filter in hardware.

**Track:** DSP in C. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Q15 interprets a signed 16-bit integer as value/32768, from -1 to 32767/32768. Multiplying Q15 values yields 30 fractional bits. Sum products in a sufficiently wide accumulator, rescale, then saturate to int16. Integer division in this course truncates toward zero, including negative sums. Document that rule so C, Python and HDL agree.

An FIR sums weighted delayed samples. This three-tap filter uses [8192,16384,8192]/32768 = [0.25,0.5,0.25]. Reset initializes both delay values to zero. There is one output for each input and no automatic tail flush.

## Trace a small example

```text
input:  32767, 0, 0, 0
output: 8191, 16383, 8191, 0  (truncation toward zero)
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement saturate_q15(acc) (acc is a sum of Q30 products; divide by 32768 then clamp), and fir_step(state,x) with state holding previous two samples. Valid state is always supplied and initially {0}. Test negative, impulse, constant and extrema. No signed right shift as a substitute for the specified division.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 17
./learn check 17
./learn quiz 17
./learn explain 17
./learn submit 17
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 17` reveals one hint at a time. `./learn solution 17` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain Q15 scale, accumulator width, saturation versus wraparound, truncation for negative values, and the impulse response.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
