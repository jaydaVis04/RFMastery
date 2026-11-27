# Mission 12: Protect the control word

Control fields must preserve unrelated register bits, and capture packets need an integrity check.

**Track:** C representations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

Use unsigned types for masks and shifts. A shift count must be nonnegative and less than the promoted left operand’s width. Signed left shift has additional constraints; right shifting negative signed values is implementation-defined in C17. A rotate by zero needs special handling to avoid shifting by 32.

Byte order differs from bit order. CRC-32/ISO-HDLC uses reflected polynomial 0xEDB88320, initial 0xFFFFFFFF, final XOR 0xFFFFFFFF, processing each byte least-significant bit first. A CRC detects accidental corruption; it is not cryptographic authentication.

## Trace a small example

```c
uint32_t next = (reg & ~UINT32_C(0xf0)) | ((value & 15u)<<4);
/* Preserve everything outside bits 7:4. */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement set_mode for bits 7:4, rotate-left with k reduced modulo 32, and reflected CRC-32. CRC accepts NULL only for n=0; its empty-buffer result is zero. Do not shift by 32. The known ASCII 123456789 check value is 0xCBF43926.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 12
./learn check 12
./learn quiz 12
./learn explain 12
./learn submit 12
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 12` reveals one hint at a time. `./learn solution 12` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain how you preserve unrelated bits, why rotate(0) needs care, and why CRC cannot prove authenticity.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
- [CRC catalogue parameters](https://reveng.sourceforge.io/crc-catalogue/17plus.htm#crc.cat.crc-32-iso-hdlc)
