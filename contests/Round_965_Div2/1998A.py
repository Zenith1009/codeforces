# def solve():
#     t = int(input("Enter the number of test cases: "))
#     for i in range(t):
#         xc, yc, k = map(int, input("Enter xc yc k: ").split())
#         points = []
#         for j in range(k):
#             xi = xc + j
#             yi = yc - j
#             points.append((xi, yi))
        
#         for point in points:
#             print(point[0], point[1])

# solve()


def solve():
    x, y, k = map(int, input().split())
    for i in range(k // 2):
        print(x - i - 1, y)
        print(x + i + 1, y)
    if k % 2 != 0:
        print(x, y)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
