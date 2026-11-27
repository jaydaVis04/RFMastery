#include "pipeline.h"
int push(struct ring *r, struct iq x)
{
    if (!r || r->count == CAP)
        return 0;
    r->data[r->head] = x;
    r->head = (r->head + 1) % CAP;
    ++r->count;
    return 1;
}
int pop(struct ring *r, struct iq *x)
{
    if (!r || !x || !r->count)
        return 0;
    *x = r->data[r->tail];
    r->tail = (r->tail + 1) % CAP;
    --r->count;
    return 1;
}
