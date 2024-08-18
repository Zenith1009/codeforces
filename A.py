def solve():
    t = int(input("Enter the number of test cases: "))
    for i in range(t):
        xc, yc, k = map(int, input("Enter xc yc k: ").split())
        points = []
        for j in range(k):
            xi = xc + j
            yi = yc - j
            points.append((xi, yi))
        
        for point in points:
            print(point[0], point[1])

solve()
