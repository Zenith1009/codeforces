def solve():
    s = input().strip()
    if len(s) >= 3:
        if s[0] == '1' and s[1] == '0' and (s[2] >= '2' or (len(s) >= 4 and s[2] >= '1')):
            print("YES")
            return
    print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
