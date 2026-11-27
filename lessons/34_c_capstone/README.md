# Mission 34: Ship the offline receiver pipeline

Combine parsing, bounded buffering and DSP into a reproducible command-line receiver component.

**Track:** C capstone. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Integration finds bugs that isolated functions miss. Keep parsing, queue, DSP and CLI concerns in separate translation units. This application reads little-endian signed-int16 I/Q, queues samples, applies the Q15 three-tap FIR independently to I and Q, and writes the same binary format. Histories are zero at start; output count equals input count; no tail flush. Rounding truncates toward zero.

Mean input power here means mean(I²+Q²) in raw count², not watts or dBm. Use a wide intermediate before squaring. Bounded storage limits memory but does not prove real-time operation. Measure plain optimized throughput separately from sanitizer correctness checks.

## Trace a small example

```text
generate.py → input.iq → decode → ring → FIR(I), FIR(Q) → output.iq
                                     └→ mean input count²
compare with an independent Python oracle
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `main.c`, `decode.c`, `ring.c`, `dsp.c` against pipeline.h. Reuse ideas from missions 14, 15 and 17; type and adapt the implementation. Run `pipeline INPUT OUTPUT` (exactly two path arguments). Return zero only after all reads/writes/closes succeed. Reject identical path strings before opening output. Other aliases/hardlinks are outside this educational CLI’s preconditions: use distinct files. Reject truncated input. Error output may be partially written; document that limitation.

On success, print exactly one JSON object with keys samples and mean_power, no other stdout. Empty input succeeds with count=0, mean_power=0. Use a fixed ring of capacity 7 in the processing path, without learner-owned heap allocations; the standard I/O library may allocate internally. The checker exercises public module functions as well as the CLI. On errors print a helpful stderr message and return nonzero. Do not load the entire file. A standard streaming fread loop with four-byte records is sufficient for regular files; this is not a POSIX device driver.

Complete ENGINEERING.md with at least 120 words describing format, ownership, error behavior, rounding, units, and measured throughput. Submission checks the draft length; technical content is self-assessed. `./learn benchmark 34` measures a plain -O2 build on synthetic data after correctness passes. Benchmarks vary by machine and are not hardware real-time guarantees.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 34
./learn check 34
./learn quiz 34
./learn explain 34
./learn submit 34
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 34` reveals one hint at a time. `./learn solution 34` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Walk through the module boundaries, malformed-input behavior, queue bounds, memory ownership, power units and rounding. Explain your measured bottleneck and one limitation.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [PySDR](https://pysdr.org/)
