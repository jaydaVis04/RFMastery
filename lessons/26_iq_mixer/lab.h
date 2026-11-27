#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct cx {
    double i, q;
};
struct cx cmul(struct cx a, struct cx b);
double magnitude(struct cx a);
double phase(struct cx a);
struct cx mix_down(struct cx x, double f0, size_t n, double fs);
#endif
