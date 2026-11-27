#include "lab.h"
int16_t saturate_q15(int64_t a)
{
    a /= 32768;
    if (a > INT16_MAX)
        return INT16_MAX;
    if (a < INT16_MIN)
        return INT16_MIN;
    return (int16_t)a;
}
int16_t fir_step(struct fir *s, int16_t x)
{
    int64_t a = (int64_t)8192 * x + (int64_t)16384 * s->z1 + (int64_t)8192 * s->z2;
    s->z2 = s->z1;
    s->z1 = x;
    return saturate_q15(a);
}
