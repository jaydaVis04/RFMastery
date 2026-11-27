# Mission 15: Decode an interleaved I/Q capture

Your first file from the simulated ADC contains interleaved signed I and Q values.

**Track:** C systems. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Portable C uses FILE* streams; POSIX adds read/write/poll and file descriptors. Calls can be short. `fread` returns items read, `ferror` distinguishes an error from ordinary EOF, and close may fail. errno matters only after an API indicates failure. A complex int16 sample occupies four eight-bit bytes: I low, I high, Q low, Q high.

This mission decodes one framed record at a time. The capstone later handles file open/read/EOF/close and trailing partial records. Do not quietly discard a truncated sample. Units here are raw ADC counts, not calibrated volts or dBm.

## Trace a small example

```text
ff 7f 00 80 → I=32767, Q=-32768
01 00 ff ff → I=1, Q=-1
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `decode_iq(bytes,n,out)` returning 0 for exactly one four-byte record, -1 for invalid pointer or length. Preserve *out on error. Decode signed values portably without unaligned pointer casts. Explain how you would preserve leftover bytes across short reads.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 15
./learn check 15
./learn quiz 15
./learn explain 15
./learn submit 15
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 15` reveals one hint at a time. `./learn solution 15` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Describe EOF versus I/O error, short reads, explicit endianness and what should happen to a one-byte trailing fragment.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [Linux man-pages](https://man7.org/linux/man-pages/)
