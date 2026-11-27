#include "lab.h"
int ring_push(struct ring *r, int x)
{
    if (!r || r->count == RING_CAP)
        return 0;
    r->data[r->head] = x;
    r->head = (r->head + 1) % RING_CAP;
    ++r->count;
    return 1;
}
int ring_pop(struct ring *r, int *out)
{
    if (!r || !out || !r->count)
        return 0;
    *out = r->data[r->tail];
    r->tail = (r->tail + 1) % RING_CAP;
    --r->count;
    return 1;
}
