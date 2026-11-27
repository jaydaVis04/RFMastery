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
    enum event ev[] = {CLAIM, FILLED, TAKE, RELEASE};
    for (int s = 0; s < 4; ++s)
        for (int e = 0; e < 5; ++e) {
            struct buffer b = {(enum buffer_state)s};
            int good = (e == (int)ev[s]);
            CHECK(transition(&b, (enum event)e) == (good ? 0 : -1));
            CHECK((int)b.state == (good ? (s + 1) % 4 : s));
        }
    struct buffer b = {(enum buffer_state)99};
    CHECK(transition(&b, CLAIM) == -1 && (int)b.state == 99);
    CHECK(transition(NULL, CLAIM) == -1);
    return 0;
}
