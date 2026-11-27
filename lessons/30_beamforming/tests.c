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
    struct cx x[] = {{1, 0}, {0, 1}}, w[] = {{1, 0}, {0, -1}};
    struct cx y = combine(x, w, 2);
    CHECK(near(y.i, 2) && near(y.q, 0));
    w[1] = (struct cx){0, 1};
    y = combine(x, w, 2);
    CHECK(near(y.i, 0) && near(y.q, 0));
    y = combine(NULL, NULL, 0);
    CHECK(y.i == 0 && y.q == 0);
    return 0;
}
