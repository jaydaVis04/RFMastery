#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
#define RING_CAP 7u
struct ring {
    int data[RING_CAP];
    size_t head, tail, count;
};
int ring_push(struct ring *r, int x);
int ring_pop(struct ring *r, int *out);
#endif
