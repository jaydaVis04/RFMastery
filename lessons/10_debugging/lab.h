#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
void *lab_alloc(size_t n);
void lab_release(void *p);
char *copy_capture(const char *src, size_t n);
#endif
