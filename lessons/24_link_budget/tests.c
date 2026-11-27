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
    CHECK(near(received_dbm(20, 2, 5, 95, 3), -71));
    CHECK(near(snr_db(-71, -100), 29));
    for (int i = 0; i < 100; ++i)
        CHECK(near(received_dbm(i, -2, 3, i * 2, 4), -i - 3));
    CHECK(near(snr_db(-110, -100), -10));
    return 0;
}
