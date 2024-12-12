import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

queries = [int(sys.stdin.readline()) for _ in range(Q)]

dp = [0] * (N + 1)

def dfs(node, parent):
    dp[node] = 1
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node] += dp[child]

dfs(R, -1)

print("\n".join(str(dp[u]) for u in queries))