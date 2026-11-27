#include "lab.h"
int encode(uint8_t *b, size_t n, const struct sample *s)
{
    if (!b || !s || n != 5)
        return -1;
    uint16_t i = (uint16_t)s->i, q = (uint16_t)s->q;
    b[0] = s->channel;
    b[1] = (uint8_t)i;
    b[2] = (uint8_t)(i >> 8);
    b[3] = (uint8_t)q;
    b[4] = (uint8_t)(q >> 8);
    return 0;
}
static int16_t signed16(const uint8_t *b)
{
    uint32_t u = (uint32_t)b[0] | ((uint32_t)b[1] << 8);
    return (int16_t)(u >= 32768 ? (int32_t)u - 65536 : (int32_t)u);
}
int decode(struct sample *s, const uint8_t *b, size_t n)
{
    if (!s || !b || n != 5)
        return -1;
    struct sample tmp = {b[0], signed16(b + 1), signed16(b + 3)};
    *s = tmp;
    return 0;
}
