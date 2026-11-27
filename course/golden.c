#include <stdint.h>
#include <stdio.h>

/* Independent C oracle for mission 35, not the learner's RTL implementation. */
int main(int argc, char **argv)
{
    if (argc != 3)
        return 1;
    FILE *in = fopen(argv[1], "r");
    if (!in)
        return 1;
    FILE *out = fopen(argv[2], "w");
    if (!out) {
        fclose(in);
        return 1;
    }
    int x, previous = 0, older = 0, status;
    int failed = 0;
    while ((status = fscanf(in, "%d", &x)) == 1) {
        if (x < INT16_MIN || x > INT16_MAX) {
            failed = 1;
            break;
        }
        int64_t acc = (int64_t)8192 * x + (int64_t)16384 * previous + (int64_t)8192 * older;
        int64_t y = acc / 32768;
        if (y > INT16_MAX)
            y = INT16_MAX;
        if (y < INT16_MIN)
            y = INT16_MIN;
        if (fprintf(out, "%d\n", (int)y) < 0) {
            failed = 1;
            break;
        }
        older = previous;
        previous = x;
    }
    if (status != EOF || ferror(in))
        failed = 1;
    if (fclose(in) != 0)
        failed = 1;
    if (fclose(out) != 0)
        failed = 1;
    return failed;
}
