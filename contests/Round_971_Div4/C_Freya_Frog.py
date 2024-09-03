def min_moves(x, y, k):
    moves = 0
    current_x = 0
    current_y = 0
    
    while current_x < x or current_y < y:
        # X-direction move
        if current_x < x:
            distance = min(k, x - current_x)
            current_x += distance
            moves += 1
        
        # Check if we've reached the destination
        if current_x >= x and current_y >= y:
            break
        
        # Y-direction move
        if current_y < y:
            distance = min(k, y - current_y)
            current_y += distance
            moves += 1
    
    return moves

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read x, y, and k for each test case
    x, y, k = map(int, input().split())
    
    # Calculate and print the minimum number of moves
    print(min_moves(x, y, k))
