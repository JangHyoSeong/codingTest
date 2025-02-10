import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))
rank = [1] * (N+1)
for _ in range(M):
    operator, a, b = map(int, sys.stdin.readline().rstrip().split())

    if operator == 0:
        union(parent, rank, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")