One can notice the following remarkable mathematical fact: the number **2025** can be represented as \((20 + 25)^2\).

You are given a year represented by a string **s**, consisting of exactly **4** characters. Thus, leading zeros are allowed in the year representation. For example, `"0001"`, `"0185"`, `"1375"` are valid year representations.

You need to express it in the form \((a + b)^2\), where **a** and **b** are non-negative integers, or determine that it is impossible.

For example, if **s = "0001"**, you can choose **\(a = 0\)**, **\(b = 1\)**, and write the year as: **\((0 + 1)^2 = 1\)**

### Input

- The first line of the input contains a single integer **\(t\) \((1 \leq t \leq 10^4)\)** — the number of test cases.
- The following lines describe the test cases.
- The only line of each test case contains a string **s**, consisting of exactly **4** characters. Each character is a digit from **0** to **9**.

### Output

For each test case, output on a separate line:

- Two numbers **a** and **b** (**\(a, b \geq 0\)**) such that \((a + b)^2 = s\), if they exist.
- If there are multiple suitable pairs, you may output any of them.
- Output **-1** if no valid pair exists.

### Example
input:
```
5
0001
1001
1000
4900
2025
```
output:
```
0 1
-1
-1
34 36
20 25
```
