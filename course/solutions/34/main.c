#include "pipeline.h"
#include <stdio.h>
#include <string.h>
int main(int argc, char **argv)
{
    if (argc != 3 || strcmp(argv[1], argv[2]) == 0) {
        fprintf(stderr, "usage: pipeline INPUT OUTPUT (distinct files)\n");
        return 1;
    }
    FILE *in = fopen(argv[1], "rb");
    if (!in) {
        perror("input");
        return 1;
    }
    FILE *out = fopen(argv[2], "wb");
    if (!out) {
        perror("output");
        fclose(in);
        return 1;
    }
    struct ring ring = {0};
    struct fir fi = {0}, fq = {0};
    size_t count = 0;
    long double power = 0;
    int failed = 0;
    uint8_t b[4];
    size_t n;
    while ((n = fread(b, 1, 4, in)) != 0) {
        struct iq x, y;
        if (n != 4 || decode(b, n, &x) != 0) {
            fprintf(stderr, "truncated sample\n");
            failed = 1;
            break;
        }
        if (!push(&ring, x) || !pop(&ring, &y)) {
            fprintf(stderr, "queue contract failed\n");
            failed = 1;
            break;
        }
        power += (long double)y.i * y.i + (long double)y.q * y.q;
        y.i = step(&fi, y.i);
        y.q = step(&fq, y.q);
        encode(b, y);
        if (fwrite(b, 1, 4, out) != 4) {
            fprintf(stderr, "write failed\n");
            failed = 1;
            break;
        }
        ++count;
    }
    if (ferror(in))
        failed = 1;
    if (fclose(in) != 0)
        failed = 1;
    if (fclose(out) != 0)
        failed = 1;
    if (failed) {
        fprintf(stderr, "pipeline failed\n");
        return 1;
    }
    printf("{\"samples\":%zu,\"mean_power\":%.12Lg}\n", count, count ? power / count : 0.L);
    return 0;
}
