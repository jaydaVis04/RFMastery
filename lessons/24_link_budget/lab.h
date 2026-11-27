#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
double received_dbm(double tx, double gt, double gr, double path, double cable);
double snr_db(double signal, double noise);
#endif
