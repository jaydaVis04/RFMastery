#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct fir {
    int16_t z1, z2;
};
int16_t saturate_q15(int64_t acc);
int16_t fir_step(struct fir *s, int16_t x);
#endif
