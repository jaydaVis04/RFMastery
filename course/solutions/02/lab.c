#include "lab.h"
size_t sample_bytes(size_t n) { return n * sizeof(uint16_t); }
int apply(int (*fn)(int), int x) { return fn(x); }
