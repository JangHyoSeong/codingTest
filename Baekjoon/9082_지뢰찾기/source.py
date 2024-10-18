T = int(input())
for testcase in range(T):
    N = int(input())
    graph = []
    graph.append([int(c) for c in input().strip()])
    graph.append([c for c in input().strip()])

    result = 0

    for i in range(N):
        if graph[1][i] == '*':
            result += 1
            if i > 0:
                graph[0][i - 1] -= 1
            graph[0][i] -= 1
            if i < N - 1:
                graph[0][i + 1] -= 1

    if graph[1][0] == '#' and graph[0][0] != 0 and graph[0][1] != 0:
        result += 1
        graph[0][0] -= 1
        graph[0][1] -= 1

    for i in range(1, N - 1):
        if graph[1][i] == '#':
            if graph[0][i - 1] >= 1 and graph[0][i] >= 1 and graph[0][i + 1] >= 1:
                result += 1
                graph[0][i - 1] -= 1
                graph[0][i] -= 1
                graph[0][i + 1] -= 1

    if graph[1][N - 1] == '#' and graph[0][N - 1] != 0 and graph[0][N - 2] != 0:
        result += 1
        graph[0][N - 1] -= 1
        graph[0][N - 2] -= 1

    print(result)
