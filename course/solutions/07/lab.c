#include "lab.h"
#include <stdlib.h>
int *calibration_new(int value)
{
    int *p = malloc(sizeof *p);
    if (p)
        *p = value;
    return p;
}
void calibration_destroy(int **owner)
{
    if (owner) {
        free(*owner);
        *owner = NULL;
    }
}
