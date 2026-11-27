#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct cx {
    double i, q;
};
void dft(const struct cx *x, size_t n, struct cx *out);
double bin_hz(size_t k, size_t n, double fs);
#endif
