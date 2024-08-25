# B. Turtle and Piggy Are Playing a Game 2

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

Turtle and Piggy are playing a game on a sequence. They are given a sequence *a₁, a₂, ..., aₙ*, and Turtle goes first. Turtle and Piggy alternate in turns (so, Turtle does the first turn, Piggy does the second, Turtle does the third, etc.).

The game goes as follows:

- Let the current length of the sequence be *m*. If *m = 1*, the game ends.
- If the game does not end and it's Turtle's turn, then Turtle must choose an integer *i* such that 1 ≤ *i* ≤ *m - 1*, set *aᵢ* to max(*aᵢ, aᵢ₊₁*), and remove *aᵢ₊₁*.
- If the game does not end and it's Piggy's turn, then Piggy must choose an integer *i* such that 1 ≤ *i* ≤ *m - 1*, set *aᵢ* to min(*aᵢ, aᵢ₊₁*), and remove *aᵢ₊₁*.

Turtle wants to maximize the value of *a₁* in the end, while Piggy wants to minimize the value of *a₁* in the end. Find the value of *a₁* in the end if both players play optimally.

You can refer to notes for further clarification.

## Input

Each test contains multiple test cases. The first line contains the number of test cases *t* (1 ≤ *t* ≤ 10⁴). The description of the test cases follows.

The first line of each test case contains a single integer *n* (2 ≤ *n* ≤ 10⁵) — the length of the sequence.

The second line of each test case contains *n* integers *a₁, a₂, ..., aₙ* (1 ≤ *aᵢ* ≤ 10⁵) — the elements of the sequence *a*.

It is guaranteed that the sum of *n* over all test cases does not exceed 10⁵.

## Output

For each test case, output a single integer — the value of *a₁* in the end if both players play optimally.

## Example

**input**  
```
5  
2  
1 2  
3  
1 2 3  
3  
3 2 3  
5  
1 2 3 2 3  
10  
2 5 2 7 9 2 5 10 7
```

**output**  
```
2  
1  
3  
2  
7
```