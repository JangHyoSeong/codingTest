import sys

def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]

    else:
        mid = (start + end) // 2
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        build(arr, tree, left_child, start, mid)
        build(arr, tree, right_child, mid + 1, end)
        tree[node] = max(tree[left_child], tree[right_child])

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_max = query(tree, node * 2 + 1, start, mid , left, right)
    right_max = query(tree, node * 2 + 2, mid + 1, end, left, right)
    return max(left_max, right_max)


def is_valid(N, arr):
    first_index = {}
    last_index = {}

    for i in range(N):
        if arr[i] not in first_index:
            first_index[arr[i]] = i
        last_index[arr[i]] = i
    
    tree = [0] * (4 * N)
    build(arr, tree, 0, 0, N - 1)

    for num in first_index:
        left, right = first_index[num], last_index[num]
        max_in_range = query(tree, 0, 0, N-1, left, right)
        if max_in_range > num:
            return "No"
    return "Yes"

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(is_valid(N, arr))