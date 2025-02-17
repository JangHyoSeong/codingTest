import sys

def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2*node + 1, start, mid)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end)
        tree[node] = min(tree[2*node + 1], tree[2*node + 2])

def query_segment_tree(tree, node, start, end, left, right):
    if right < start or end < left:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_min = query_segment_tree(tree, 2*node + 1, start, mid, left, right)
    right_min = query_segment_tree(tree, 2*node + 2, mid+1, end, left, right)
    return min(left_min, right_min)

N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
tree = [0] * (4*N)
build_segment_tree(numbers, tree, 0, 0, N-1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(query_segment_tree(tree, 0, 0, N-1, a-1, b-1)))
    sys.stdout.write("\n")