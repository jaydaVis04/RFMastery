#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct sample {
    uint8_t channel;
    int16_t i, q;
};
int encode(uint8_t *b, size_t n, const struct sample *s);
int decode(struct sample *s, const uint8_t *b, size_t n);
#endif
