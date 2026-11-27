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
    struct cx a = {3, 4}, b = {-2, 1}, c = cmul(a, b);
    CHECK(near(c.i, -10) && near(c.q, -5));
    CHECK(near(magnitude(a), 5));
    CHECK(near(phase((struct cx){-1, 1}), 2.356194490192345));
    for (size_t n = 0; n < 100; ++n) {
        double t = 6.283185307179586 * 1000 * n / 10000;
        struct cx y = mix_down((struct cx){cos(t), sin(t)}, 1000, n, 10000);
        CHECK(near(y.i, 1) && near(y.q, 0));
    }
    return 0;
}
