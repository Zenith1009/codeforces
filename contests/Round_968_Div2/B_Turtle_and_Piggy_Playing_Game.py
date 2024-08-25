import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()))
    print(a[n // 2])


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     a.sort()
#     ans = a[n // 2]
    
#     print(ans)
