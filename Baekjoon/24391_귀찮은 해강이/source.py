import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(parent, a, b)

arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
now_node_top = find(parent, arr[0])
for i in range(1, N):
    next_node_top = find(parent, arr[i])
    if now_node_top != next_node_top:
        count += 1
        now_node_top = next_node_top

print(count)