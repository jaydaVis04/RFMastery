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
static int near(double a, double b) { return fabs(a - b) < 1e-8 * (1.0 + fabs(b)); }
int main(void)
{
    struct cx x[64], y[64];
    for (int tone = -7; tone <= 7; ++tone) {
        for (int j = 0; j < 64; ++j) {
            double a = 6.283185307179586 * tone * j / 64;
            x[j] = (struct cx){cos(a), sin(a)};
        }
        dft(x, 64, y);
        for (int k = 0; k < 64; ++k) {
            CHECK(near(y[k].i, k == (tone + 64) % 64 ? 64 : 0));
            CHECK(near(y[k].q, 0));
        }
    }
    CHECK(near(bin_hz(8, 64, 8000), 1000));
    CHECK(near(bin_hz(56, 64, 8000), -1000));
    CHECK(near(bin_hz(32, 64, 8000), -4000));
    return 0;
}
