# Vocabulary you should be able to explain

For each term, give the plain explanation, an example, and one limitation/failure. Do not memorize an acronym alone. These are generic concepts, not product internals.

## C and systems

| Term | Plain explanation / useful distinction |
|---|---|
| Declaration | Introduces a name and type; a definition also supplies storage or a body. |
| Translation unit | Source after preprocessing; compiled independently before linking. |
| Linkage | Whether declarations in scopes/files can refer to the same entity. File-scope static gives internal linkage. |
| Pointer | A value designating an object/function or a permitted special value; not a stored length. |
| Array | Contiguous elements of one type; often converts to pointer to first element in expressions. |
| const | Restricts modification through the qualified access; it is not thread synchronization. |
| size_t | Unsigned integer type used for sizes and sizeof results. |
| Storage duration | How long an object exists: automatic, static, thread or allocated. |
| Stack | Common implementation region for call state and automatic objects; not a mandatory C layout. |
| Heap | Common implementation region for dynamic allocations; object lifetime is controlled by allocation/free. |
| malloc | Allocates uninitialized storage or returns NULL; byte size must be safe. |
| calloc | Allocates array storage with zeroed bytes; not a universal pointer/float representation guarantee. |
| realloc | May move storage; nonzero failure preserves the old block; update through a temporary. |
| free | Ends allocated storage lifetime; only base pointer once; free(NULL) is harmless. |
| Ownership | Contract specifying who must release a resource and when. |
| Alias | Another pointer/access path to an object; clearing one pointer does not clear aliases. |
| Undefined behavior | The language imposes no behavior requirements after the violation. A crash is not guaranteed. |
| Alignment | Address constraints for a type; arbitrary byte buffers cannot simply become struct pointers. |
| Padding | Extra bytes/bits used in representation/layout; native struct bytes are not a wire format. |
| Endianness | Byte order for multibyte values; separate from serial bit order. |
| volatile | Specified accesses are observable; does not supply atomics or a thread happens-before relationship. |
| Atomic | An operation with indivisibility and specified ordering semantics; one atomic does not protect every invariant. |
| Data race | Conflicting unsynchronized concurrent accesses with at least one write to ordinary data; undefined in C. |
| DMA | Device/memory transfer mechanism needing platform-specific ownership, completion and coherency handling. |
| Backpressure | A downstream stage asks upstream to wait because it cannot accept more data. |
| Latency | Time from an event/input to a result; distinguish buffering and computation delay. |
| Throughput | Work completed per unit time; a good average does not bound worst-case latency. |
| Sanitizer | Runtime instrumentation detecting selected classes of mistakes, without proving correctness. |
| Q15 | Signed integer scaled by 1/32768; products and rescaling need explicit width/rounding. |
| Saturation | Clamping an out-of-range value to min/max instead of wrapping. |

## FPGA and digital hardware

| Term | Plain explanation / useful distinction |
|---|---|
| FPGA | Configurable hardware fabric; benefits depend on parallelism, determinism, resources and verification effort. |
| LUT | Small configurable truth table implementing Boolean logic. |
| Flip-flop | State element sampling data at a clock edge. |
| Register | Group of state bits; also used for software-visible control/status locations. |
| Block RAM | Dedicated FPGA memory resources. |
| DSP block/slice | Dedicated arithmetic hardware, often multiply/accumulate capable. |
| Combinational logic | Output depends on present inputs, with no intended stored state. |
| Sequential logic | Includes stored state updated according to clocks/events. |
| FSM | Finite state machine: state, transition rules and outputs. |
| Latch | Level-sensitive storage; incomplete combinational assignment may infer one unintentionally. |
| Nonblocking assignment | Verilog <= schedules state updates after evaluation at the triggering timestep. |
| Synthesis | Maps a hardware description into a logic/netlist representation. |
| Place and route | Assigns physical resources and routing; affects timing and congestion. |
| Setup/hold | Required data stability before/after a sampling edge. |
| Critical path | A limiting timing path; reducing it can allow a shorter clock period. |
| Pipeline | Registers divide work into stages; latency and throughput are separate metrics. |
| Metastability | A storage element temporarily fails to resolve cleanly after a timing violation. |
| CDC | Clock domain crossing; requires an appropriate coherent transfer strategy. |
| Two-flop synchronizer | Common risk-reduction technique for a suitable single control signal, not an arbitrary changing bus. |
| FIFO | First-in-first-out queue; synchronous/asynchronous designs have different clock assumptions. |
| AXI-Stream | Streaming protocol; valid and ready both high at a clock edge accept data. |
| TLAST | Optional streaming packet-boundary indication with interface-specific meaning. |
| Timing closure | Meeting required timing constraints after implementation; simulation success is insufficient. |

