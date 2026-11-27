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
#include <pthread.h>
static atomic_uint c;
static void *work(void *p)
{
    (void)p;
    for (int i = 0; i < 25000; ++i)
        complete(&c);
    return NULL;
}
int main(void)
{
    pthread_t t[4];
    atomic_init(&c, 0);
    CHECK(completed(&c) == 0);
    for (int i = 0; i < 4; ++i)
        CHECK(pthread_create(&t[i], NULL, work, NULL) == 0);
    for (int i = 0; i < 4; ++i)
        CHECK(pthread_join(t[i], NULL) == 0);
    CHECK(completed(&c) == 100000);
    return 0;
}
