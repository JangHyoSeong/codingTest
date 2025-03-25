import sys

MOD = 1000000007

def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    left_number = build_segment_tree(arr, tree, 2*node, start, mid)
    right_number = build_segment_tree(arr, tree, 2*node + 1, mid+1, end)
    tree[node] = (left_number * right_number) % MOD
    return tree[node]

def update(tree, node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2

    if idx <= mid:
        update(tree, node*2, start, mid, idx, value)
    
    else:
        update(tree, node*2 + 1, mid+1, end, idx, value)
    
    tree[node] = (tree[node*2] * tree[node*2 + 1]) % MOD


def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_number = query(tree, node*2, start, mid, left, right)
    right_number = query(tree, node*2 + 1, mid + 1, end, left, right)

    return (left_number * right_number) % MOD
    


N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

tree = [0] * (4*N)
build_segment_tree(numbers, tree, 1, 0, N-1)

results = []

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        update(tree, 1, 0, N-1, b-1, c)

    else:
        results.append(query(tree, 1, 0, N-1, b-1, c-1))

print("\n".join(map(str, results)))