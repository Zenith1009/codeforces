
# A. Make All Equal

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

You are given a cyclic array $a_1, a_2, \ldots, a_n$.

You can perform the following operation on $a$ at most $n-1$ times:

* Let $m$ be the current size of $a$, you can choose any two adjacent elements where the previous one is no greater than the latter one (In particular, $a_m$ and $a_1$ are adjacent and $a_m$ is the previous one), and delete exactly one of them. In other words, choose an integer $i$ $(1 \leq i \leq m)$ where $a_i \leq a_{(i \mod m) + 1}$ holds, and delete exactly one of $a_i$ or $a_{(i \mod m) + 1}$ from $a$.

Your goal is to find the minimum number of operations needed to make all elements in $a$ equal.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $t$ $(1 \leq t \leq 500)$. The description of the test cases follows.

The first line of each test case contains a single integer $n$ $(1 \leq n \leq 100)$— the length of the array $a$.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ $(1 \leq a_i \leq n)$ — the elements of array $a$.

## Output
For each test case, output a single line containing an integer: the minimum number of operations needed to make all elements in $a$ equal.
