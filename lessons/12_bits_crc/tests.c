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
    CHECK(set_mode(0xa5a5a5a5u, 0x123) == 0xa5a5a535u);
    for (unsigned k = 0; k < 100; ++k) {
        uint32_t x = 0x81234567u, y = x;
        for (unsigned j = 0; j < k % 32; ++j)
            y = (uint32_t)((y << 1) | (y >> 31));
        CHECK(rotl32(x, k) == y);
    }
    CHECK(crc32(NULL, 0) == 0);
    CHECK(crc32((const unsigned char *)"123456789", 9) == 0xcbf43926u);
    unsigned char a[] = {0, 1, 2, 255};
    CHECK(crc32(a, 4) == 0x3fb23824u);
    return 0;
}
