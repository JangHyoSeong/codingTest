import sys
sys.setrecursionlimit(100000)

def find_lca(parent, depth, a, b):
    while depth[a] > depth[b]:
        a = parent[a]
    
    while depth[b] > depth[a]:
        b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

def dfs(parent, node, d):
    depth[node] = d
    for child in tree[node]:
        dfs(parent, child, d+1)

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())

    parent = [0] * (N+1)
    depth = [0] * (N+1)
    tree = [[] for _ in range(N+1)]

    is_root = [True] * (N+1)

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        parent[b] = a
        is_root[b] = False
        tree[a].append(b)

        root = is_root.index(True, 1)

    dfs(parent, root, 0)
    a, b = map(int, sys.stdin.readline().split())
    print(find_lca(parent, depth, a, b))