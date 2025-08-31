import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
parent = [i for i in range(N + 1)]
total = 0
max_cost = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost
        max_cost = max(max_cost, cost)

print(total - max_cost)