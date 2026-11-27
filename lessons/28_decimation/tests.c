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
    double x[] = {1, 0, 0, 0, 0}, y[8] = {99};
    CHECK(decimate(x, 5, 0, y, 8) == SIZE_MAX && y[0] == 99);
    CHECK(decimate(x, 5, 2, y, 2) == SIZE_MAX && y[0] == 99);
    CHECK(decimate(NULL, 0, 4, NULL, 0) == 0);
    CHECK(decimate(x, 5, 2, y, 8) == 3);
    CHECK(near(y[0], .25) && near(y[1], .25) && near(y[2], 0));
    for (size_t i = 0; i < 5; ++i)
        x[i] = 1;
    CHECK(decimate(x, 5, 1, y, 8) == 5);
    CHECK(near(y[0], .25) && near(y[1], .75) && near(y[4], 1));
    return 0;
}
