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
static int fail;
static int live;
void *lab_realloc(void *p, size_t n)
{
    if (fail)
        return NULL;
    if (!p)
        ++live;
    return realloc(p, n);
}
void lab_free(void *p)
{
    if (p)
        --live;
    free(p);
}
int main(void)
{
    struct vec v = {0};
    CHECK(vec_push(NULL, 1) == -1);
    for (int i = 0; i < 1000; ++i)
        CHECK(vec_push(&v, i) == 0);
    for (size_t i = 0; i < v.len; ++i)
        CHECK(v.data[i] == (int)i);
    while (v.len < v.cap)
        CHECK(vec_push(&v, 7) == 0);
    int *old = v.data;
    size_t cap = v.cap, len = v.len;
    fail = 1;
    CHECK(vec_push(&v, 9) == -1 && v.data == old && v.cap == cap && v.len == len && v.data[3] == 3);
    fail = 0;
    CHECK(vec_push(&v, 9) == 0);
    vec_destroy(&v);
    CHECK(!v.data && !v.len && !v.cap && !live);
    vec_destroy(&v);
    vec_destroy(NULL);
    struct vec huge = {.data = (int *)&live, .len = SIZE_MAX, .cap = SIZE_MAX};
    CHECK(vec_push(&huge, 0) == -1);
    return 0;
}
