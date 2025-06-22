import sys
from heapq import heappop, heappush

testcase = 1
while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    
    dist = [[int(21e8)] * N for _ in range(N)]
    dist[0][0] = table[0][0]

    pq = [(table[0][0], 0, 0)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while pq:
        now_dist, x, y = heappop(pq)

        if now_dist > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = now_dist + table[nx][ny]

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
    
    print(f'Problem {testcase}: {dist[N-1][N-1]}')
    testcase += 1