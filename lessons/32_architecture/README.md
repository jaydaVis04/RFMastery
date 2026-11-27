# Mission 32: Brief the radio team

Prepare a short system briefing that a software intern can explain accurately.

**Track:** RF systems conversation. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A cellular network connects user equipment (UE) through the RAN to a core network. A generic disaggregated 5G picture contains RU, DU and CU. RU handles radio and selected lower-PHY functions; DU handles other PHY/MAC/RLC work; CU handles higher layers. Exact boundaries depend on split/configuration. O-RAN 7.2x is a lower-layer split; fronthaul needs throughput and timing discipline.

Battelle’s public RavenStar page describes a software-defined radio unit with a broadband aperture, beam steering and O-RAN interoperability. This course makes no claim about its internal FPGA vendor, HDL, CPU, OS or internship requirements. Public materials refer to different configurations and frequency spans; confirm the specific product/version rather than treating one number as a universal specification.

## Trace a small example

```text
UE ↔ [antenna/RF + RU] ↔ fronthaul ↔ DU ↔ CU ↔ core
Conceptual industry diagram; not a RavenStar internal architecture.
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Write your briefing in design.md. Include: (1) a labeled UE/RU/DU/CU/core chain, (2) two analog and two digital operations, (3) one fronthaul timing/throughput tradeoff, (4) a cited public RavenStar statement, (5) three questions to ask the internship team. Check evaluates only that a substantive draft exists; explain records your self-assessed reasoning. The quiz checks factual distinctions. Neither automatically judges the technical correctness of your prose.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 32
./learn check 32
./learn quiz 32
./learn explain 32
./learn submit 32
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 32` reveals one hint at a time. `./learn solution 32` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Deliver your briefing aloud in 90 seconds. Explain what you know from public sources and which implementation details you must ask the team to confirm.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Battelle RavenStar public description](https://www.battelle.org/markets/industry/communications/ravenstar)
- [O-RAN Alliance](https://www.o-ran.org/)
