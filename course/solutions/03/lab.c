#include "lab.h"
size_t count_above(const int *x, size_t n, int t)
{
    size_t hits = 0;
    for (size_t i = 0; i < n; ++i)
        if (x[i] > t)
            ++hits;
    return hits;
}
