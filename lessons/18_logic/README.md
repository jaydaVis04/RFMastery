# Mission 18: Route the digital input

Before clocking samples through hardware, build a combinational selector and exhaustively test it.

**Track:** FPGA foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Combinational logic depends only on current inputs. Sequential logic includes state stored in flip-flops. Gates implement AND, OR, XOR and NOT. A mux selects one input. A LUT implements a Boolean function; a register stores bits at a clock edge. HDL describes concurrent hardware, not a sequence of CPU instructions.

Use assign or an always @* block for combinational logic. Every path must drive the output to avoid accidental latch inference. This mission uses a four-input, one-bit mux. It needs no clock.

## Trace a small example

```verilog
assign y = sel ? b : a; // 2:1 mux
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement module lab with inputs wire [3:0] data, input wire [1:0] sel, output wire y. y must equal data[sel]. Fill in the existing module body. The testbench exhausts all 64 combinations, then prints PASS. No hardware board is used. Write truth tables for AND/OR/XOR as extra practice.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 18
./learn check 18
./learn quiz 18
./learn explain 18
./learn submit 18
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 18` reveals one hint at a time. `./learn solution 18` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain combinational versus sequential logic. Why does this mux need no clock, while a counter does?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
