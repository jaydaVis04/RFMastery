#ifndef PIPELINE_H
#define PIPELINE_H
#include <stddef.h>
#include <stdint.h>
struct iq {
    int16_t i, q;
};
#define CAP 7u
struct ring {
    struct iq data[CAP];
    size_t head, tail, count;
};
struct fir {
    int16_t z1, z2;
};
int decode(const uint8_t *b, size_t n, struct iq *out);
void encode(uint8_t b[4], struct iq x);
int push(struct ring *r, struct iq x);
int pop(struct ring *r, struct iq *x);
int16_t step(struct fir *f, int16_t x);
#endif
