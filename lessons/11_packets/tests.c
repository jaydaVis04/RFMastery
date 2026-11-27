#include "lab.h"
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define CHECK(x)                                                                                   \
    do {                                                                                           \
        if (!(x)) {                                                                                \
            fprintf(stderr, "FAIL line %d: %s\n", __LINE__, #x);                                   \
            return 1;                                                                              \
        }                                                                                          \
    } while (0)
int main(void)
{
    uint8_t b[5], want[] = {1, 0x34, 0x12, 0xfe, 0xff};
    struct sample s = {1, 0x1234, -2}, d = {9, 8, 7};
    CHECK(encode(b, 5, &s) == 0 && memcmp(b, want, 5) == 0);
    CHECK(decode(&d, b, 4) == -1 && d.i == 8);
    for (int i = -32768; i <= 32767; i += 257) {
        s.i = (int16_t)i;
        s.q = (int16_t)(-1 - i);
        CHECK(encode(b, 5, &s) == 0);
        CHECK(decode(&d, b, 5) == 0 && d.i == s.i && d.q == s.q && d.channel == 1);
    }
    CHECK(encode(NULL, 5, &s) == -1);
    CHECK(decode(NULL, b, 5) == -1);
    return 0;
}
