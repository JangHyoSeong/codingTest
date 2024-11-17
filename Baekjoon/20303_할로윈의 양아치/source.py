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

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

parent = [i for i in range(N)]
rank = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(parent, rank, a, b)

component = {}
for i in range(N):
    root = find(parent, i)
    if root not in component:
        component[root] = {'count': 0, 'candies': 0}
    component[root]['count'] += 1
    component[root]['candies'] += candies[i]

dp = [0] * K

for comp in component.values():
    count = comp['count']
    candy_sum = comp['candies']

    for j in range(K - 1, count - 1, -1):
        dp[j] = max(dp[j], dp[j - count] + candy_sum)

print(dp[K - 1])