#include "lab.h"
void reverse(int *a, size_t n)
{
    for (size_t i = 0; i < n / 2; ++i) {
        int t = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = t;
    }
}
