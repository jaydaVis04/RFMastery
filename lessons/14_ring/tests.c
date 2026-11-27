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
    struct ring r = {0};
    int out = 77;
    CHECK(!ring_pop(&r, &out) && out == 77);
    CHECK(!ring_push(NULL, 1));
    int next = 0;
    for (int cycle = 0; cycle < 100; ++cycle) {
        for (unsigned i = 0; i < RING_CAP; ++i)
            CHECK(ring_push(&r, next++));
        CHECK(!ring_push(&r, 999));
        CHECK(!ring_pop(&r, NULL));
        for (unsigned i = 0; i < RING_CAP; ++i) {
            CHECK(ring_pop(&r, &out));
            CHECK(out == next - (int)RING_CAP + (int)i);
        }
        CHECK(r.count == 0);
    }
    return 0;
}
