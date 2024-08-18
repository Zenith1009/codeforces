def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # This line creates a boolean array 'v' of size n+2, initialized with False values
    # It is likely used to mark or track certain elements, where n is probably the 
    # number of elements in the main array 'a'. The extra 2 slots (n+2) might be 
    # used as sentinels or to handle edge cases without additional boundary checks.
    v = [False] * (n + 2)

    can_sit = True
    for i in range(n):
        v[a[i]] = True
        if i > 0 and not v[a[i] - 1] and not v[a[i] + 1]:
            can_sit = False

    print("YES" if can_sit else "NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
