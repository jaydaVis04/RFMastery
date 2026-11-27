# Mission 25: Identify the aliased beacon

Two continuous tones produce the same real samples. Identify what your receiver can actually distinguish.

**Track:** RF and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

For ideal reconstruction of a real baseband signal bandlimited to B, sample above 2B. Real converters need transition bands and anti-alias filters. Complex I/Q sampling can represent a total bandwidth approaching the sample rate under ideal assumptions; do not blindly apply the real-signal factor-of-two rule.

Real cosines at f and fs-f alias. Fold frequency modulo fs into [0,fs/2]. An ADC also quantizes amplitude; clipping occurs when the input exceeds its range and creates distortion. Filtering must happen before sampling or downsampling to prevent aliases that cannot later be separated.

## Trace a small example

```text
fs=1000 Hz, tone=850 Hz → modulo=850 → fold to 150 Hz
A real 850 Hz cosine and 150 Hz cosine have identical ideal samples.
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement alias_hz(f,fs) for real cosine frequency, allowing negative f. Return NAN for nonfinite input or fs<=0. Otherwise return the nonnegative folded frequency in [0,fs/2]. Use fmod and fabs. Explain why this folding loses the sign needed for complex tones.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 25
./learn check 25
./learn quiz 25
./learn explain 25
./learn submit 25
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 25` reveals one hint at a time. `./learn solution 25` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain Nyquist, anti-alias filtering, quantization and clipping. Why is real-cosine frequency folding different from a complex I/Q frequency axis?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
