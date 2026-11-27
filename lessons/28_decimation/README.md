# Mission 28: Reduce the stream rate responsibly

The host cannot keep up with the incoming stream. Reduce the sample rate without pretending a weak filter is sufficient.

**Track:** RF and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

FIR filters use a finite weighted history; IIR filters include feedback and need stability analysis. Low-pass retains low frequencies, high-pass high frequencies, band-pass a band. Decimation reduces sample rate after an anti-alias filter. Interpolation inserts samples and filters images.

For 48 kS/s→12 kS/s, the new real Nyquist frequency is 6 kHz. Passband and transition must fit below it, with adequate stopband attenuation. This toy three-tap filter demonstrates ordering and state only; it does not meet a general-purpose anti-alias specification. A realistic design requires firwin or equivalent design and measured response.

## Trace a small example

```text
Filter x at every input index, then emit filtered indices 0,M,2M,...
Reset history is zero; no tail flush; output count = ceil(n/M).
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `decimate(x,n,M,out,cap)`: filter with [.25,.5,.25], zero history at start of each call, emit filtered indices divisible by M. Return count, or SIZE_MAX on M=0, NULL nonempty buffers, or insufficient capacity. NULL x/out is allowed when n=0. Reject before writing on error; buffers do not overlap. n and finite input values are moderate. This is block-local, not a continuous multi-call streaming filter.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 28
./learn check 28
./learn quiz 28
./learn explain 28
./learn submit 28
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 28` reveals one hint at a time. `./learn solution 28` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain anti-aliasing before decimation, passband/transition/stopband, interpolation images, and the toy filter’s limits.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
- [SciPy filter design](https://docs.scipy.org/doc/scipy/reference/signal.html)
