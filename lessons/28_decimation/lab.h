#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
size_t decimate(const double *x, size_t n, size_t m, double *out, size_t cap);
#endif
