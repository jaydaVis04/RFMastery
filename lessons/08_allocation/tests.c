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
    CHECK(samples_new(0, 1) == NULL);
    CHECK(samples_new(SIZE_MAX, 0) == NULL);
    for (size_t n = 1; n <= 1000; n *= 10) {
        int *p = samples_new(n, 1);
        CHECK(p);
        for (size_t i = 0; i < n; ++i)
            CHECK(p[i] == 0);
        free(p);
        p = samples_new(n, 0);
        CHECK(p);
        for (size_t i = 0; i < n; ++i)
            p[i] = (int)i;
        CHECK(p[n - 1] == (int)n - 1);
        free(p);
    }
    return 0;
}
