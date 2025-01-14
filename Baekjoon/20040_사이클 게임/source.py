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
        
        return False
    
    else:
        return True

n, m = map(int, sys.stdin.readline().rstrip().split())
parent = list(range(n))
rank = [0] * n

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if union(parent, rank, a, b):
        print(i)
        exit()

print(0)