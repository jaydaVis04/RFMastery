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
    int y = 99;
    CHECK(clamp_checked(3, 5, 4, &y) == -1 && y == 99);
    CHECK(clamp_checked(0, 0, 1, NULL) == -1);
    for (int x = -20; x <= 20; ++x) {
        CHECK(clamp_checked(x, -8, 7, &y) == 0);
        CHECK(y == (x < -8 ? -8 : x > 7 ? 7 : x));
    }
    CHECK(clamp_checked(INT_MIN, INT_MIN, INT_MAX, &y) == 0 && y == INT_MIN);
    return 0;
}
