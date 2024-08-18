# I didn't quite get the question, so I recreated the solution in python, it works but still need explainaion.


import sys

# Function to calculate squared distance between two points
def calc_sq_dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def main():
    # Read number of test cases
    for _ in range(int(sys.stdin.readline())):
        # Read number of circles
        n = int(sys.stdin.readline())
        # Read coordinates of circles
        circles = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
        # Read start and end coordinates
        xs, ys, xt, yt = map(int, sys.stdin.readline().split())
        # Calculate squared distance between start and end points
        comp = calc_sq_dist(xs, ys, xt, yt)
        
        # Check if it's possible to reach the end point without touching any circle
        possible = all(calc_sq_dist(xt, yt, xi, yi) > comp for xi, yi in circles)
        print("YES" if possible else "NO")

if __name__ == "__main__":
    main()