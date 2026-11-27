#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
enum buffer_state { FREE, FILLING, READY, PROCESSING };
enum event { CLAIM, FILLED, TAKE, RELEASE };
struct buffer {
    enum buffer_state state;
};
int transition(struct buffer *b, enum event e);
#endif
