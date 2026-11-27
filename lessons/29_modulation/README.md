# Mission 29: Map bits onto a constellation

The receiver’s constellation display shows symbols rather than individual bits.

**Track:** RF vocabulary and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

BPSK uses two phases; QPSK uses four points; QAM uses amplitude and phase. A symbol may encode several bits: QPSK carries two, 16-QAM four before coding and overhead. Symbol rate, bit rate, and sample rate are different. Samples per symbol depends on the waveform and pulse shaping.

EVM measures deviation from ideal constellation symbols using an explicitly defined reference/normalization. BER is erroneous bits divided by compared bits. OFDM uses many orthogonal subcarriers through IFFT/FFT and often a cyclic prefix to manage multipath under its design assumptions. It does not eliminate all interference or synchronization work.

## Trace a small example

```text
00 → (+1+j)/sqrt(2); 01 → (+1-j)/sqrt(2)
10 → (-1+j)/sqrt(2); 11 → (-1-j)/sqrt(2)
1 Msymbol/s QPSK → 2 Mbit/s before overhead
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement qpsk(b0,b1) using exactly this mapping and `bit_errors(a,b,n)` counting unequal bits, not unequal bytes. Bits are always 0 or 1, pointers valid for n>0; n=0 allows NULL. Implement normalized RMS EVM: sqrt(sum(|meas-ref|²)/sum(|ref|²)), return NAN for n=0 or zero reference energy. Arrays are finite valid inputs otherwise.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 29
./learn check 29
./learn quiz 29
./learn explain 29
./learn submit 29
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 29` reveals one hint at a time. `./learn solution 29` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain bits/symbol, EVM versus BER, QAM, OFDM and cyclic prefix. What assumptions are missing before claiming a useful net data rate?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
