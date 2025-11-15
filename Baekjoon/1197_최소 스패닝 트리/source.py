import sys
sys.setrecursionlimit(10**6)

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
        
        return True
    return False

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(V+1))

total_cost = 0
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)