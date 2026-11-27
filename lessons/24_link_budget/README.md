# Mission 24: Find the missing link margin

A weak received signal may be entirely predictable. Account for every gain and loss.

**Track:** RF vocabulary and math. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A receive chain often contains antenna → preselection filter → low-noise amplifier (LNA) → mixer/local oscillator (LO) or direct ADC → digital processing. A transmitter reverses the general direction through DAC, filtering and power amplifier (PA). An ADC converts voltage to samples; a DAC does the reverse. Gain cannot repair clipping or remove existing noise.

In a simplified link budget, received dBm = transmit dBm + antenna gains dBi - path/cable losses dB. SNR dB = signal dBm - noise dBm measured over the same bandwidth. This is an estimate: fading, interference, noise figure, distortion, mismatch, and implementation losses may matter. Calibration connects instrument readings to traceable references.

## Trace a small example

```text
20 dBm + 2 dBi + 5 dBi - 95 dB - 3 dB = -71 dBm
SNR with -100 dBm noise in the same bandwidth = 29 dB
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement received_dbm(tx,gt,gr,path,cable) and snr_db(signal,noise). Inputs are finite valid values, gains may be negative, and positive path/cable arguments denote losses. Do not convert to linear units just to add dB terms.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 24
./learn check 24
./learn quiz 24
./learn explain 24
./learn submit 24
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 24` reveals one hint at a time. `./learn solution 24` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Walk through a receiver signal chain, explain LNA/PA/LO/ADC/DAC, and state two limitations of this simple link budget.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
