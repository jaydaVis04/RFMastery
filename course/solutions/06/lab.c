#include "lab.h"
size_t bounded_len(const char *s, size_t max)
{
    size_t i = 0;
    while (i < max && s[i])
        ++i;
    return i;
}
int hex_encode(const unsigned char *s, size_t n, char *d, size_t c)
{
    if (!d || (!s && n) || n > (SIZE_MAX - 1) / 2 || c < 2 * n + 1)
        return -1;
    const char *h = "0123456789abcdef";
    for (size_t i = 0; i < n; ++i) {
        d[2 * i] = h[s[i] >> 4];
        d[2 * i + 1] = h[s[i] & 15];
    }
    d[2 * n] = 0;
    return 0;
}
