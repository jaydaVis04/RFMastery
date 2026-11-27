#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
double mw_to_dbm(double mw);
double dbm_to_mw(double dbm);
double wavelength_m(double hz);
#endif
