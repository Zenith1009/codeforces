def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for _ in range(int(input())):
        q = input().strip()
        if len(q) != n:
            print("NO")
            continue
        p = {}
        c = {}
        matching = True
        for i, char in enumerate(q, 1):
            if char not in c:
                if a[i] in p:
                    matching = False
                    break
                p[a[i]] = True
                c[char] = a[i]
            elif c[char] != a[i]:
                matching = False
                break

        print("YES" if matching else "NO")

for _ in range(int(input())):
    solve()
