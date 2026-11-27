#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
uint32_t device_status(void);
void clear_events(uint32_t *status, uint32_t ones);
int wait_ready(size_t polls);
#endif
