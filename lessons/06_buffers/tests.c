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
    CHECK(bounded_len(NULL, 0) == 0);
    char raw[3] = {1, 2, 3};
    CHECK(bounded_len(raw, 3) == 3);
    CHECK(bounded_len("a", 8) == 1);
    unsigned char b[] = {0, 0x41, 0xff};
    char out[16] = "unchanged";
    CHECK(hex_encode(b, 3, out, 6) == -1 && strcmp(out, "unchanged") == 0);
    CHECK(hex_encode(b, 3, out, sizeof out) == 0 && strcmp(out, "0041ff") == 0);
    CHECK(hex_encode(NULL, 0, out, 1) == 0 && out[0] == 0);
    CHECK(hex_encode(b, SIZE_MAX, out, 16) == -1);
    CHECK(hex_encode(NULL, 1, out, 16) == -1);
    CHECK(hex_encode(b, 1, NULL, 16) == -1);
    return 0;
}
