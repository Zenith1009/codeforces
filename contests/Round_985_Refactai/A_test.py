def solve(l, r, k):
    S = set(range(l, r + 1))
    
    def count_multiples(x, S):

        count = 0
        curr_mult = x
        while curr_mult <= r:
            if curr_mult in S:
                count += 1
            curr_mult += x
        return count
    
    operations = 0
    while True:
        found = False

        for x in sorted(S):
            if count_multiples(x, S) >= k:
                S.remove(x)
                operations += 1
                found = True
                break
        if not found:
            break
    
    return operations
t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    print(solve(l, r, k))
