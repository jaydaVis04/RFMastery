#include "lab.h"
#include <math.h>
double alias_hz(double f, double fs)
{
    if (!isfinite(f) || !isfinite(fs) || fs <= 0)
        return NAN;
    double a = fmod(fabs(f), fs);
    return a > fs / 2 ? fs - a : a;
}