## RF, DSP and radio systems

| Term | Plain explanation / useful distinction |
|---|---|
| Frequency / wavelength | Cycles/s versus distance per cycle; wavelength≈3e8/f in free space. |
| Phase | Position within an oscillation; relative phase matters for coherent combining. |
| dB | Logarithmic ratio: 10log10 for power, 20log10 for equal-impedance voltage ratios. |
| dBm | Absolute power relative to 1 mW; negative values are positive powers below 1 mW. |
| dBi | Antenna gain relative to an ideal isotropic radiator. |
| SNR | Signal-to-noise ratio; compare levels over compatible bandwidths. |
| Noise figure | Noise degradation added by a component/system under specified conditions. |
| Link budget | Gains/losses accounting; does not by itself prove successful decoding. |
| LNA / PA | Low-noise receive amplifier / power amplifier for transmission. |
| LO / mixer | Local oscillator / frequency translation using multiplication and filtering. |
| ADC / DAC | Analog-to-digital / digital-to-analog converter. |
| Clipping | Amplitude exceeds a system’s range, creating nonlinear distortion. |
| Sampling | Measuring a continuous signal at discrete times. |
| Aliasing | Different continuous signals become indistinguishable after sampling. |
| Nyquist | Real baseband needs sampling above twice its highest bandlimit under ideal assumptions. |
| I/Q | Complex I+jQ representation preserving amplitude and phase information. |
| Baseband | Signal represented around zero frequency; can be real or complex. |
| NCO | Numerically controlled oscillator for digital phase/sine/cosine generation. |
| DFT / FFT | Frequency transform / efficient algorithm computing that transform. |
| Bin spacing | fs/N; distinguish from practical tone resolution. |
| Leakage / window | Finite nonperiodic observation spreads spectrum; window trades sidelobes versus main-lobe width. |
| PSD | Power spectral density, with power-per-bandwidth units and required normalization/calibration. |
| FIR / IIR | Filter with finite feedforward history / recursive filter with feedback and stability considerations. |
| Decimation | Filter then reduce sample rate; suppress frequencies that would alias. |
| Interpolation | Increase sample rate with filtering to suppress images. |
| BPSK / QPSK / QAM | Two phase states / four phase points / amplitude and phase constellation schemes. |
| Symbol rate | Symbols/s; differs from bits/s and samples/s. |
| OFDM | Orthogonal multicarrier modulation commonly using IFFT/FFT and cyclic prefix. |
| EVM / BER | Constellation error magnitude / fraction of incorrect compared bits. |
| Polarization | Electric-field orientation/behavior; mismatch can reduce received signal. |
| MIMO | Multiple transmit/receive paths for spatial communication strategies. |
| Beamforming | Combining complex weights/delays across channels to shape spatial response. |
| Calibration | Relating or correcting measurements/channels against known references. |
| SDR / USRP / UHD | Software-defined radio / Ettus radio hardware family / host driver/API for supported hardware. |
| RX overflow / TX underflow | Receive delivery/consumption too slow / transmit samples not available in time. |
| UE / RU / DU / CU | User equipment / radio unit / distributed unit / central unit in a disaggregated RAN. |
| Fronthaul | Transport between radio and distributed functions; capacity, latency and synchronization matter. |
| O-RAN 7.2x | Lower-layer functional split; specific allocations depend on configuration. |
| SCPI / VISA | Instrument command language / instrument-access architecture; commands vary by model. |
| VNA | Vector network analyzer measuring scattering parameters including reflection and transmission. |

Continue with [Beej](https://beej.us/guide/bgc/html/split/), [PySDR](https://pysdr.org/), [Icarus](https://steveicarus.github.io/iverilog/) and the [resource directory](RESOURCES.md). Definitions here are brief teaching aids; consult complete API and protocol contracts before implementing a real device.
