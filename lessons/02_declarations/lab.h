#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
size_t sample_bytes(size_t n);
int apply(int (*fn)(int), int x);
#endif
