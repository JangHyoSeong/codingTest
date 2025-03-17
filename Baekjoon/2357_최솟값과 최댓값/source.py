import sys

def build_segment_tree(arr: list, tree: list, node: int, start: int, end: int, type: str):
    if start == end:
        tree[node] = arr[start]
    
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2*node + 1, start, mid, type)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end, type)
        
        if type == "max":
            tree[node] = max(tree[2*node + 1], tree[2*node + 2])
        elif type == "min":
            tree[node] = min(tree[2*node + 1], tree[2*node + 2])

def query_segment_tree(tree: list, node: int, start: int, end: int, left: int, right: int, type: str):
    if right < start or end < left:
        if type == "min":
            return int(21e8)
        elif type == "max":
            return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_result = query_segment_tree(tree, 2*node + 1, start, mid, left, right, type)
    right_result = query_segment_tree(tree, 2*node + 2, mid + 1, end, left, right, type)
    
    if type == "max":
        return max(left_result, right_result)
    elif type == "min":
        return min(left_result, right_result)

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

min_tree = [0] * (4*N)
max_tree = [0] * (4*N)

build_segment_tree(arr, min_tree, 0, 0, N-1, "min")
build_segment_tree(arr, max_tree, 0, 0, N-1, "max")

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    min_result = query_segment_tree(min_tree, 0, 0, N-1, a-1, b-1, "min")
    max_result = query_segment_tree(max_tree, 0, 0, N-1, a-1, b-1, "max")
    print(min_result, max_result)