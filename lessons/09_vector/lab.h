#ifndef SIGNAL_LAB_H
#define SIGNAL_LAB_H
#include <stddef.h>
#include <stdint.h>
struct vec {
    int *data;
    size_t len, cap;
};
void *lab_realloc(void *p, size_t bytes);
void lab_free(void *p);
int vec_push(struct vec *v, int x);
void vec_destroy(struct vec *v);
#endif
