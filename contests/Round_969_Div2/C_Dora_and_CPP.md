# C. Dora and C++

**time limit per test:** 2 seconds  
**memory limit per test:** 256 megabytes

Dora has just learned the programming language C++!

However, she has completely misunderstood the meaning of C++. She considers it as two kinds of adding operations on the array *c* with *n* elements. Dora has two integers *a* and *b*. In one operation, she can choose one of the following things to do:

- Choose an integer *i* such that \( 1 \leq i \leq n \), and increase \( c_i \) by *a*.
- Choose an integer *i* such that \( 1 \leq i \leq n \), and increase \( c_i \) by *b*.

Note that *a* and *b* are constants, and they can be the same.

Let's define a *range* of array *d* as \( \text{max}(d_i) - \text{min}(d_i) \). For instance, the range of the array \([1, 2, 3, 4]\) is \( 4 - 1 = 3 \), the range of the array \([5, 2, 8, 2, 2, 1]\) is \( 8 - 1 = 7 \), and the range of the array \([3, 3, 3]\) is \( 3 - 3 = 0 \).

After any number of operations (possibly 0), Dora calculates the range of the new array. You need to help Dora minimize this value, but since Dora loves exploring all by herself, you only need to tell her the minimized value.

## Input

Each test consists of multiple test cases. The first line contains a single integer *t* (1 ≤ *t* ≤ \( 10^4 \)) — the number of test cases. The description of test cases follows.

The first line of each test case contains three integers *n*, *a*, and *b* (1 ≤ *n* ≤ \( 10^5 \), 1 ≤ *a*, *b* ≤ \( 10^9 \)) — the length of the array *c* and the constant values, respectively.

The second line of each test case contains *n* integers \( c_1, c_2, \dots, c_n \) (1 ≤ \( c_i \) ≤ \( 10^9 \)) — the initial elements of the array *c*.

It is guaranteed that the sum of *n* over all test cases does not exceed \( 10^5 \).

## Output

For each test case, output a single integer — the minimum possible range of the array after any number of operations.
