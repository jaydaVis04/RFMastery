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
    int *a = calibration_new(7), *b = calibration_new(9);
    CHECK(a && b && a != b && *a == 7 && *b == 9);
    *a = 2;
    CHECK(*b == 9);
    calibration_destroy(&a);
    CHECK(a == NULL);
    calibration_destroy(&a);
    calibration_destroy(NULL);
    calibration_destroy(&b);
    CHECK(b == NULL);
    return 0;
}
