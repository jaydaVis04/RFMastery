import csv, math
def measure(instrument, attempts, low, high):
    if type(attempts) is not int or attempts < 1 or not math.isfinite(low) or not math.isfinite(high) or low > high:
        raise ValueError("invalid measurement contract")
    for used in range(1, attempts+1):
        try:
            value=float(instrument.query("MEAS:POW?"))
            if not math.isfinite(value):
                raise ValueError("nonfinite")
        except (TimeoutError, ValueError):
            continue
        return {"power_dbm":value,"pass":low<=value<=high,"attempts":used}
    raise RuntimeError("measurement unavailable after bounded retries")
def save_csv(path, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=['power_dbm','pass','attempts'])
        writer.writeheader()
        writer.writerows(rows)
