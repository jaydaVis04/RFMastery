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
    CHECK(count_above(NULL, 0, 0) == 0);
    int x[257];
    for (int t = -6; t <= 6; ++t) {
        size_t want = 0;
        for (size_t i = 0; i < 257; ++i) {
            x[i] = (int)(i % 13) - 6;
            want += (x[i] > t);
        }
        CHECK(count_above(x, 257, t) == want);
    }
    return 0;
}
