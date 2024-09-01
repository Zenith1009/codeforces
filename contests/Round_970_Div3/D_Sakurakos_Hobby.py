def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    string = input()
    
    result = [0] * n
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            cycle = []
            current = i
            
    
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = numbers[current] - 1
            
    
            zero_count = sum(1 for index in cycle if string[index] == '0')
            
    
            for index in cycle:
                result[index] = zero_count
    
    print(*result)

def main():
    t = int(input())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
