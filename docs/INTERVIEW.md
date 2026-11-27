# Mock interview prompts and review rubric

Use `./learn interview` for five random prompts. Speak before checking notes. Start with a 30–90 second explanation, then a concrete example and failure mode. For a coding prompt, clarify constraints before implementation.

## C reasoning

1. Declare an array of four pointers and a pointer to an array of four ints. Explain the parentheses.
2. Compare pointer and array sizeof behavior in a caller and function parameter.
3. Draw the lifetime/ownership of a local pointer, its allocation and an alias after free.
4. Compare malloc/calloc/realloc/free, including zero-size and failure contracts.
5. A vector loses data when realloc fails. Explain and repair the ownership mistake.
6. Encode a signed I/Q packet portably. Why not cast the struct to bytes?
7. Explain integer promotion, signed overflow and an unsigned countdown bug.
8. Rotate uint32_t by k, including k=0 and k=32. Why are these boundaries important?
9. Design a seven-slot ring, then explain how concurrency changes its assumptions.
10. Show how you diagnose a use-after-free using a sanitizer. What might it miss?
11. Explain volatile versus atomic versus a mutex using separate examples.
12. Interpret Q15, choose accumulator width, and specify rounding/saturation.

## FPGA reasoning

13. Explain what hardware a mux, flip-flop and counter represent.
14. Compare blocking and nonblocking Verilog assignments and explain testbench sampling timing.
15. Draw an FSM and explain reset, malformed input and timeout behavior.
16. Compare latency and throughput before/after pipelining.
17. Explain setup/hold, critical path and why simulation differs from timing analysis.
18. Why is independently synchronizing every bit of a changing word unsafe?
19. Trace valid/ready for a stall, simultaneous consume/replace and reset flush.
20. Specify a software-controlled FIR accelerator: registers, format, ownership, error status and data flow.

## RF/SDR conversation

21. Explain dB versus dBm versus dBi, using a numerical example.
22. Draw an RF receive chain and name ADC, LNA, LO and digital processing roles.
23. Calculate an alias and explain why an anti-alias filter must precede the loss of information.
24. Explain complex I/Q and shift a tone to DC, including the sign convention.
25. Calculate FFT bin spacing and discuss windowing, zero padding and calibration.
26. Explain why downsampling without adequate filtering breaks a receiver.
27. Compare bits/symbol, symbol rate, bit rate and sample rate for QPSK.
28. Explain EVM, BER, OFDM and cyclic prefix with a limitation of each explanation.
29. Explain phase-aware combining and wideband channel calibration.
30. Estimate a four-channel complex-int16 stream’s payload bandwidth and block delay.
31. Compare RX overflow, TX underflow and late timed commands.
32. Draw RU/DU/CU/core and state what the exact functional split depends on.
33. Compare a spectrum analyzer, oscilloscope, signal generator and VNA.
34. A SCPI query times out, then returns a failed measurement. What should the test log say?

## Project defense

35. Show your C capstone’s tests, error contract, rounding, units and benchmark.
36. Show your HDL capstone’s C comparison, accepted transaction counts and reset/flush behavior.
37. Name one bug you fixed and the test that would catch its return.
38. State one limitation and a next experiment that could resolve it.
39. Explain why a CPU, FPGA or GPU might be appropriate for a workload; avoid universal speed claims.

## Self-review rubric

Score each item 0 (cannot explain), 1 (partial/with notes), or 2 (independent and defensible):

| Dimension | What to look for |
|---|---|
| Mechanism | Correct causal explanation rather than an acronym expansion |
| Example | Concrete input/output or event sequence |
| Boundary | Empty/full, overflow, allocation failure, malformed input, stalls or reset as appropriate |
| Evidence | A test, diagnostic, measurement or source that supports the claim |
| Tradeoff | Performance, latency, complexity, resources, accuracy or portability cost |
| Limitation | What is assumed or not proven, and how you would investigate |

Any zero suggests a mission to revisit. These scores are self-assessment aids, not an interview prediction or validated competence scale. Mission 36’s draft should answer five prompts and include evidence from your own work.

## Questions for the internship team

- Which C/C++ standard and build/test tools are used?
- Which FPGA family, HDL and simulator does the team use?
- Which OS, driver interfaces, DMA/streaming protocols and sample formats matter?
- Is intern work mainly host processing, embedded control, FPGA verification, RF automation or a mix?
- Which instruments, measurements and coding practices would help me prepare?
- What would a successful first-month intern deliverable look like?

Public RavenStar material is context, not confirmation of those internal choices.
