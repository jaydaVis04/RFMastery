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
    CHECK(saturate_q15(INT64_MAX) == 32767);
    CHECK(saturate_q15(INT64_MIN) == -32768);
    CHECK(saturate_q15(-32767) == 0);
    struct fir s = {0};
    CHECK(fir_step(&s, 32767) == 8191);
    CHECK(fir_step(&s, 0) == 16383);
    CHECK(fir_step(&s, 0) == 8191);
    CHECK(fir_step(&s, 0) == 0);
    uint32_t seed = 17;
    int16_t a = 0, b = 0;
    memset(&s, 0, sizeof s);
    for (int i = 0; i < 5000; ++i) {
        seed = seed * 1664525u + 1013904223u;
        int16_t x = (int16_t)((int32_t)(seed % 65536) - 32768);
        int64_t y = ((int64_t)8192 * x + (int64_t)16384 * a + (int64_t)8192 * b) / 32768;
        CHECK(fir_step(&s, x) == y);
        b = a;
        a = x;
    }
    return 0;
}
