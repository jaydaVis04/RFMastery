# A twelve-week route

Aim for roughly ten hours per week. The schedule is a planning estimate; move forward when you can solve an unfamiliar variation and explain your reasoning. Most effort goes to writing, tracing, testing and debugging C. RF aims for useful engineering conversation and small numerical models; FPGA aims for digital foundations and simulation, without assuming a particular vendor.

| Week | Missions | Evidence to produce |
|---|---|---|
| 1 | 01–04 | Compile a multi-file program, distinguish compiler/linker errors, explain declarations and interfaces |
| 2 | 05–07 | Reverse safely, distinguish strings/binary data, draw object lifetimes |
| 3 | 08–10 | Allocate/free, grow a vector through failure, interpret a sanitizer report |
| 4 | 11–13 | Encode an explicit packet, mask/rotate/CRC, bound simulated register polling |
| 5 | 14–17 | Ring with wrap tests, signed I/Q decode, atomic counter, Q15 FIR |
| 6 | 18–20 | Truth tables, Verilog mux/counter/FSM, testbench scheduling and reset |
| 7 | 21–22 | Hold a stalled stream stable, explain coherent CDC, specify ownership/control plane |
| 8 | 23–25 | dBm/wavelength/link budget calculations, RF chain, anti-aliasing explanation |
| 9 | 26–28 | Complex mixing, spectrum bins/leakage/windowing, filter-before-decimation |
| 10 | 29–33 | Modulation/EVM, beamforming, throughput/loss, architecture briefing, instrument mock |
| 11 | 34 | Reproducible C pipeline, oracle agreement, malformed-input failures, sanitizer run, benchmark |
| 12 | 35–36 | C/HDL agreement under stalls/reset, capstone walkthrough and mixed mock interview |

## A realistic weekly rhythm

- Three 90-minute coding blocks: one small mission or a coherent part of a harder one.
- One 90-minute debugging/refactoring block: repair failing tests and improve interfaces.
- Two one-hour concept blocks: trace, calculate and explain with a few examples.
- Two one-hour review/project blocks: revisit prior work and integrate components.

Move time between these as needed. Missing a day is not a reset. Use `review --all` when you want a short early practice session, and keep failed concepts in rotation. Your schedule and review history are local; no notifications or external calendar events are created.

## C checkpoints

After 04: build and explain a function split across files. After 10: explain who owns every allocation, preserve old data on failure, and interpret a memory report. After 17: implement a bounded ring and integer filter without undefined arithmetic. After 34: show correct CLI errors, binary output and measured throughput.

When reviewing memory, draw two boxes: the pointer variable and the object it designates. Label owner, lifetime and aliases. When reviewing arithmetic, write units and ranges before code. When reviewing streaming, mark only accepted transfers on a timeline.

## If the interview is soon

Prioritize 01–17, then 18–22 and 23–27. Review the glossary, the RU/DU/CU briefing and mock interview prompts. Implement one smaller end-to-end C project rather than claiming to have finished both capstones without evidence. Ask the team which language standard, FPGA toolchain, OS, interfaces and test equipment the internship actually uses. This is prioritization guidance, not a claim about an unprovided Battelle job posting.
