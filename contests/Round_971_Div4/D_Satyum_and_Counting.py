def sq_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    count = 0
    distances = {}
    for i in range(n):
        for j in range(i + 1, n):
            dist = sq_dist(points[i], points[j])
            distances.setdefault(dist, []).append((i, j))
    
    for dist, pairs in distances.items():
        m = len(pairs)
        count += m * (m - 1) // 2
    
    return count

t = int(input())
for _ in range(t):
    print(solve())
