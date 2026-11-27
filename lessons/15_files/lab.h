#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct iq {
    int16_t i, q;
};
int decode_iq(const uint8_t *b, size_t n, struct iq *out);
#endif
