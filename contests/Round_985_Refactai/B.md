## B. Replacement

time limit per test: 1 second  
memory limit per test: 256 megabytes

You have a binary string* $s$ of length $n$, and Iris gives you another binary string $r$ of length $n-1$.

Iris is going to play a game with you. During the game, you will perform $n-1$ operations on $s$. In the $i$-th operation $(1 \leq i \leq n-1)$:

- First, you choose an index $k$ such that $1 \leq k \leq |s| - 1$ and $s_k \neq s_{k+1}$. If it is impossible to choose such an index, you lose;
- Then, you replace $s_ks_{k+1}$ with $r_i$. Note that this decreases the length of $s$ by 1.

If all the $n-1$ operations are performed successfully, you win.

Determine whether it is possible for you to win this game.

*A binary string is a string where each character is either 0 or 1.

### Input
Each test contains multiple test cases. The first line of the input contains a single integer $t$ $(1 \leq t \leq 10^4)$ — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer $n$ $(2 \leq n \leq 10^5)$ — the length of $s$.

The second line contains the binary string $s$ of length $n$ $(s_i = 0 \text{ or } 1)$.

The third line contains the binary string $r$ of length $n-1$ $(r_i = 0 \text{ or } 1)$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.

### Output
For each test case, print "YES" (without quotes) if you can win the game, and "NO" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yES", "yeS", "Yes", and "YES" will be recognized as positive responses.

Sure, I've carefully translated the information in the image to markdown code. Here it is:

## Example

### Input
```
6
2
11
0
2
01
1
4
1101
001
6
111110
10000
6
010010
11010
8
10010010
0010010
```

### Output
```
NO
YES
YES
NO
YES
NO
```

### Note
In the first test case, you cannot perform the first operation. Thus, you lose the game.

In the second test case, you can choose \( k = 1 \) in the only operation, and after that, \( s \) becomes equal to 1. Thus, you win the game.

In the third test case, you can perform the following operations: \( 1101 \rightarrow 101 \rightarrow 10 \rightarrow 1 \).
