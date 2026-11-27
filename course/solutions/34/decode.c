#include "pipeline.h"
static int16_t le(const uint8_t *b)
{
    uint32_t u = (uint32_t)b[0] | ((uint32_t)b[1] << 8);
    return (int16_t)(u >= 32768 ? (int32_t)u - 65536 : (int32_t)u);
}
int decode(const uint8_t *b, size_t n, struct iq *out)
{
    if (!b || !out || n != 4)
        return -1;
    *out = (struct iq){le(b), le(b + 2)};
    return 0;
}
void encode(uint8_t b[4], struct iq x)
{
    uint16_t i = (uint16_t)x.i, q = (uint16_t)x.q;
    b[0] = (uint8_t)i;
    b[1] = (uint8_t)(i >> 8);
    b[2] = (uint8_t)q;
    b[3] = (uint8_t)(q >> 8);
}
