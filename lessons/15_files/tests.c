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
    uint8_t b[] = {0xff, 0x7f, 0, 0x80};
    struct iq x = {8, 9};
    for (size_t n = 0; n < 4; ++n)
        CHECK(decode_iq(b, n, &x) == -1 && x.i == 8 && x.q == 9);
    CHECK(decode_iq(b, 4, &x) == 0 && x.i == 32767 && x.q == -32768);
    for (uint32_t u = 0; u < 65536; u += 31) {
        b[0] = (uint8_t)u;
        b[1] = (uint8_t)(u >> 8);
        CHECK(decode_iq(b, 4, &x) == 0);
        CHECK(x.i == (int32_t)u - (u >= 32768 ? 65536 : 0));
    }
    CHECK(decode_iq(NULL, 4, &x) == -1);
    CHECK(decode_iq(b, 4, NULL) == -1);
    return 0;
}
