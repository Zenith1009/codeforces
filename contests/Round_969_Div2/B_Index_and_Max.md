# B. Index and Maximum Value

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

After receiving yet another integer array \( a_1, a_2, \dots, a_n \) at her birthday party, Index decides to perform some operations on it.

Formally, there are *m* operations that she is going to perform in order. Each of them belongs to one of the two types:

- `+ l r`. Given two integers *l* and *r*, for all \( 1 \leq i \leq n \) such that \( l \leq a_i \leq r \), set \( a_i := a_i + 1 \).
- `- l r`. Given two integers *l* and *r*, for all \( 1 \leq i \leq n \) such that \( l \leq a_i \leq r \), set \( a_i := a_i - 1 \).

For example, if the initial array \( a = [7, 1, 3, 4, 3] \), after performing the operation `+ 2 4`, the array becomes \( a = [7, 1, 4, 5, 4] \). Then, after performing the operation `- 1 10`, the array becomes \( a = [6, 0, 3, 4, 3] \).

Index is curious about the maximum value in the array *a*. Please help her find it after each of the *m* operations.

## Input

Each test consists of multiple test cases. The first line contains a single integer *t* (1 ≤ *t* ≤ \( 2 \cdot 10^4 \)) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers *n* and *m* (1 ≤ *n* ≤ \( 10^5 \), 1 ≤ *m* ≤ \( 10^5 \)) — the length of the array and the number of operations.

The second line of each test case contains *n* integers \( a_1, a_2, \dots, a_n \) (1 ≤ \( a_i \) ≤ \( 10^9 \)) — the initial array *a*.

Then *m* lines follow, each line corresponds to an operation, in the following format: `c l r` (c ∈ {`+`, `-`}), *l* and *r* are integers, \( 1 \leq l \leq r \leq 10^9 \) — the description of the operation.

Note that the elements \( a_i \) may not satisfy \( 1 \leq a_i \leq 10^9 \) after some operations, as it is shown in the example.

It is guaranteed that the sum of *n* over all test cases does not exceed \( 10^5 \), and the sum of *m* over all test cases does not exceed \( 10^5 \).

## Output

For each test case, output one single line containing *m* integers, with the *i*-th of them describing the maximum value of the array after the *i*-th operation.

## Example

**Input**  
```
5
5 5
1 2 3 2 1
+ 1 3
- 2 3
+ 1 2
+ 2 4
- 6 8
5 5
1 3 3 4 5
+ 1 4
+ 2 3
- 4 5
- 3 3
- 2 6
5 5
1 1 1 1 1
+ 2 3
- 4 5
+ 1 6
- 2 5
+ 1 8
1 1
1
- 1 1
1 1
1000000000
+ 1000000000 1000000000
```

**Output**  
```
4 4 4 5 5
5 5 4 4 3
1 1 2 1 2
0
1000000001
```
