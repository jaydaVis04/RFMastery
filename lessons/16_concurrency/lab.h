#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stdatomic.h>
#include <stddef.h>
#include <stdint.h>
void complete(atomic_uint *counter);
unsigned completed(const atomic_uint *counter);
#endif
