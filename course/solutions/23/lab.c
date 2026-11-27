#include "lab.h"
#include <math.h>
double mw_to_dbm(double x) { return isfinite(x) && x > 0 ? 10 * log10(x) : NAN; }
double dbm_to_mw(double x) { return isfinite(x) && x >= -200 && x <= 200 ? pow(10, x / 10) : NAN; }
double wavelength_m(double x) { return isfinite(x) && x > 0 ? 3e8 / x : NAN; }
