#include "lab.h"
#include <stdlib.h>
int *samples_new(size_t n, int zeroed)
{
    int *p;
    if (n == 0 || n > SIZE_MAX / sizeof *p)
        return NULL;
    return zeroed ? calloc(n, sizeof *p) : malloc(n * sizeof *p);
}
