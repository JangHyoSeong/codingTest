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
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
        return True
    
    return False


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N+1)]
total_cost = 0
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)