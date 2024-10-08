# B. Generate Permutation

**time limit per test:** 1.5 seconds  
**memory limit per test:** 256 megabytes

There is an integer sequence $a$ of length $n$, where each element is initially $-1$.

Misuki has two typewriters where the first one writes letters from left to right, with a pointer initially pointing to 1, and another writes letters from right to left with a pointer initially pointing to $n$.

Misuki would choose one of the typewriters and use it to perform the following operations until $a$ becomes a permutation of $[1, 2, \ldots, n]$:

* **write number**: write the minimum positive integer that hasn't appeared in $a$ to $a_i$, $i$ is the position where the pointer points at. Such operation can be performed only when $a_i = -1$.
* **carriage return**: return the pointer to its initial position (i.e. 1 for the first typewriter, $n$ for the second)
* **move pointer**: move the pointer to the next position, let $i$ be the position the pointer points at before this operation, if Misuki is using the first typewriter, $i := i + 1$ would happen, and $i := i - 1$ otherwise. Such operation can be performed only if after the operation, $1 \leq i \leq n$ holds.

Your task is to construct any permutation $p$ of length $n$, such that the minimum number of carriage return operations needed to make $a = p$ is the same no matter which typewriter Misuki is using.

## Input
Each test contains multiple test cases. The first line of input contains a single integer $t$ $(1 \leq t \leq 500)$ — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer $n$ $(1 \leq n \leq 2 \cdot 10^5)$ — the length of the permutation.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

## Output
For each test case, output a line of $n$ integers, representing the permutation $p$ of length $n$ such that the minimum number of carriage return operations needed to make $a = p$ is the same no matter which typewriter Misuki is using, or $-1$ if it is impossible to do so.

If there are multiple valid permutations, you can output any of them.

## Example

**Input**
```
3
1
2
3
```

**Output**
```
1
-1
3 1 2
```

## Note

In the first testcase, it's possible to make $a = p = [1]$ using 0 carriage return operations.

In the second testcase, it is possible to make $a = p = [1, 2]$ with the minimal number of carriage returns as follows:

If Misuki is using the first typewriter:
- **Write number:** write 1 to $a_1$, $a$ becomes $[1, -1]$
- **Move pointer:** move the pointer to the next position. (i.e. 2)
- **Write number:** write 2 to $a_2$, $a$ becomes $[1, 2]$

If Misuki is using the second typewriter:
- **Move pointer:** move the pointer to the next position. (i.e. 1)
- **Write number:** write 1 to $a_1$, $a$ becomes $[1, -1]$
- **Carriage return:** return the pointer to 2.
- **Write number:** write 2 to $a_2$, $a$ becomes $[1, 2]$

It can be proven that the minimum number of carriage returns needed to transform $a$ into $p$ when using the first typewriter is 0 and it is 1 when using the second one, so this permutation is not valid.

Similarly, $p = [2, 1]$ is also not valid, so there is no solution for $n = 2$.

In the third testcase, it is possible to make $a = p = [3, 1, 2]$ with 1 carriage return with both the first and the second typewriter. It can be proven that, for both typewriters, it is impossible to write $p$ with 0 carriage returns.

With the first typewriter it is possible to:
