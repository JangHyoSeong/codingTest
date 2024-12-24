def dfs(node):
    cycle = []
    while not visited[node]:
        visited[node] = True
        cycle.append(node)
        node = arr[node] - 1

    if node in cycle:
        cycle_start = cycle.index(node)
        for i in cycle[cycle_start:]:
            team[i] = True

T = int(input())

for testcase in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    visited = [False] * N
    team = [False] * N

    for i in range(N):
        if not visited[i]:
            dfs(i)
    
    print(N - sum(team))