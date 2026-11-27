import math
def payload_bps(rate, channels, bytes_per_sample=4):
    if not all(math.isfinite(x) and x > 0 for x in (rate, channels, bytes_per_sample)):
        raise ValueError("positive finite arguments required")
    return rate * channels * bytes_per_sample
def block_ms(count, rate):
    if not math.isfinite(rate) or rate <= 0 or not math.isfinite(count) or count < 0:
        raise ValueError("invalid count/rate")
    return 1000 * count / rate
def missing_blocks(seqs):
    total, prev = 0, None
    for n in seqs:
        if not isinstance(n, int) or n < 0 or (prev is not None and n <= prev):
            raise ValueError("sequence must increase")
        if prev is not None:
            total += n - prev - 1
        prev = n
    return total
