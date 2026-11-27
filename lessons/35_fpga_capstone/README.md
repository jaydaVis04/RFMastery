# Mission 35: Match hardware to the C golden model

The final accelerator must match C arithmetic exactly while its downstream consumer stalls.

**Track:** FPGA capstone. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Start from the arithmetic contract: signed 16-bit samples, Q15 coefficients [8192,16384,8192], wide signed accumulation, division by 32768 truncating toward zero, saturation, zero history on synchronous reset. Delay history advances only for accepted inputs. The one-slot output retains its value while stalled and can be replaced on simultaneous output/input transfer.

Without stalls, each accepted input becomes visible at the output register after its acceptance edge; it can be consumed on the following edge. Throughput after fill can be one sample/cycle. Stalls extend elapsed latency. Reset discards pending output and history. Compare accepted output transactions, not arbitrary clock-cycle guesses.

## Trace a small example

```text
Deterministic vectors → compiled C golden FIR → expected.txt
          └──────────→ HDL with valid/ready → scoreboard against expected
Reset splits the test into independent zero-history epochs.
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement module lab in lab.v, matching the signed ports. Use a one-slot elastic output, updating history only on s_valid&&s_ready. The grader compiles a C golden model, generates impulse/zero/constant/alternating/extreme/random vectors, and runs a self-checking testbench with randomized stalls and reset/flush. Any mismatch, loss, duplicate or unstable stalled output fails. Use a 64-bit signed accumulator to avoid accidental Verilog width truncation. Add latency/resource/timing limitations to your explanation.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 35
./learn check 35
./learn quiz 35
./learn explain 35
./learn submit 35
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 35` reveals one hint at a time. `./learn solution 35` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain signed widths, scale, C-versus-HDL rounding, handshake stalls, reset/flush, measured cycle latency and why simulation still does not prove synthesis/timing closure.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
- [PySDR](https://pysdr.org/)
