import sys
input = sys.stdin.readline

# Precompute all perfect squares from 0 to 99
squares = {i*i: i for i in range(100)}

T = int(input())
for _ in range(T):
    y = int(input())
    if y in squares:
        print(0, squares[y])
    else:
        print(-1)

# Simplified version of the solution:

'''
import math

def main():
    T = int(input())  # 1 ≤ T ≤ 1e4
    
    for _ in range(T):
        ystr = input().strip()  # exactly 4 chars, may have leading zeros
        y = int(ystr)          # numeric value 0..9999
        
        s = int(math.sqrt(y) + 0.5)  # nearest integer root
        if s * s != y or s > 99:     # must be perfect square
            print(-1)
        else:
            print(0, s)  # (0 + s)^2 = y

if __name__ == "__main__":
    main()
'''