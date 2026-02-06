# Mission: Pydantic (Strict Structs)

## The Objective
Python is loosely typed. This is bad for Engineering.
Refuse to accept bad data by using Pydantic Models.

## The Challenge
Create `strict.py` that:
1.  Imports `BaseModel` from `pydantic`.
2.  Defines a class `User(BaseModel)` with fields:
    *   `id`: int
    *   `name`: str
3.  Tries to create a User with `id="100"` (String!).
4.  Prints the user.id (It should be an Integer!).

## Requirements
*   You must install pydantic first: `pip install pydantic`.
*   Verify that Pydantic *coerces* the string "100" into the integer 100.

## Verification
Output: `User(id=100, name='Neo')`. (Note the lack of quotes around 100).
