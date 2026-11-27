#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct cx {
    double i, q;
};
struct cx combine(const struct cx *x, const struct cx *w, size_t n);
#endif
