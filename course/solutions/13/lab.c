#include "lab.h"
void clear_events(uint32_t *s, uint32_t o)
{
    if (s)
        *s &= ~(o & 15u);
}
int wait_ready(size_t polls)
{
    for (size_t i = 0; i < polls; ++i)
        if (device_status() & 1u)
            return 0;
    return -1;
}
