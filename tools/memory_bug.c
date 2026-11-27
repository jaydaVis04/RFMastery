/* Intentionally broken examples for mission 10. Run one at a time under ASan.
 * Work on a copy when repairing them. These are not reference implementations. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Choose bounds or lifetime (intentionally invalid access)\n");
        return 1;
    }
    volatile int *p = malloc(4 * sizeof *p);
    if (!p)
        return 1;
    p[0] = 7;
    if (strcmp(argv[1], "bounds") == 0) {
        p[4] = 99; /* BUG: allocation has indices 0..3. */
        free((void *)p);
    } else if (strcmp(argv[1], "lifetime") == 0) {
        free((void *)p);
        printf("%d\n", p[0]); /* BUG: allocated object's lifetime ended. */
    } else {
        free((void *)p);
        fprintf(stderr, "Unknown mode\n");
        return 1;
    }
    return 0;
}
