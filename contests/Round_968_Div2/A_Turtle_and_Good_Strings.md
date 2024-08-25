# A. Turtle and Good Strings

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

Turtle thinks a string *s* is a good string if there exists a sequence of strings *t₁, t₂, ..., tₖ* (*k* is an arbitrary integer) such that:

- *k* ≥ 2.
- *s = t₁ + t₂ + ... + tₖ*, where + represents the concatenation operation. For example, abc = a + bc.
- For all 1 ≤ *i* < *j* ≤ *k*, the first character of *tᵢ* isn't equal to the last character of *tⱼ*.

Turtle is given a string *s* consisting of lowercase Latin letters. Please tell him whether the string *s* is a good string!

## Input

Each test contains multiple test cases. The first line contains the number of test cases *t* (1 ≤ *t* ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer *n* (2 ≤ *n* ≤ 100) — the length of the string.

The second line of each test case contains a string *s* of length *n*, consisting of lowercase Latin letters.

## Output

For each test case, output "YES" if the string *s* is a good string, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

## Example

**input**  
```
4  
2  
aa  
3  
aba  
4  
abcb  
12  
abcabcabcabc
```

**output**  
```
No  
nO  
Yes  
YES
```