def solve():
    n = int(input())
    s = input()
    root = int(n**0.5)
    
    if root * root != n:
        print("NO")
        return
    
    ones = sum(1 for c in s if c == '1')
    zeros = n - ones
    
    if ones == 4 * (root - 1) and zeros == (root - 2) * (root - 2):
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()
