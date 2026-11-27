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
static int live, fail;
void *lab_alloc(size_t n)
{
    if (fail)
        return NULL;
    void *p = malloc(n);
    if (p)
        ++live;
    return p;
}
void lab_release(void *p)
{
    if (p)
        --live;
    free(p);
}
int main(void)
{
    char raw[] = {65, 0, 66};
    for (size_t n = 0; n <= 3; ++n) {
        char *p = copy_capture(raw, n);
        CHECK(p && memcmp(p, raw, n) == 0 && p[n] == 0);
        lab_release(p);
    }
    CHECK(copy_capture(NULL, 1) == NULL);
    CHECK(copy_capture(raw, SIZE_MAX) == NULL);
    char *p = copy_capture(NULL, 0);
    CHECK(p && p[0] == 0);
    lab_release(p);
    fail = 1;
    CHECK(copy_capture(raw, 3) == NULL);
    CHECK(live == 0);
    return 0;
}
