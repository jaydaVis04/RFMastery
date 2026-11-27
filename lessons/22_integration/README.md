# Mission 22: Define accelerator ownership

Host C configures the accelerator while programmable logic processes a stream. Decide who owns each buffer.

**Track:** C and FPGA integration. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

An FPGA contains LUTs, flip-flops, routing, block RAM and often DSP blocks and high-speed interfaces. An SoC FPGA may combine a CPU and fabric. Synthesis maps HDL, placement/routing chooses physical locations, and static timing analysis checks constraints. Software commonly manages configuration and buffers while logic handles sample-rate arithmetic.

Separate control plane (configuration, status, reset) from data plane (sample transport). Before coding, specify sample format, clock domains, coefficients, register semantics, handshake, latency and error handling. A model of ownership is not an actual DMA API.

## Trace a small example

```text
CPU registers → FPGA FIR configuration
Memory ↔ platform DMA ↔ FIFO ↔ FIR ↔ output
FREE → FILLING → READY → PROCESSING → FREE
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `transition(buffer,event)` for FREE+CLAIM→FILLING, FILLING+FILLED→READY, READY+TAKE→PROCESSING, PROCESSING+RELEASE→FREE. Return 0 on legal transition, -1 otherwise, preserving state on error. Reject unknown states and NULL. Add an accelerator contract to your explanation: format, ownership, reset, backpressure and errors.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 22
./learn check 22
./learn quiz 22
./learn explain 22
./learn submit 22
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 22` reveals one hint at a time. `./learn solution 22` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Describe host versus FPGA work, the four ownership states, and the cache/ordering requirements that this simulation does not implement.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Linux device access documentation](https://docs.kernel.org/driver-api/device-io.html)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
