# Mission 31: Account for missing receiver blocks

The synthetic receiver reports numbered blocks. Detect lost samples rather than trusting a plausible plot.

**Track:** SDR systems. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

SDR implements many radio functions in software or programmable logic, while RF converters, gain, analog bandwidth and transport remain physical limits. UHD is the host driver/API for supported USRPs. RX overflow means receive samples were not delivered or consumed in time; TX underflow means timely transmit data was missing. Late timed commands are another failure category.

Complex int16 uses four payload bytes/sample. At 10 MS/s, that is 40 MB/s/channel before overhead. A 4096-sample block at 1 MS/s spans 4.096 ms. Bigger blocks amortize overhead but increase buffering delay. Measure worst-case time as well as averages; offline timing is not proof of hardware real-time operation.

## Trace a small example

```text
sequence 0,1,4,5 → blocks 2 and 3 are missing
4 channels × 5 MS/s × 4 bytes = 80,000,000 bytes/s payload
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement payload_bps(rate,channels,bytes_per_sample=4), block_ms(count,rate), and missing_blocks(seqs). Nonpositive rate/channels/bytes_per_sample and negative count raise ValueError. Sequences must be nonnegative, strictly increasing integers; empty is valid. Count gaps between observed blocks only (no assumed missing prefix). Reject duplicates, backwards or negative values with ValueError. Use Python stdlib only.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 31
./learn check 31
./learn quiz 31
./learn explain 31
./learn submit 31
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 31` reveals one hint at a time. `./learn solution 31` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain overflow, underflow, late commands, throughput versus latency, and your policy for sequence gaps.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Ettus UHD manual](https://files.ettus.com/manual/)
- [PySDR](https://pysdr.org/)
