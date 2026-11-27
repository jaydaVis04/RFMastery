# Mission 20: Recognize a framed command

Commands arrive as bytes. Recognize start, payload and end markers while recovering from errors.

**Track:** FPGA foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

An FSM has state storage, next-state logic, and outputs. A Moore output depends on state; a Mealy output may also depend on current input. Supply default assignments in combinational logic. Setup and hold specify stability around the capture edge. A long combinational critical path limits clock speed.

Pipelining adds registers to shorten paths; it can increase latency while preserving one-result-per-cycle throughput after fill. This parser’s accepted byte event is valid=1 at posedge. It recognizes exactly A5, any one payload byte, 5A. There is no ready signal; valid=0 leaves parser progress unchanged.

## Trace a small example

```text
IDLE --valid A5--> PAYLOAD --valid any--> END
END --valid 5A--> IDLE + one-cycle done
END --valid other--> IDLE, no done
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement this three-state parser in module lab. Synchronous reset discards partial frames and clears done. done is a one-cycle pulse (clear each clock unless a completed frame occurs), even if valid becomes zero. Inputs in IDLE other than A5 are ignored. A wrong end marker is discarded without being treated as a new start. No timeout is required in the graded design; sketch one as an extension.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 20
./learn check 20
./learn quiz 20
./learn explain 20
./learn submit 20
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 20` reveals one hint at a time. `./learn solution 20` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Draw the FSM, explain the invalid end-marker rule, and compare pipeline latency to throughput. How would a timeout alter the state machine?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
- [Icarus Verilog documentation](https://steveicarus.github.io/iverilog/)
