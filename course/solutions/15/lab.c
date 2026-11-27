#include "lab.h"
static int16_t le(const uint8_t *b)
{
    uint32_t x = (uint32_t)b[0] | ((uint32_t)b[1] << 8);
    return (int16_t)(x >= 32768 ? (int32_t)x - 65536 : (int32_t)x);
}
int decode_iq(const uint8_t *b, size_t n, struct iq *out)
{
    if (!b || !out || n != 4)
        return -1;
    struct iq v = {le(b), le(b + 2)};
    *out = v;
    return 0;
}
