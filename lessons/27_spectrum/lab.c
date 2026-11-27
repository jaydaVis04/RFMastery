#include "lab.h"
void dft(const struct cx *x, size_t n, struct cx *out)
{
    (void)x;
    for (size_t k = 0; k < n; ++k)
        out[k] = (struct cx){0, 0};
}
double bin_hz(size_t k, size_t n, double fs)
{
    (void)k;
    (void)n;
    (void)fs;
    return 0;
}
