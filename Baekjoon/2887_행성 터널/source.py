import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

    return True

N = int(sys.stdin.readline().rstrip())
planets = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

edges = []
for dim in range(3):
    planets.sort(key=lambda p: p[dim])
    for i in range(N-1):
        cost = abs(planets[i][dim] - planets[i+1][dim])
        edges.append((cost, planets[i][3], planets[i+1][3]))

edges.sort()

parent = list(range(N))
total_cost = 0
count = 0

for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost
        count += 1
        if count == N - 1:
            break

print(total_cost)