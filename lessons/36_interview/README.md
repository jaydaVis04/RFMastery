# Mission 36: Defend the engineering decisions

Give a mock interview using your own tested work as evidence.

**Track:** Interview and transfer. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A good technical answer states assumptions, explains a correct approach, tests boundary cases and discusses tradeoffs. Clarify sample format/rate/capacity, full/empty and ownership rules before writing a queue. Distinguish simulation correctness from timing closure and measured throughput from a real-time guarantee.

Practice aloud: declarations, pointer versus array, stack versus heap, malloc/calloc/realloc/free, volatile versus atomic, aliasing, I/Q, AXI handshake, underflow, beamforming. Use one example and one failure mode for each. If the posting becomes available, prioritize its actual required skills over generic curriculum guesses.

## Trace a small example

```text
Prompt: Design a bounded receiver queue.
Clarify → state invariants → implement → test wrap/full/empty → discuss rates.
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Write a 400+ word interview record in design.md: answer five questions from docs/INTERVIEW.md, include two boundary tests, one measured result, one tradeoff, one limitation, and three questions for the team. Keep answers in your own words. The checker only confirms a substantive draft; prose accuracy requires self-review or a human/assistant review. All prior flags are required to award this final mission’s flag. The final quiz mixes the entire course, with 12 questions per session. `./learn interview` draws oral prompts without revealing suggested answers.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 36
./learn check 36
./learn quiz 36
./learn explain 36
./learn submit 36
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 36` reveals one hint at a time. `./learn solution 36` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Give a five-minute walkthrough of the two capstones, including a bug you fixed, evidence of correctness, one limitation, and what you would ask the Battelle team.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [PySDR](https://pysdr.org/)
- [HDLBits exercises](https://hdlbits.01xz.net/wiki/Main_Page)
