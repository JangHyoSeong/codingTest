import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        
        else:
            parent[root_x] = root_y        

N = int(sys.stdin.readline().rstrip())

parent = list(range(N+1))

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b)

root_set = set()
for i in range(1, N+1):
    root_set.add(find(parent, i))

print(" ".join(map(str, root_set)))