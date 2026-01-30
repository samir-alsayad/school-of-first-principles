# Experiment: The Sealed Letter (Immutability)

**One New Idea:** Some states can be changed (Mutable), some cannot (Immutable).

## Prerequisites
*   None.

## Hypotheses / Question
We claim "Tuples are sealed envelopes".
**Hypothesis:** If we try to write into a Tuple, the computer should stop us with an error.

## Prediction
**STOP.**
1.  We have a list `my_list = [1, 2]`. We try `my_list[0] = 99`. What happens?
2.  We have a tuple `my_tuple = (1, 2)`. We try `my_tuple[0] = 99`. What happens?

## The Experiment
We will try to break the Tuple.

## Verification
### Actual Output
/Users/Shared/school-of-first-principles 
❯ /Users/samir/.pyenv/versions/3.12.3/bin/python /Users/Shared/school-of-first-principles/state/immutability/01_tuple_vs_list/main.py
--- PART 1: The List (Binder) ---
Before: [1, 2]
After:  [99, 2]
Success! Lists are mutable.

--- PART 2: The Tuple (Sealed Envelope) ---
Before: (1, 2)
Traceback (most recent call last):
  File "/Users/Shared/school-of-first-principles/state/immutability/01_tuple_vs_list/main.py", line 14, in <module>
    my_tuple[0] = 99
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

### My Learnings


The crash happened, because tuples are designed to be immutable lists by default, so that when one tries to change something in them after they have been initialized, the machine doesnt allow it.
