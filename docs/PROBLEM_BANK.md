# Transfer and advanced problem bank

These optional problems are for later independent work. Build them in scratch/ or your own project directory; they do not grant automatic flags. State preconditions, write boundary tests, explain the mechanism and compare performance only after correctness. Rebuild a selected problem after a few days with your earlier code closed.

## C foundations and robust APIs

| Problem | Acceptance criteria |
|---|---|
| 1. String primitives | Implement strlen/strcmp for valid terminated strings and memcpy for explicitly nonoverlapping buffers. Explain why binary buffers need lengths and why overlap needs memmove. |
| 2. Integer parser | Use strtol with errno, end pointer, target-range bounds and trailing-character policy. Test empty, whitespace, sign, zero, INT_MIN/MAX, overflow and junk suffix. |
| 3. Bit count | Implement a simple 32-bit scan and x&=x-1 method. Compare zero, all bits, alternating patterns and random values against a trusted reference. |
| 4. Dynamic byte buffer | Implement append/destroy with length/capacity invariants, multiplication/addition overflow checks and allocation-failure injection. Specify append overlap/aliasing policy. |
| 5. Linked list | Insert/delete/reverse, handle empty and one node, and free every node. Compare locality/allocation costs with a contiguous structure. |
| 6. Packet decoder | Validate minimum length, declared length, type and CRC before exposing a payload view. Reject truncated and oversized packets; define ownership of the view. |
| 7. Streaming parser FSM | Parse start/length/payload/checksum from arbitrarily split input chunks. Test noise, partial frames, invalid length, checksum failure and recovery. |
| 8. Fixed memory pool | Allocate/release aligned blocks; detect double release and invalid handles using an index/generation design. Document capacity and stale-handle behavior. |
| 9. Moving average | Use a ring/running sum with explicit startup and overflow bounds. Compare every output with a slow independent recomputation. |
| 10. Complex Q15 multiply | Implement (ac-bd)+j(ad+bc), wide intermediates, documented rounding and saturation. Compare extrema and random cases with a double reference/tolerance. |
| 11. File transport | Loop over POSIX short reads/writes, EINTR and EOF in a testable abstraction. Preserve partial records and report truncated final input. |
| 12. Producer/consumer queue | First use a mutex/condition variables; specify shutdown and full/empty policy. Only then study a C11 SPSC design with documented acquire/release publication. Test ordering and stress; a stress pass does not prove race freedom. |
| 13. Performance experiment | Measure a fixed processing workload at -O0/-O2, separate I/O and computation, report median/range and workload. Prevent dead-code removal by consuming results. |
| 14. Ownership review | Trace all error exits of a multi-resource function. Test failure after each acquisition. Explain aliases and who releases each resource. |
| 15. Portability review | Audit packet/Q15 code for CHAR_BIT, type width, promotion, signed shifts, alignment and narrowing assumptions. Identify what depends on POSIX rather than C17. |

## FPGA verification

| Problem | Acceptance criteria |
|---|---|
| 16. Edge detector | One-cycle pulse on a synchronized signal’s rising edge; explicit reset and adjacent-event contract. Do not confuse this with a complete CDC input solution. |
| 17. Depth-four FIFO | Test empty/full/wrap, simultaneous push/pop, backpressure and reset. Define whether full can accept when also popping and verify it consistently. |
| 18. Framed-stream FSM | Start/payload/end/error/timeout states with a diagram. A malformed marker must recover according to a written rule, not an accidental implementation. |
| 19. Pipelined MAC | Choose signed widths and overflow policy, identify latency, compare against a golden model and count accepted transactions. |
| 20. Valid/ready scoreboard | Randomized stalls and bursts, stability while stalled, no loss/duplication, reset flush. Test multiple deterministic seeds and report them. |
| 21. CDC design review | Choose a control-bit synchronizer, handshake or asynchronous FIFO for three different scenarios. Explain why per-bit synchronization is insufficient for an arbitrary bus. Hardware CDC/timing requires proper tools and constraints. |

## RF, DSP and automation

| Problem | Acceptance criteria |
|---|---|
| 22. Units drill | Convert -30 dBm to watts; apply +6 dB; calculate wavelength at 600 MHz and 7 GHz. Show units and reference levels. |
| 23. Stream budget | Four channels, complex int16, 5 MS/s. Calculate payload bytes/s, then discuss overhead and worst-case block deadlines. |
| 24. Negative-frequency tone | Generate complex -2 kHz, correctly label a shifted spectrum, and explain why its direction differs from +2 kHz. |
| 25. Filter/decimate | Design a real anti-alias FIR for 48→12 kS/s, including passband/transition/attenuation. Use 2 kHz and 10 kHz tones and quantify suppression before/after downsampling. Optional NumPy/SciPy environment needed. |
| 26. Noisy QPSK | Add deterministic Gaussian noise at two levels; compute a specified EVM and BER after explicit decisions. Explain sample/symbol synchronization assumptions. |
| 27. Array combining | Compare aligned, uncorrected and opposite phase voltages, including count² rather than calibrated power unless a reference is supplied. Discuss calibration across frequency. |
| 28. Mock test campaign | Sweep gain/frequency/bandwidth settings with deterministic simulated responses. Log version/calibration/settings/units/time/limits and unavailable measurements separately from RF failures. |
| 29. Instrument resilience | Test timeout, malformed/nonfinite reading, retry exhaustion and valid out-of-limit reading. Never retry a valid result solely to fish for a pass. |
| 30. Architecture brief | Trace samples from antenna/ADC to FPGA/host and RU/DU/CU/core, label assumptions, estimate transport demand and ask three role-specific questions. |

## Selected numerical checks

Keep these closed until you have attempted the calculations:

<details>
<summary>Open selected checks</summary>

- CRC-32/ISO-HDLC for ASCII 123456789 is 0xCBF43926 using the specified reflected algorithm/parameters.
- -30 dBm = 0.001 mW = 1 microwatt = 1e-6 W.
- +6 dB multiplies power by 10^0.6 ≈ 3.981.
- Wavelengths at 600 MHz and 7 GHz are approximately 0.50 m and 0.04286 m in free space.
- Four complex-int16 channels at 5 MS/s require 80,000,000 payload bytes/s before overhead.
- 1 MS/s with N=4096 gives 244.140625 Hz bin spacing.
- A 10 kHz real tone downsampled to 12 kS/s without adequate filtering aliases to 2 kHz, colliding with a desired 2 kHz tone.
- A ring does not require a power-of-two capacity; bitmask wrapping specifically requires appropriate power-of-two assumptions.

</details>
