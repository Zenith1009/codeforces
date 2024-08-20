def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = [0] * (n + 1)
    for num in a:
        count[num] += 1
    
    max_count = max(count)
    operations = n - max_count
    
    print(f"{operations}\n")

t = int(input())
for _ in range(t):
    solve()
