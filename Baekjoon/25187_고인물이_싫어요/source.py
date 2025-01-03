import sys

N, M, Q = map(int, sys.stdin.readline().rstrip().split())
water = list(map(int, sys.stdin.readline().rstrip().split()))
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

parent = list(range(N))
size = [1] * N
clean_count = [water[i] for i in range(N)]
dirty_count = [1-water[i] for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        clean_count[root_x] += clean_count[root_y]
        dirty_count[root_x] += dirty_count[root_y]

for pipe in pipes:
    union(pipe[0]-1, pipe[1]-1)

for query in queries:
    query -= 1
    root_query = find(query)

    if clean_count[root_query] > dirty_count[root_query]:
        print(1)
    else:
        print(0)