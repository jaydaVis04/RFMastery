#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
uint32_t set_mode(uint32_t reg, uint32_t value);
uint32_t rotl32(uint32_t x, unsigned k);
uint32_t crc32(const unsigned char *b, size_t n);
#endif
