# A. Doremy's Paint 3

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

An array \( b_1, b_2, \dots, b_n \) of positive integers is good if all the sums of two adjacent elements are equal to the same value. More formally, the array is good if there exists a \( k \) such that \( b_1 + b_2 = b_2 + b_3 = \dots = b_{n-1} + b_n = k \).

Doremy has an array *a* of length *n*. Now Doremy can permute its elements (change their order) however she wants. Determine if she can make the array good.

## Input

The input consists of multiple test cases. The first line contains a single integer *t* (1 ≤ *t* ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer *n* (2 ≤ *n* ≤ 100) — the length of the array *a*.

The second line of each test case contains *n* integers \( a_1, a_2, \dots, a_n \) (1 ≤ \( a_i \) ≤ \( 10^5 \)).

There are no constraints on the sum of *n* over all test cases.

## Output

For each test case, print "Yes" (without quotes), if it is possible to make the array good, and "No" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "YEs", and "YeS" will be recognized as positive responses.

## Example

**input**  
5  
2  
8 9  
3  
1 2 1  
4  
1 1 4 5  
4  
2 3 3 3  
4  
100000 100000 100000 100000

**output**  
Yes  
Yes  
No  
Yes  
Yes

## Note

In the first test case, \([8, 9]\) and \([9, 8]\) are good.

In the second test case, \([1, 2, 1]\) is good because \(a_1 + a_2 = a_2 + a_3 = 3\).

In the third test case, it can be shown that no permutation is good.
