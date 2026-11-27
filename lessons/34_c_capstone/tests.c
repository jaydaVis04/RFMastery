#include "pipeline.h"
#include <assert.h>
#include <string.h>
int main(void)
{
    struct ring r = {0};
    struct iq x = {11, -12}, o = {0};
    assert(!pop(&r, &o));
    for (int j = 0; j < 7; ++j) {
        x.i = (int16_t)j;
        assert(push(&r, x));
    }
    assert(!push(&r, x));
    for (int j = 0; j < 7; ++j) {
        assert(pop(&r, &o));
        assert(o.i == j);
    }
    assert(!pop(&r, &o));
    for (int cycle = 0; cycle < 40; ++cycle) {
        assert(push(&r, x));
        assert(pop(&r, &o));
        assert(o.q == x.q);
    }
    uint8_t b[4];
    x = (struct iq){-32768, 32767};
    encode(b, x);
    assert(b[0] == 0 && b[1] == 128 && b[2] == 255 && b[3] == 127);
    assert(decode(b, 4, &o) == 0 && o.i == x.i && o.q == x.q);
    assert(decode(b, 3, &o) == -1);
    struct fir f = {0};
    assert(step(&f, 32767) == 8191);
    assert(step(&f, 0) == 16383);
    assert(step(&f, 0) == 8191);
    assert(step(&f, 0) == 0);
    return 0;
}
