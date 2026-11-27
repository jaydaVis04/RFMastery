#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
size_t bounded_len(const char *s, size_t max);
int hex_encode(const unsigned char *src, size_t n, char *dst, size_t cap);
#endif
