#include "lab.h"
int transition(struct buffer *b, enum event e)
{
    if (!b)
        return -1;
    switch (b->state) {
    case FREE:
        if (e != CLAIM)
            return -1;
        b->state = FILLING;
        break;
    case FILLING:
        if (e != FILLED)
            return -1;
        b->state = READY;
        break;
    case READY:
        if (e != TAKE)
            return -1;
        b->state = PROCESSING;
        break;
    case PROCESSING:
        if (e != RELEASE)
            return -1;
        b->state = FREE;
        break;
    default:
        return -1;
    }
    return 0;
}
