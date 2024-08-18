import sys

def calc_sq_dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def main():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        n = int(input())  # Number of circles
        
        circles = []
        for _ in range(n):
            xi, yi = map(int, input().split())
            circles.append((xi, yi))
        
        xs, ys, xt, yt = map(int, input().split())  # Start and target coordinates
        comp = calc_sq_dist(xs, ys, xt, yt)  # Squared distance between start and target
        possible = True

        for xi, yi in circles:
            st_dist = calc_sq_dist(xs, ys, xi, yi)  # Squared distance from start to circle
            end_dist = calc_sq_dist(xt, yt, xi, yi)  # Squared distance from target to circle
            
            if end_dist <= comp:
                possible = False
                break

        print("YES" if possible else "NO")

if __name__ == "__main__":
    main()