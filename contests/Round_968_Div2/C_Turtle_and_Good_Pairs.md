# C. Turtle and Good Pairs

**time limit per test:** 2 seconds  
**memory limit per test:** 256 megabytes

Turtle gives you a string *s*, consisting of lowercase Latin letters.

Turtle considers a pair of integers *(i, j)* (1 ≤ *i* < *j* ≤ *n*) to be a pleasant pair if and only if there exists an integer *k* such that *i* ≤ *k* < *j* and both of the following two conditions hold:

- *sᵢ* ≠ *sₖ*₊₁.
- *sₖ* ≠ *sₖ₊₁* or *sₖ₊₁* ≠ *sⱼ*.

Besides, Turtle considers a pair of integers *(i, j)* (1 ≤ *i* < *j* ≤ *n*) to be a good pair if and only if *sᵢ* = *sⱼ* or *(i, j)* is a pleasant pair.

Turtle wants to reorder the string *s* so that the number of good pairs is maximized. Please help him!

## Input

Each test contains multiple test cases. The first line contains the number of test cases *t* (1 ≤ *t* ≤ 10⁴). The description of the test cases follows.

The first line of each test case contains a single integer *n* (2 ≤ *n* ≤ 2 ⋅ 10⁵) — the length of the string.

The second line of each test case contains a string *s* of length *n*, consisting of lowercase Latin letters.

It is guaranteed that the sum of *n* over all test cases does not exceed 2 ⋅ 10⁵.

## Output

For each test case, output the string *s* after reordering so that the number of good pairs is maximized. If there are multiple answers, print any of them.

## Example

**input**  
```
5  
3  
abc  
5  
edddf  
6  
turtle  
8  
PPPPPPPP  
10  
codeforces
```

**output**  
```
acb  
dddef  
urtlet  
PPPPPPPP  
codeforces
```