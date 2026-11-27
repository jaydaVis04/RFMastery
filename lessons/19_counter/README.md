# Mission 19: Clock the sample counter

Count clock edges, wrap at sixteen, and recover from reset during a capture.

**Track:** FPGA foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Use nonblocking <= assignments for clocked state updates. Their right-hand sides are evaluated at the triggering edge and updates become visible later in the simulation timestep. Testbenches must check after those updates, for example at #1 after posedge. Blocking = is normally used for combinational calculations.

This counter has synchronous active-high reset: reset is sampled only on a rising edge. It is not an asynchronous reset. Simulation checks functional behavior; synthesis maps hardware, placement/routing assigns resources and wires, and timing analysis checks constraints. Passing simulation alone does not prove timing closure.

## Trace a small example

```verilog
always @(posedge clk) begin
  if (rst) q <= 4'd0;
  else q <= q + 4'd1;
end
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement a four-bit counter with the exact module lab ports in lab.v. The bench uses a 10 ns clock, tests reset at startup and midstream, and checks wraparound. It writes wave.vcd into the build folder for optional GTKWave inspection.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 19
./learn check 19
./learn quiz 19
./learn explain 19
./learn submit 19
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 19` reveals one hint at a time. `./learn solution 19` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain nonblocking updates, synchronous reset, simulation scheduling and why simulation cannot prove hardware timing.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
