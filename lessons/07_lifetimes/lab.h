#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
int *calibration_new(int value);
void calibration_destroy(int **owner);
#endif
