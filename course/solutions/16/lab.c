#include "lab.h"
void complete(atomic_uint *c) { atomic_fetch_add_explicit(c, 1u, memory_order_relaxed); }
unsigned completed(const atomic_uint *c) { return atomic_load_explicit(c, memory_order_relaxed); }
