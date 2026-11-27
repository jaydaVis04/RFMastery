#include "lab.h"
size_t decimate(const double *x, size_t n, size_t m, double *out, size_t cap)
{
    if (!m || (!x && n) || (!out && n))
        return SIZE_MAX;
    size_t need = n / m + (n % m != 0);
    if (cap < need)
        return SIZE_MAX;
    double a = 0, b = 0;
    size_t k = 0;
    for (size_t i = 0; i < n; ++i) {
        double y = .25 * x[i] + .5 * a + .25 * b;
        b = a;
        a = x[i];
        if (i % m == 0)
            out[k++] = y;
    }
    return k;
}
