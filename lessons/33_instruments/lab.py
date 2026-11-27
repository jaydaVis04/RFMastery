def measure(instrument, attempts, low, high):
    raise NotImplementedError("Implement validation, bounded retries and results")

def save_csv(path, rows):
    raise NotImplementedError("Write explicit units and pass/fail fields")
