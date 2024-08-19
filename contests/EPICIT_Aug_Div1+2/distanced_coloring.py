def main():
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        result = min(n, k) * min(m, k)
        print(f"{result}\n")

if __name__ == "__main__":
    main()