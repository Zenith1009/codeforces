import sys

def solve():
    n = int(sys.stdin.readline())
    a = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    s = sys.stdin.readline().strip()
    ans = 0
    l, r = 0, n - 1
    while r > l:
        l += s[l] == 'R'
        r -= s[r] == 'L'
        if l < r:
            ans += a[r + 1] - a[l]
            l += 1
            r -= 1
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()