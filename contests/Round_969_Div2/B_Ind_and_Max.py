def max_of_ops():
    n, no_ops = map(int, input().split())
    
    array = list(map(int, input().split()))
    max_val = max(array)
    results = []
    for _ in range(no_ops):
        op, l, r = input().split()
        l = int(l)
        r = int(r)
        
        if l <= max_val <= r:
            if op == '-':
                max_val -= 1
            else:
                max_val += 1
        
        results.append(str(max_val))
    
    print(' '.join(results))
    # print()

test_cases = int(input())

for _ in range(test_cases):
    max_of_ops()
