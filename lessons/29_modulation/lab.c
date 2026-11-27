#include "lab.h"
struct cx qpsk(unsigned a, unsigned b)
{
    (void)a;
    (void)b;
    return (struct cx){0, 0};
}
size_t bit_errors(const unsigned char *a, const unsigned char *b, size_t n)
{
    (void)a;
    (void)b;
    (void)n;
    return 0;
}
double evm(const struct cx *r, const struct cx *m, size_t n)
{
    (void)r;
    (void)m;
    (void)n;
    return 0;
}
