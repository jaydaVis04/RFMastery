#include "pipeline.h"
int16_t step(struct fir *f, int16_t x)
{
    int64_t a = ((int64_t)8192 * x + (int64_t)16384 * f->z1 + (int64_t)8192 * f->z2) / 32768;
    f->z2 = f->z1;
    f->z1 = x;
    if (a > INT16_MAX)
        a = INT16_MAX;
    if (a < INT16_MIN)
        a = INT16_MIN;
    return (int16_t)a;
}
