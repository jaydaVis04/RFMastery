# How to use practice to build understanding

The course is built around effortful recall, implementation and checking. It cannot guarantee expertise or identify an individually optimal schedule. Use performance on unfamiliar variations and your ability to explain failure modes as evidence of progress.

## What the research supports

Practice testing and distributing study over time received high utility ratings in Dunlosky and colleagues’ review across learning conditions. That supports a course with recall questions and later revisits, rather than relying on rereading. Their evaluation also gives self-explanation a more qualified, moderate assessment. [Dunlosky et al. (2013), review and publication](https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html)

Karpicke and Roediger’s experiments found that repeated retrieval improved delayed retention of studied word lists. That is evidence for retrieval as a learning activity; transferring the idea to engineering requires actual code, reasoning and application alongside factual recall. It does not establish a particular C course or flag mechanic as effective. [Karpicke & Roediger (2007), original paper](https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JML.pdf)

Chi and colleagues examined how students explained worked mechanics examples and connected those explanations with their problem-solving behavior. This motivates asking you to explain why a line or design decision works. It is not proof that speaking for a certain number of minutes guarantees programming skill. [Chi et al. (1989), original study](https://doi.org/10.1207/s15516709cog1302_1)

## How that becomes this course

| Design choice | What you actually do | Evidence boundary |
|---|---|---|
| Retrieve | Predict an example and answer before opening notes | Supported principle; a multiple-choice score alone is limited evidence |
| Implement | Write working C/HDL/Python against a contract | Engineering practice choice, assessed by behavioral tests |
| Get feedback | Use first failing assertion/diagnostic to revise | Tests expose selected mistakes; they do not prove correctness |
| Explain | Mechanism + example + boundary + limitation | Based on self-explanation work; technical accuracy needs review |
| Space | Revisit cards and rebuild later | Spacing is supported; exact intervals are practical defaults |
| Transfer | Change assumptions and test a new case | A course-design choice aimed at avoiding one-example memorization |
| Mix topics | Final quiz combines C, hardware and RF | A way to practice choosing among concepts, not a personalized adaptive tutor |
| Earn flags | Celebrate completion of concrete work | A motivational story mechanic, not a research-backed mastery metric |

The review queue uses 1, 3, 7, 14 and 30 days after correct responses; missed/partial answers return after ten minutes. Those are transparent heuristics. To change them, edit `INTERVALS` and the missed-card delay in course/engine.py. Shorter/longer intervals may fit your interview date and performance. There is no time lock on lessons or flags.

## A 60–90 minute session

1. Spend 5–10 minutes on `./learn review`. Recall an answer before revealing the model. Grade yourself honestly.
2. Read one small section and trace its worked example for 10–15 minutes.
3. Implement for 30–45 minutes, using compiler/test feedback. Try one hypothesis at a time.
4. Close notes. Explain for two minutes, save a concise record, then answer the quiz.
5. Write the next smallest action before you stop. On another day, rebuild one difficult part from a blank scratch file.

If you are stuck after a serious attempt, use the first hint. If that is insufficient, study a reference, close it, and reconstruct a smaller example. Record assisted practice without treating it as failure. Reading a solution is exposure; later reconstruction is evidence you can retrieve the method.

## Avoid familiar-looking answers as a mastery test

Ask yourself: can I implement a variation, explain why an edge case matters, diagnose a failure, and state a limitation? In a quiz the correct option may look familiar. In `review`, type the answer before comparing. In coding, add a test not provided by the course. In the interview, reason from requirements rather than reciting vocabulary.

The course never automatically declares that your explanation is conceptually correct. Request a human or assistant review of code and notes for misconceptions, especially around atomics, CDC, physical RF units and timing analysis.
