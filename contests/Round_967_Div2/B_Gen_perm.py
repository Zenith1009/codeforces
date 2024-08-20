def solve():
    n = int(input())

    if n % 2 == 0:
        print(-1)
    else:
        for i in range(n, 0, -2):
            print(i, end=" ")
        for i in range(2, n, 2):
            print(i, end=" ")
        print()

t = int(input())
for _ in range(t):
    solve()
