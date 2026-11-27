# Mission 26: Move a complex beacon to baseband

The beacon is offset from your receiver center frequency. Translate it digitally.

**Track:** RF and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

I/Q samples are I+jQ: I is real, Q imaginary. Magnitude is hypot(I,Q); phase is atan2(Q,I), which preserves quadrants. Complex multiplication combines amplitude and phase. Multiplying by exp(-j*2π*f0*n/fs) shifts every complex frequency downward by f0. The sign matters.

An NCO generates digital sine/cosine values with a phase accumulator. A real cosine has both positive and negative frequency components; a complex rotating tone can distinguish their direction. This exercise uses double precision and bounded inputs, not a hardware NCO’s quantization model.

## Trace a small example

```text
(3+4j) has magnitude 5 and phase about 53.13 degrees.
+2000 Hz × exp(-j*2π*1500*n/fs) → +500 Hz
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement complex multiply, magnitude, phase (radians), and mix_down(x,f0,n,fs). Inputs are finite with fs>0 and moderate n. Use a portable pi constant; M_PI is not required by C17. Preserve amplitude under mixing.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 26
./learn check 26
./learn quiz 26
./learn explain 26
./learn submit 26
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 26` reveals one hint at a time. `./learn solution 26` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain I/Q, complex magnitude/phase, NCO and the sign of frequency translation. Contrast positive and negative complex tones.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
