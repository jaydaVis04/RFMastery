# Mission 21: Survive downstream backpressure

Your data path must hold samples when the next stage stalls.

**Track:** FPGA streaming. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A valid/ready transfer occurs only when both are high at a clock edge. Once valid is asserted, a producer holds data and valid stable until acceptance, except under the defined reset/flush contract. TLAST can identify packet boundaries. A one-slot elastic stage can accept a replacement on the same edge its old value is consumed.

Clock domain crossing risks metastability. Two flip-flops are a common synchronizer for a single slowly changing control bit, not an arbitrary data bus. Independently synchronizing bits can combine bits from different words. Use coherent handshakes or an asynchronous FIFO with a verified CDC design. This lesson has one clock and does not solve CDC.

## Trace a small example

```text
s_ready = !occupied || m_ready
When s_ready: occupied <- s_valid; if s_valid store s_data
While occupied && !m_ready: hold valid and data
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement a one-slot 16-bit elastic stage using the lab.v interface. m_valid is a register; m_data is retained while stalled. On synchronous reset, m_valid becomes 0 and pending data is discarded. s_ready may be combinational !m_valid||m_ready; transfers during reset are ignored. Testbench uses a queue scoreboard, deterministic randomized stalls, simultaneous transfer and drain. Extension: turn it into a depth-four FIFO and add a full/empty test.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 21
./learn check 21
./learn quiz 21
./learn explain 21
./learn submit 21
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 21` reveals one hint at a time. `./learn solution 21` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain all four valid/ready combinations, stall stability, simultaneous replacement, reset flush, and why multibit CDC needs more than independent synchronizers.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
- [Arm AMBA documentation](https://developer.arm.com/Architectures/AMBA)
