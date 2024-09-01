import math

def main():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        diff = r - l
        k = 1
        while (k * (k + 1)) // 2 <= diff:
            k += 1
        print(k)

if __name__ == "__main__":
    main()
