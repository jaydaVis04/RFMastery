# Resource directory

Read a small section, close it, and implement something. These are study resources and documentation pointers, not a prerequisite to finish every book. Lesson READMEs point you back to relevant sources.

## C and systems

| Resource | Use it for |
|---|---|
| [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/) | Primary introductory text: types, functions, pointers, memory, structs and files. |
| [C reference](https://en.cppreference.com/w/c) | Look up precise library contracts; a reference, not the primary teaching sequence. |
| [Stanford CS107 resources](https://web.stanford.edu/class/cs107/resources/) | Systems C, representations, debugging and memory exercises. |
| [GCC documentation](https://gcc.gnu.org/onlinedocs/) | Warning flags, optimization and build stages. |
| [Clang ASan](https://clang.llvm.org/docs/AddressSanitizer.html) | Runtime memory instrumentation, report interpretation and platform limitations. |
| [Valgrind Memcheck](https://valgrind.org/docs/manual/mc-manual.html) | Additional memory/leak diagnostics on supported platforms; use a separate plain build. |
| [GDB documentation](https://sourceware.org/gdb/documentation/) | Breakpoints, stepping, watchpoints and stack inspection. |
| [LLDB tutorial](https://lldb.llvm.org/use/tutorial.html) | Convenient debugging workflow on this Mac. |
| [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard) | Robustness, integer/memory pitfalls and secure C practices. |
| [Linux man-pages](https://man7.org/linux/man-pages/) | POSIX/Linux return values, partial I/O, errors and system calls. |
| [Linux device I/O](https://docs.kernel.org/driver-api/device-io.html) | MMIO accessors, ordering and platform constraints. |
| [CRC RevEng catalogue](https://reveng.sourceforge.io/crc-catalogue/17plus.htm#crc.cat.crc-32-iso-hdlc) | Exact CRC variants and parameters; a polynomial alone is insufficient. |

## FPGA and streaming

| Resource | Use it for |
|---|---|
| [HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) | Additional combinational, sequential and FSM exercises. |
| [Icarus Verilog](https://steveicarus.github.io/iverilog/) | Simulation installation, compiler/runtime usage and limitations. |
| [GTKWave](https://gtkwave.sourceforge.net/) | Optional waveform inspection; testbench assertions still determine pass/fail. |
| [AMD university HDL material](https://www.amd.com/en/corporate/university-program/vivado/vivado-teaching-material/hdl-design.html) | Vendor-specific examples and implementation flow if relevant to the actual team. |
| [Arm AMBA documentation](https://developer.arm.com/Architectures/AMBA) | AXI/AXI-Stream interface specifications; select the relevant specification/version. |

## RF, DSP and test

| Resource | Use it for |
|---|---|
| [PySDR](https://pysdr.org/) | Primary RF/DSP/SDR teaching text with executable Python examples. |
| [PySDR I/Q sampling](https://pysdr.org/content/sampling) | Sampling, Nyquist, complex representation and receiver context. |
| [DSP Guide](https://www.dspguide.com/) | Filtering/transforms and deeper DSP intuition. |
| [Analog Devices SDR textbook](https://www.analog.com/en/resources/technical-books/software-defined-radio-for-engineers.html) | Radio architectures and communication engineering context. |
| [NumPy FFT](https://numpy.org/doc/stable/reference/routines.fft.html) | Transform conventions, axes and normalization. |
| [SciPy signal](https://docs.scipy.org/doc/scipy/reference/signal.html) | firwin, frequency response and resampling tools. |
| [Ettus UHD manual](https://files.ettus.com/manual/) | Supported USRP interfaces, rates, streaming and timing errors. |
| [Ettus knowledge base](https://kb.ettus.com/) | SDR workshops and hardware documentation. |
| [PyVISA](https://pyvisa.readthedocs.io/) | Real instrument access after completing the offline mock. |

The built-in exercises need no NumPy/SciPy/PyVISA packages. For optional textbook experiments, create your own virtual environment and install packages there; keep the core course environment independent.

## Public product and architecture context

| Resource | Scope |
|---|---|
| [Battelle RavenStar](https://www.battelle.org/markets/industry/communications/ravenstar) | Public O-RAN-compatible radio/aperture and beam-steering description. |
| [Battelle RavenStar antenna brochure](https://www.battelle.org/docs/default-source/industry/brochures/ravenstar-for-5g-and-beyond.pdf) | Public configuration claims, including a broader FR1 span in that brochure; do not conflate versions with an unconfirmed internship platform. |
| [O-RAN Alliance](https://www.o-ran.org/) | Public architecture/specification entry point. |
| [ETSI publication of O-RAN architecture v14](https://www.etsi.org/deliver/etsi_ts/103900_103999/103982/14.00.00_60/ts_103982v140000p.pdf) | A published architecture version for deeper study; not a claim it is the team’s version. |
| [ETSI publication of fronthaul C/U/S planes v17.01](https://www.etsi.org/deliver/etsi_ts/103800_103899/103859/17.01.00_60/ts_103859v170100p.pdf) | Split 7.2x and configurable precoding placement; advanced reference. |

## Learning research

- [Dunlosky et al. 2013](https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html): broad technique review.
- [Karpicke & Roediger 2007](https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JML.pdf): original repeated-retrieval experiments.
- [Chi et al. 1989](https://doi.org/10.1207/s15516709cog1302_1): original worked-example/self-explanation study.

Learning sources, selected C/HDL/device documentation and current public RavenStar descriptions were consulted during course creation on November 26, 2026. Other links are standard reference pointers and were not all individually live-verified. The course’s independently authored exercises do not reproduce those books. See [learning-method notes](LEARNING_METHOD.md) for the limits of the research-to-course inference.
