N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

min_dist = [float('inf')] * (N+1)
min_dist[1] = 0

for i in range(N):
    for j in range(M):
        now_node = edges[j][0]
        next_node = edges[j][1]
        dist = edges[j][2]

        if min_dist[now_node] != float('inf') and min_dist[next_node] > min_dist[now_node] + dist:
            min_dist[next_node] = min_dist[now_node] + dist
            if i == N-1:
                print(-1)
                exit()

for i in range(2, N+1):
    if min_dist[i] == float('inf'):
        print(-1)
    else:
        print(min_dist[i])