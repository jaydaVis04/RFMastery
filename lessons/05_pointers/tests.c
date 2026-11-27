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
    reverse(NULL, 0);
    for (size_t n = 0; n < 129; ++n) {
        int a[130];
        for (size_t i = 0; i < 130; ++i)
            a[i] = (int)i;
        reverse(a, n);
        for (size_t i = 0; i < n; ++i)
            CHECK(a[i] == (int)(n - 1 - i));
        CHECK(a[n] == (int)n);
    }
    return 0;
}
