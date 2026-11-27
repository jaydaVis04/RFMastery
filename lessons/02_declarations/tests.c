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
static int twice(int x) { return x * 2; }
int main(void)
{
    CHECK(sample_bytes(0) == 0);
    for (size_t n = 1; n < 300; ++n)
        CHECK(sample_bytes(n) == n * sizeof(uint16_t));
    CHECK(apply(twice, 21) == 42);
    CHECK(apply(twice, -9) == -18);
    return 0;
}
