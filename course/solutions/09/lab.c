#include "lab.h"
int vec_push(struct vec *v, int x)
{
    if (!v || v->len > v->cap || ((v->cap == 0) != (v->data == NULL)))
        return -1;
    if (v->len == v->cap) {
        if (v->cap > SIZE_MAX / 2)
            return -1;
        size_t c = v->cap ? v->cap * 2 : 4;
        if (c > SIZE_MAX / sizeof *v->data)
            return -1;
        int *p = lab_realloc(v->data, c * sizeof *p);
        if (!p)
            return -1;
        v->data = p;
        v->cap = c;
    }
    v->data[v->len++] = x;
    return 0;
}
void vec_destroy(struct vec *v)
{
    if (v) {
        lab_free(v->data);
        v->data = NULL;
        v->len = 0;
        v->cap = 0;
    }
}
