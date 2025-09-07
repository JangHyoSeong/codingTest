import sys
sys.setrecursionlimit(123456)

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
nodes = [('', 0)] * (N + 1)

for i in range(2, N+1):
    t, a, p = sys.stdin.readline().rstrip().split()
    a, p = int(a), int(p)
    graph[p].append(i)
    nodes[i] = (t, a)

def dfs(node):
    total_sheep = 0
    for child in graph[node]:
        total_sheep += dfs(child)

    t, a = nodes[node]
    if t == 'W':
        if total_sheep > a:
            return total_sheep - a
        
        else:
            return 0
    
    elif t == 'S':
        return total_sheep + a
    else:
        return total_sheep

print(dfs(1))