#include "lab.h"
/* Broken idea: p=lab_alloc(n); for(i=0;i<=n;++i)p[i]=src[i];
   lab_release(p); return p; Find the allocation, bound, and lifetime bugs. */
char *copy_capture(const char *src, size_t n)
{
    (void)src;
    (void)n;
    return 0;
}
