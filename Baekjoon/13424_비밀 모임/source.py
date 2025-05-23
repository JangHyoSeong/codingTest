import sys

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())

    graph = [[int(21e8)] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = c
        graph[b][a] = c
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    K = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))

    min_dist = int(21e8)
    for i in range(1, N+1):
        temp_dist = 0
        for num in start:
            temp_dist += graph[num][i]

        if min_dist > temp_dist:
            result = i
            min_dist = temp_dist
            
    
    print(result)