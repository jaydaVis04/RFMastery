#include "lab.h"
#include <math.h>
struct cx qpsk(unsigned a, unsigned b)
{
    double s = sqrt(.5);
    return (struct cx){a ? -s : s, b ? -s : s};
}
size_t bit_errors(const unsigned char *a, const unsigned char *b, size_t n)
{
    size_t e = 0;
    for (size_t i = 0; i < n; ++i)
        e += (a[i] != b[i]);
    return e;
}
double evm(const struct cx *r, const struct cx *m, size_t n)
{
    double e = 0, p = 0;
    for (size_t i = 0; i < n; ++i) {
        double a = m[i].i - r[i].i, b = m[i].q - r[i].q;
        e += a * a + b * b;
        p += r[i].i * r[i].i + r[i].q * r[i].q;
    }
    return n && p > 0 ? sqrt(e / p) : NAN;
}
