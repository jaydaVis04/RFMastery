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
static size_t calls, ready_at;
uint32_t device_status(void)
{
    ++calls;
    return calls >= ready_at ? 1u : 0u;
}
int main(void)
{
    uint32_t s = 0xffff;
    clear_events(&s, 0xfff5);
    CHECK(s == 0xfffa);
    clear_events(NULL, 1);
    ready_at = 3;
    CHECK(wait_ready(0) == -1 && calls == 0);
    CHECK(wait_ready(2) == -1 && calls == 2);
    CHECK(wait_ready(9) == 0 && calls == 3);
    calls = 0;
    ready_at = 100;
    CHECK(wait_ready(8) == -1 && calls == 8);
    return 0;
}
