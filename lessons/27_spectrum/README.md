# Mission 27: Find the tone in the spectrum

Turn a finite set of samples into frequency bins and distinguish a plotting grid from resolving power.

**Track:** RF and DSP. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

The DFT maps N samples into N complex frequency bins. An FFT efficiently computes the same transform. Bin spacing is fs/N. This small lab uses a direct O(N²) DFT to expose the math; it is not a high-performance FFT implementation. The forward transform uses exp(-j2πkn/N) without normalization.

Non-bin-centered tones leak into many bins. A Hann window reduces sidelobes while broadening the main lobe; amplitude and PSD need suitable normalization. Zero padding interpolates the spectral grid without adding information or true resolving power. Arbitrary FFT magnitude is not calibrated dBm.

## Trace a small example

```text
fs=8000, N=64 → bin spacing=125 Hz
complex +1000 Hz tone → unshifted bin 8
complex -1000 Hz tone → unshifted bin 56 (signed -8)
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `dft(x,N,out)` with forward unnormalized complex DFT and `bin_hz(k,N,fs)` with unshifted bin indexing: k<N/2 maps positive; k>=N/2 maps (k-N)*fs/N. N is even, >=2, and k<N. Buffers do not overlap and are valid. Extension: compare a 1003 Hz tone with/without a Hann window using tools/signal_lab.py.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 27
./learn check 27
./learn quiz 27
./learn explain 27
./learn submit 27
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 27` reveals one hint at a time. `./learn solution 27` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain DFT versus FFT, bin spacing, leakage, windowing, zero padding and why spectrum units require normalization/calibration.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PySDR](https://pysdr.org/)
- [NumPy FFT documentation](https://numpy.org/doc/stable/reference/routines.fft.html)
