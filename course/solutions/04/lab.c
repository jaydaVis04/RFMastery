#include "lab.h"
int clamp_checked(int x, int lo, int hi, int *out)
{
    if (!out || lo > hi)
        return -1;
    *out = x < lo ? lo : (x > hi ? hi : x);
    return 0;
}
