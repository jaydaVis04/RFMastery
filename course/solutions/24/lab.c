#include "lab.h"
double received_dbm(double t, double a, double b, double p, double c) { return t + a + b - p - c; }
double snr_db(double s, double n) { return s - n; }
