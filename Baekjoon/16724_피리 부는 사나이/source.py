def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x
    


N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

parent = [i for i in range(N * M)]

move = {
    "D" : (1, 0),
    "U" : (-1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}

for i in range(N):
    for j in range(M):
        ni, nj = i + move[table[i][j]][0], j + move[table[i][j]][1]
        union(parent, i * M + j, ni * M + nj)

roots = set(find(parent, i) for i in range(N * M))
print(len(roots))
