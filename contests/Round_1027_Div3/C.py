import sys
input = sys.stdin.readline

MAX_COORD = 1000000
tree = [0] * (4 * MAX_COORD + 8)
touched = []

def update(node, start, end, pos, val):
    touched.append(node)
    if start == end:
        tree[node] = max(tree[node], val)
        return
    
    mid = (start + end) >> 1
    if pos <= mid:
        update(node << 1, start, mid, pos, val)
    else:
        update((node << 1) | 1, mid + 1, end, pos, val)
    
    tree[node] = max(tree[node << 1], tree[(node << 1) | 1])

def query(node, start, end, l, r):
    if l > r:
        return 0
    if l <= start and end <= r:
        return tree[node]
    
    mid = (start + end) >> 1
    res = 0
    if l <= mid:
        res = max(res, query(node << 1, start, mid, l, r))
    if r > mid:
        res = max(res, query((node << 1) | 1, mid + 1, end, l, r))
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Clear touched nodes
    for idx in touched:
        if idx < len(tree):
            tree[idx] = 0
    touched.clear()
    
    ans = 0
    for x in a:
        dp = 1
        
        # Query [1, x-2]
        if x >= 3:
            dp = max(dp, query(1, 1, MAX_COORD, 1, x - 2) + 1)
        
        # Query [max(1, x-1), x]
        l = max(1, x - 1)
        if l <= x:
            dp = max(dp, query(1, 1, MAX_COORD, l, x))
        
        update(1, 1, MAX_COORD, x, dp)
        ans = max(ans, dp)
    
    print(ans)


'''
MAX_COORDINATE = 1000000

class SegmentTree:
    def __init__(self):
        self.tree = [0] * (4 * MAX_COORDINATE + 8)
        self.touched_nodes = []
    
    def update(self, node_idx, seg_start, seg_end, update_pos, new_dp_val):
        self.touched_nodes.append(node_idx)
        
        if seg_start == seg_end:
            self.tree[node_idx] = max(self.tree[node_idx], new_dp_val)
            return
        
        mid = seg_start + (seg_end - seg_start) // 2
        if update_pos <= mid:
            self.update(2 * node_idx, seg_start, mid, update_pos, new_dp_val)
        else:
            self.update(2 * node_idx + 1, mid + 1, seg_end, update_pos, new_dp_val)
        
        self.tree[node_idx] = max(self.tree[2 * node_idx], self.tree[2 * node_idx + 1])
    
    def query(self, node_idx, seg_start, seg_end, query_L, query_R):
        if query_L > query_R:
            return 0
        
        if query_L <= seg_start and seg_end <= query_R:
            return self.tree[node_idx]
        
        mid = seg_start + (seg_end - seg_start) // 2
        max_val_found = 0
        
        if query_L <= mid:
            max_val_found = max(max_val_found, 
                              self.query(2 * node_idx, seg_start, mid, query_L, query_R))
        if query_R > mid:
            max_val_found = max(max_val_found, 
                              self.query(2 * node_idx + 1, mid + 1, seg_end, query_L, query_R))
        
        return max_val_found
    
    def clear_touched_nodes(self):
        for idx in self.touched_nodes:
            if idx < len(self.tree):
                self.tree[idx] = 0
        self.touched_nodes.clear()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Clear previous test case data
    seg_tree.clear_touched_nodes()
    
    max_total_arrays = 0
    
    for i in range(n):
        current_a_val = a[i]
        
        dp_val_for_current_a = 1
        
        # Case 1: Query range [1, current_a_val - 2]
        max_prev_dp1 = 0
        if current_a_val - 2 >= 1:
            max_prev_dp1 = seg_tree.query(1, 1, MAX_COORDINATE, 1, current_a_val - 2)
        dp_val_for_current_a = max(dp_val_for_current_a, max_prev_dp1 + 1)
        
        # Case 2: Query range [max(1, current_a_val - 1), current_a_val]
        max_prev_dp2 = 0
        query_L_case2 = max(1, current_a_val - 1)
        query_R_case2 = current_a_val
        
        if query_L_case2 <= query_R_case2:
            max_prev_dp2 = seg_tree.query(1, 1, MAX_COORDINATE, query_L_case2, query_R_case2)
        dp_val_for_current_a = max(dp_val_for_current_a, max_prev_dp2)
        
        # Update segment tree
        seg_tree.update(1, 1, MAX_COORDINATE, current_a_val, dp_val_for_current_a)
        
        max_total_arrays = max(max_total_arrays, dp_val_for_current_a)
    
    print(max_total_arrays)

def main():
    global seg_tree
    seg_tree = SegmentTree()
    
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()
'''