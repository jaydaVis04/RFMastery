# C from a blank file

Start here if the first lesson assumes words you have not met. Type the program yourself, then change one thing at a time.

## Your first complete program

```c
#include <stdio.h>

int main(void)
{
    int samples = 16;
    printf("samples=%d\n", samples);
    return 0;
}
```

Save it as scratch/hello.c (create scratch first). Compile and run:

```sh
mkdir -p scratch
cc -std=c17 -Wall -Wextra -Wpedantic -g scratch/hello.c -o scratch/hello
./scratch/hello
```

`#include` makes a library’s declarations available. `int main(void)` defines the program’s application entry function: it returns an int and has no parameters. Braces group its body. `int samples=16;` declares an integer object and initializes it. A semicolon ends that declaration. `printf` is a function call; the format string and samples are arguments. `%d` formats an int, and `\n` is a newline. `return 0` exits main with success. `//` and `/* ... */` introduce comments. Whitespace and indentation help humans; braces and punctuation determine structure.

Try changing 16 to 32; predict before running. Then remove a semicolon, read the error, and fix it. Change `%d` to `%s` and see the warning: format specifiers must match argument types. Do not run a mismatched variadic call to see what happens; fix the warning first.

## Values, types and operators

An object has a type, a value and a lifetime. `int x=3;` initializes x. `x=4;` assigns later. `x==4` compares and produces true/false; it does not assign. Arithmetic includes +, -, *, / and %. Integer division discards the fractional part. `7/2` is 3; `7.0/2` is 3.5 because floating arithmetic is used. Signed integer overflow is undefined; a bigger type is not an unlimited type.

`char` stores a character-sized integer; its signedness is implementation-dependent. `size_t` represents object sizes/counts. `uint16_t` and `int16_t` are exact-width integers if supported; include stdint.h. Use `%zu` for size_t. For fixed-width types, inttypes.h provides macros such as `PRIu32` for portable printing.

```c
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
int main(void) {
    uint32_t frequency_hz = UINT32_C(900000000);
    printf("frequency=%" PRIu32 " Hz, bytes=%zu\n", frequency_hz, sizeof frequency_hz);
    return 0;
}
```

Learn binary and hex for hardware: 0b literals are not C17 syntax; 0x10 is hexadecimal sixteen. One hex digit represents four bits. 0xff is eight one bits. A byte is CHAR_BIT bits; packet labs assume CHAR_BIT==8, supported by the exact eight-bit types on this machine.

## Decisions and loops

```c
if (samples > 10) {
    puts("large block");
} else {
    puts("small block");
}
for (size_t i = 0; i < 4; ++i) {
    printf("%zu\n", i);
}
```

The loop initializes i once, checks i<4 before each iteration, runs the body, then increments i. It prints 0,1,2,3. Use braces. A zero-length loop must do zero accesses. `break` exits a loop; `continue` goes to the next iteration. `&&` requires both conditions; `||` either; `!` negates. `&` is a different bitwise operation or an address operator depending on context.

## Functions and interfaces

```c
int square(int x) { return x*x; } /* precondition: product fits int */
int main(void) { int y=square(5); return y==25 ? 0 : 1; }
```

The function receives a copy of x, calculates a result, and returns it. A prototype, `int square(int x);`, declares the interface before a call. Definitions can live in another .c file; their prototypes belong in a shared header. A function pointer holds a callable function designation with a matching type: `int (*fn)(int)=square;` then `fn(5)` calls square. If that declaration feels hard in mission 2, trace its parentheses and revisit it after mission 4.

## Addresses and arrays

```c
int a[3] = {10,20,30};
int *p = &a[0];
*p = 99; /* a[0] becomes 99 */
```

An array contains elements; a pointer designates an object. `&x` takes its address. `*p` accesses a pointed-to object only while that pointer is valid. `a[i]` accesses the element at index i. Indices are 0..n-1. No runtime bounds checks are automatically inserted by ordinary C. A pointer does not remember array length. Pass a count explicitly.

## Memory, ownership and errors

```c
#include <stdlib.h>
int *p = malloc(3 * sizeof *p);
if (p == NULL) { /* handle failure */ }
else {
    for (size_t i=0; i<3; ++i) p[i]=(int)i;
    free(p);
    p=NULL;
}
```

This fragment needs an enclosing function. `p` is a pointer object; the allocated array is a separate object. Reading uninitialized allocated storage is invalid. The allocation survives leaving the block until freed, but you lose access if you discard its last owning pointer. Decide who owns the resource and who frees it. For variable counts, reject multiplication overflow before allocation; mission 8 teaches this in detail.

## Read failures productively

- A compiler error means translation failed; fix the first useful diagnostic.
- A linker error often means a needed definition or library is missing.
- A nonzero process return means your program/test reported failure.
- An assertion names a behavior the test expected.
- A sanitizer report names a detected runtime mistake, which may have an earlier cause.

Make a prediction, run a small case, compare, and explain the mismatch. Keep that loop small enough to understand.
