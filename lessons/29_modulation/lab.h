#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct cx {
    double i, q;
};
struct cx qpsk(unsigned b0, unsigned b1);
size_t bit_errors(const unsigned char *a, const unsigned char *b, size_t n);
double evm(const struct cx *ref, const struct cx *meas, size_t n);
#endif
