#include "lab.h"
char *copy_capture(const char *src, size_t n)
{
    if ((!src && n) || n == SIZE_MAX)
        return NULL;
    char *p = lab_alloc(n + 1);
    if (!p)
        return NULL;
    for (size_t i = 0; i < n; ++i)
        p[i] = src[i];
    p[n] = 0;
    return p;
}
