# Mission 23: Recover the units

The receiver log mixes watts, milliwatts and dBm. Translate before interpreting it.

**Track:** RF vocabulary and math. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Frequency is cycles per second. Wavelength is propagation speed/frequency; use c≈3e8 m/s in free space. dB expresses a ratio: 10log10(P2/P1) for power; 20log10(V2/V1) for voltage at equal impedance. dBm is an absolute power referenced to 1 mW. dBi is antenna gain relative to an isotropic antenna.

Units belong in every interface. 30 dBm is 1000 mW or 1 W. Negative dBm is not negative power. Converting an FFT’s arbitrary amplitude to dBm requires calibration and an impedance/reference convention.

## Trace a small example

```text
10 mW → 10log10(10) = 10 dBm
1 GHz → 3e8/1e9 = 0.30 m wavelength
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement mw_to_dbm, dbm_to_mw, and wavelength_m. mw_to_dbm rejects nonpositive or nonfinite input with NAN. dbm_to_mw accepts finite -200..200 (return NAN outside); wavelength rejects nonpositive or nonfinite frequency with NAN. Include math.h. Values use milliwatts, dBm, hertz and meters respectively.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 23
./learn check 23
./learn quiz 23
./learn explain 23
./learn submit 23
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 23` reveals one hint at a time. `./learn solution 23` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain dB, dBm and dBi conversationally. Convert -30 dBm to watts and calculate wavelength at 900 MHz.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
