# Mission 04: Separate the gain controller

Another engineer needs your gain function through a stable header.

**Track:** C foundations. **Suggested effort:** 2–4 sessions; capstones need longer. Work at your pace.

## Understand

C passes every argument by value, including pointers. An output pointer lets a function modify a caller-owned object. Headers declare interfaces; .c files define functions. Include guards prevent duplicate declarations. File-scope `static` gives internal linkage. `extern` normally declares a symbol defined elsewhere.

Design errors as part of the API. Here, invalid bounds or a NULL output are errors. An error must not modify the caller’s old output value. The grader compiles your implementation and test harness as separate translation units before linking.

## Trace a small example

```c
int set_answer(int *out) {
    if (out == NULL) return -1;
    *out = 42;
    return 0;
}
```

Before running anything, predict the result and explain why. Then check your prediction.

## Build it

Implement `clamp_checked(x,lo,hi,out)`. Return 0 and write the bounded value on success. Return -1 for lo>hi or out==NULL; preserve *out on error. Keep the prototype in lab.h and the definition in lab.c.

The source contract in this folder is authoritative. Edit the learner source files; keep the tests as your diagnostic instruments. Read their assertions when a failure is unclear. They are visible on purpose. The grader changes inputs and checks behavior; printing a flag will not pass it.

## Work from the repository root

```sh
./learn lesson 4
./learn check 4
./learn quiz 4
./learn explain 4
./learn submit 4
```

`check` does not require passing earlier missions. A flag requires passing code checks (or the design rubric), every quiz question, and a saved explanation. `submit` reruns checks before awarding it. No waiting period prevents learning.

Stuck? `./learn hint 4` reveals one hint at a time. `./learn solution 4` reveals a reference and records assisted practice; rebuild it later without looking. Your work is never overwritten.

## Explain without notes

Describe pass-by-value, output parameters, declaration versus definition, and the error contract of your API.

## Transfer challenge

Change one assumption: input size, sign, units, timing, or ownership. Predict which test or design decision must change. Add a test of your own, then explain one remaining limitation. These extensions are self-assessed and do not award automatic credit.

## Read more

- [Beej’s Guide to C](https://beej.us/guide/bgc/html/split/)
