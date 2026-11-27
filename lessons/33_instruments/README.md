# Mission 33: Automate a mock RF measurement

An instrument occasionally times out or sends malformed text. Your test log must distinguish measurement failure from a passing radio.

**Track:** RF test automation. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A spectrum analyzer displays frequency-domain power; a signal generator supplies controlled stimulus; a VNA measures scattering parameters such as reflection/transmission; an oscilloscope displays voltage versus time. SCPI is a common command language, with model-specific syntax. PyVISA connects Python to supported instrument backends.

Automated tests should record units, settings, timestamp, device/firmware identity, calibration state and pass/fail limits. Use bounded timeouts and retries. Communication failure is not a passing measurement. This lab has no physical instrument or transmission: the mock’s query method supplies all responses.

## Trace a small example

```text
query("MEAS:POW?") → "-32.0" dBm
limits [-33,-31] inclusive → pass
Timeout or NaN response → retry, then explicit failure
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `measure(instrument,attempts,low,high)`. Query exactly MEAS:POW?; parse a finite float. Retry TimeoutError and malformed/nonfinite responses at most attempts times. On a valid reading return {"power_dbm": value, "pass": low<=value<=high, "attempts": used}. A valid out-of-limit measurement is a completed failing test, not a retry. Exhaustion raises RuntimeError; invalid attempts (<1 or not int), nonfinite limits, or low>high raise ValueError before querying. Other exceptions propagate. Implement save_csv(path,rows) with header power_dbm,pass,attempts and one row per result. The mock must have a bounded timeout contract; this wrapper cannot interrupt a query that hangs internally.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 33
./learn check 33
./learn quiz 33
./learn explain 33
./learn submit 33
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 33` reveals one hint at a time. `./learn solution 33` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain the four instrument types, SCPI, bounded retries, calibration, communication failure versus RF failure, and what metadata a real lab log still needs.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [PyVISA documentation](https://pyvisa.readthedocs.io/)
- [PySDR](https://pysdr.org/)
