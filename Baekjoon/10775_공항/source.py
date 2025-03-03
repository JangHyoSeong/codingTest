import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)


G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(P)]

parent = list(range(G+1))
count = 0

for plane in arr:
    docking = find(plane)

    if docking == 0:
        break

    union(docking, docking-1)
    count += 1

print(count)