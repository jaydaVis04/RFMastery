#include "lab.h"
uint32_t set_mode(uint32_t r, uint32_t v) { return (r & ~UINT32_C(0xf0)) | ((v & 15u) << 4); }
uint32_t rotl32(uint32_t x, unsigned k)
{
    k %= 32;
    return k ? (uint32_t)((x << k) | (x >> (32 - k))) : x;
}
uint32_t crc32(const unsigned char *b, size_t n)
{
    uint32_t c = UINT32_C(0xffffffff);
    for (size_t i = 0; i < n; ++i) {
        c ^= b[i];
        for (int j = 0; j < 8; ++j)
            c = (c >> 1) ^ ((c & 1u) ? UINT32_C(0xedb88320) : 0u);
    }
    return c ^ UINT32_C(0xffffffff);
}
