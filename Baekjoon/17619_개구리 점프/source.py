import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[max(root_x, root_y)] = min(root_x, root_y)

N, Q = map(int, sys.stdin.readline().split())

logs = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

logs.sort(key=lambda x: x[0])

parent = list(range(N))
right_end = logs[0][1]

for i in range(N-1):

    right_end = max(right_end, logs[i][1])
    if right_end >= logs[i+1][0]:
        union(logs[i][3], logs[i+1][3])

for i in range(N):
    find(i)

for a, b in queries:
    if find(a - 1) == find(b - 1):
        print(1)
    else:
        print(0)
