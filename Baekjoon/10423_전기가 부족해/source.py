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


N, M, K = map(int, sys.stdin.readline().rstrip().split())
generators = list(map(int, sys.stdin.readline().rstrip().split()))

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x : x[2])

parent = list(range(N+1))
rank = [0] * (N+1)

virtual_node = 0
for generator in generators:
    union(parent, rank, virtual_node, generator)

min_cost = 0
for u, v, w in edges:
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        min_cost += w

print(min_cost)