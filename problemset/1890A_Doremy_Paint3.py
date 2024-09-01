def solve():
    n = int(input())
    a = list(map(int, input().split()))
    unique = set(a)
    
    if len(unique) > 2:
        print("No")
    elif len(unique) == 1 or n <= 2:
        print("Yes")
    else:
        count = a.count(list(unique)[0])
        if abs(count - (n - count)) <= 1:
            print("Yes")
        else:
            print("No")

t = int(input())
for _ in range(t):
    solve()
