def solve(l, r, k):
    if r-l > 10**6 and k == 2:
        return min(r//2, r-l+1)
    
    S = set(range(l, r+1))
    ops = 0
    
    for x in range(l, r+1):
        if x not in S: continue

        count, n = 0, x
        while n <= r and count < k:
            if n in S:
                count += 1
            n += x
        if count >= k:
            S.remove(x)
            ops += 1
            
    return ops

for _ in range(int(input())):
    l,r,k = map(int,input().split())
    print(solve(l,r,k))