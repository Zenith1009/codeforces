import sys

def read():
    return int(sys.stdin.readline())

def main():
    for _ in range(read()):
        read()
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        
        print("Bob" if a == b or a[::-1] == b else "Alice")

if __name__ == "__main__":
    main()
