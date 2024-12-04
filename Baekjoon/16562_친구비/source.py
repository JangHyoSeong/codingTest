def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

N, M, k = map(int, input().split())
money = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N)]
rank = [0] * N

for v, w in edges:
    union(parent, rank, v-1, w-1)

root_min_cost = {}
for i in range(N):
    root = find(parent, i)
    if root not in root_min_cost:
        root_min_cost[root] = money[i]
    else:
        root_min_cost[root] = min(root_min_cost[root], money[i])

total_cost = sum(root_min_cost.values())

print(total_cost if total_cost <= k else "Oh no")