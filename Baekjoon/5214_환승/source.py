from collections import deque

N, K, M = map(int, input().split())

station_to_tube = [[] for _ in range(N+1)]
tube_to_station = []

for i in range(M):
    arr = list(map(int, input().split()))
    tube_to_station.append(arr)
    for station in arr:
        station_to_tube[station].append(i)

queue = deque([(1, 1)])
visited_station = [False] * (N+1)
visited_station[1] = True
visited_tube = [False] * M

while queue:
    now, count = queue.popleft()

    if now == N:
        print(count)
        break

    for tube in station_to_tube[now]:
        if not visited_tube[tube]:
            visited_tube[tube] = True

            for next in tube_to_station[tube]:
                if not visited_station[next]:
                    visited_station[next] = True
                    queue.append((next, count+1))

else:
    print(-1)