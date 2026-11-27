# Mission 30: Align two antenna channels

Two antennas receive the same signal with different phases. Align them before combining.

**Track:** RF vocabulary and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Antennas have radiation patterns, gain, polarization, impedance and bandwidth. MIMO uses multiple signal paths. Beamforming combines complex weighted channels to favor directions or spatial channels. Coherent voltages add with phase; powers alone cannot represent cancellation. Two unit voltages aligned sum to magnitude two, while opposite phases cancel.

Element spacing relative to wavelength changes with frequency. Wideband arrays need gain/phase/timing calibration across channels and frequency. A simple narrowband phase-weight model does not capture true-time-delay requirements or full array patterns. Do not infer RavenStar internals from this toy model.

## Trace a small example

```text
a=1+j0, b=0+j1 → a+b=1+j1 (magnitude sqrt(2))
weight b by -j → a+(-j)b=2+j0
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `combine(x,w,n)` as sum(w[k]*x[k]) with no conjugation (weights already contain the chosen correction). NULL arrays are allowed for n=0, returning {0,0}. Inputs are finite/moderate. Include a cancellation test in your own notes.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 30
./learn check 30
./learn quiz 30
./learn explain 30
./learn submit 30
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 30` reveals one hint at a time. `./learn solution 30` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain coherent combining, MIMO, polarization, half-wavelength spacing and why channel calibration matters over a wide band.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
- [Battelle public RavenStar page](https://www.battelle.org/markets/industry/communications/ravenstar)
