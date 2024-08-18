def solve(n, p):
    # Calculate prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + p[i]
    
    # Create a list of (element, prefix sum) pairs
    elements_with_sum = [(p[i], prefix_sum[i + 1]) for i in range(n)]
    
    # Sort based on prefix sums
    elements_with_sum.sort(key=lambda x: x[1])
    
    # Assign q in reverse order
    q = [0] * n
    for i in range(n):
        q[elements_with_sum[i][0] - 1] = n - i
    
    return q

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    # Solve and output
    result = solve(n, p)
    print(*result)