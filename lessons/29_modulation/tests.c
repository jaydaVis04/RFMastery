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
    for (unsigned a = 0; a < 2; ++a)
        for (unsigned b = 0; b < 2; ++b) {
            struct cx z = qpsk(a, b);
            CHECK((z.i < 0) == (a != 0) && (z.q < 0) == (b != 0));
            CHECK(near(z.i * z.i + z.q * z.q, 1));
        }
    unsigned char a[] = {0, 1, 1, 0}, b[] = {1, 1, 0, 0};
    CHECK(bit_errors(a, b, 4) == 2);
    CHECK(bit_errors(NULL, NULL, 0) == 0);
    struct cx r[] = {{1, 0}, {0, 1}}, m[] = {{1.1, 0}, {0, 1.1}};
    CHECK(near(evm(r, m, 2), .1));
    CHECK(isnan(evm(r, m, 0)));
    struct cx zero = {0, 0};
    CHECK(isnan(evm(&zero, &zero, 1)));
    return 0;
}
