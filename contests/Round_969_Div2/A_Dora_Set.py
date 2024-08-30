def coprimes():
    l, r = map(int, input().split())
    if l % 2 == 0:
        l += 1
    print((r - l + 2) // 4)

t = int(input())
for _ in range(t):
    coprimes()