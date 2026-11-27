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
    CHECK(near(mw_to_dbm(10), 10));
    CHECK(near(mw_to_dbm(.01), -20));
    CHECK(near(dbm_to_mw(30), 1000));
    for (int d = -100; d <= 100; d += 5)
        CHECK(near(mw_to_dbm(dbm_to_mw(d)), d));
    CHECK(near(wavelength_m(900e6), 1.0 / 3));
    CHECK(isnan(mw_to_dbm(0)) && isnan(mw_to_dbm(INFINITY)));
    CHECK(isnan(dbm_to_mw(NAN)) && isnan(dbm_to_mw(201)));
    CHECK(isnan(wavelength_m(-1)));
    return 0;
}
