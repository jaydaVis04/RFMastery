#include "lab.h"
#include <math.h>
void dft(const struct cx *x, size_t n, struct cx *o)
{
    for (size_t k = 0; k < n; ++k) {
        double re = 0, im = 0;
        for (size_t j = 0; j < n; ++j) {
            double a = 6.283185307179586 * (double)k * (double)j / (double)n;
            re += x[j].i * cos(a) + x[j].q * sin(a);
            im += x[j].q * cos(a) - x[j].i * sin(a);
        }
        o[k] = (struct cx){re, im};
    }
}
double bin_hz(size_t k, size_t n, double fs)
{
    double signed_bin = k < n / 2 ? (double)k : (double)k - (double)n;
    return signed_bin * fs / (double)n;
}
