#include "lab.h"
#include <math.h>
struct cx cmul(struct cx a, struct cx b)
{
    return (struct cx){a.i * b.i - a.q * b.q, a.i * b.q + a.q * b.i};
}
double magnitude(struct cx a) { return hypot(a.i, a.q); }
double phase(struct cx a) { return atan2(a.q, a.i); }
struct cx mix_down(struct cx x, double f, size_t n, double fs)
{
    double a = 6.283185307179586 * f * (double)n / fs;
    return cmul(x, (struct cx){cos(a), -sin(a)});
}
