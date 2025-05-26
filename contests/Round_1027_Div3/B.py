import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    count0 = s.count('0')
    count1 = n - count0
    
    bad_pairs = n // 2 - k
    
    if count0 < bad_pairs or count1 < bad_pairs:
        print("NO")
        continue
    
    remaining0 = count0 - bad_pairs
    remaining1 = count1 - bad_pairs
    
    if remaining0 // 2 + remaining1 // 2 >= k:
        print("YES")
    else:
        print("NO")

# Simplified version of the solution:
'''
def solve():
    n, k = map(int, input().split())
    s = input().strip()
    
    # Count zeros and ones
    count0 = s.count('0')
    count1 = n - count0
    
    num_total_pairs = n // 2
    num_bad_pairs_needed = num_total_pairs - k
    
    # Check if we have enough characters for bad pairs
    if count0 < num_bad_pairs_needed or count1 < num_bad_pairs_needed:
        print("NO")
        return
    
    # Calculate remaining characters for good pairs
    remaining_zeros_for_good = count0 - num_bad_pairs_needed
    remaining_ones_for_good = count1 - num_bad_pairs_needed
    
    # Calculate maximum good pairs we can form
    possible_good_pairs_from_zeros = remaining_zeros_for_good // 2
    possible_good_pairs_from_ones = remaining_ones_for_good // 2
    
    total_max_good_pairs_can_form = possible_good_pairs_from_zeros + possible_good_pairs_from_ones
    
    if total_max_good_pairs_can_form >= k:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
'''