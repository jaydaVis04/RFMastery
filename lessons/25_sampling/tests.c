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
    CHECK(near(alias_hz(850, 1000), 150));
    CHECK(near(alias_hz(-2700, 1000), 300));
    CHECK(near(alias_hz(1000, 1000), 0));
    CHECK(near(alias_hz(500, 1000), 500));
    CHECK(isnan(alias_hz(1, 0)));
    CHECK(isnan(alias_hz(NAN, 1000)));
    for (int f = -3000; f <= 3000; f += 37) {
        double a = alias_hz(f, 1000);
        CHECK(a >= 0 && a <= 500);
        for (int n = 0; n < 5; ++n)
            CHECK(
                near(cos(6.283185307179586 * f * n / 1000), cos(6.283185307179586 * a * n / 1000)));
    }
    return 0;
}
