#include "lab.h"
struct cx combine(const struct cx *x, const struct cx *w, size_t n)
{
    struct cx y = {0, 0};
    for (size_t i = 0; i < n; ++i) {
        y.i += w[i].i * x[i].i - w[i].q * x[i].q;
        y.q += w[i].i * x[i].q + w[i].q * x[i].i;
    }
    return y;
}
