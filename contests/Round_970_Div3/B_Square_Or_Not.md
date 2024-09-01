## B. Square or Not

**Time Limit:** 2 seconds

**Memory Limit:** 256 megabytes

**Problem Statement:**

A beautiful binary matrix is a matrix with ones on its edges and zeros inside.

Sakurako was playing with a beautiful binary matrix of size `r x c` and created a binary string `s` by writing down all the rows of the matrix, starting from the first and ending with the `r`-th. More formally, the element from the matrix in the `i`-th row and `j`-th column corresponds to the `((i-1)*c+j)`-th element of the string.

You need to check whether the beautiful matrix from which the string `s` was obtained could be **squared**. In other words, you need to check whether the string `s` could have been built from a **square** beautiful binary matrix (i.e., one where `r=c`).

**Input:**

The first line contains a single integer `t` (1 ≤ t ≤ 10^4) - the number of test cases.

The first line of each test case contains a single integer `n` (2 ≤ n ≤ 2 * 10^5) - the length of the string.

The second line of each test case contains the string `s` of length `n`. The string is always the result of writing out the strings of a beautiful matrix.

It is guaranteed that the sum of `n` across all test cases does not exceed 2 * 10^5.

**Output:**

Print "Yes", if the original matrix could have been square, and "No" otherwise.

**Examples:**

**Input:**
```
5
2
11
4
1111
9
111101111
9
111111111
12
111110011111
```

**Output:**
```
No
Yes
Yes
No
No
```

**Explanation:**

- For the second test case, string "1111" can be obtained from the matrix: