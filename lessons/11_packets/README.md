# Mission 11: Define the five-byte wire format

Two machines disagree about a native struct layout. Replace it with an explicit packet format.

**Track:** C representations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Struct members stay in declaration order but may have internal and trailing padding. `sizeof` includes padding; `offsetof` reports a member’s offset. Unions overlap storage; enums name integer constants. A native struct is not a portable network packet: alignment, padding, endianness and representations differ.

This packet is exactly five eight-bit bytes: channel, then signed I and signed Q in little-endian 16-bit two’s-complement wire representation. To decode negative values portably, form an unsigned 16-bit magnitude, then subtract 65536 in a wider signed type if bit 15 is set. Do not cast arbitrary byte pointers to struct pointers.

## Trace a small example

```c
struct sample { uint8_t channel; int16_t i, q; };
/* channel=1, i=0x1234, q=-2 encodes 01 34 12 fe ff */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement encode and decode as declared. Return -1 for NULL pointers or n!=5. Error paths preserve the output. Encode into bytes explicitly; decode without unaligned casts. The in-memory struct may be larger than five bytes. Run a small local program printing sizeof and offsetof as an ungraded exploration.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 11
./learn check 11
./learn quiz 11
./learn explain 11
./learn submit 11
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 11` reveals one hint at a time. `./learn solution 11` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain padding, alignment, byte order and why writing sizeof(struct sample) bytes would violate this packet contract.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)
