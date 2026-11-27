# Mission 05: Repair the reversed capture

A capture buffer arrived in reverse order. Repair it in place without allocating.

**Track:** C memory. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

A pointer designates an object or function. `&` obtains an address; `*` dereferences a valid pointer. Pointer arithmetic is scaled by the pointed-to type and is defined only within one array or one past it. One-past may be formed but never dereferenced. NULL does not designate an object.

An array often converts to a pointer to its first element. In a function parameter, `int a[4]` is adjusted to `int *a`; sizeof there measures the pointer. Pass the element count separately. Array storage and the pointer variable are different objects.

## Trace a small example

```c
int a[4] = {10,20,30,40};
int *p = a;
/* *(p+2) == 30; sizeof a / sizeof a[0] == 4 */
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `reverse(a,n)` without heap allocation. NULL is allowed for n==0 only. Handle odd/even lengths and avoid forming n-1 when n==0. Draw each swap for a five-element buffer.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 5
./learn check 5
./learn quiz 5
./learn explain 5
./learn submit 5
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 5` reveals one hint at a time. `./learn solution 5` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Explain the difference between an array, a pointer, and a one-past pointer. Why can a function not infer n from sizeof its array parameter?

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
