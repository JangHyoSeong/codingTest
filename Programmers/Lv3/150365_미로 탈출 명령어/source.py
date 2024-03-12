from collections import deque

def solution(n, m, x, y, r, c, k):

    # 가야하는 최소 거리와, 갈 수 있는 횟수가 서로 짝수, 서로 홀수여야만 도착할 수 있음
    if (abs(r-x) + abs(c-y))%2 != k%2:
        return 'impossible'
    
    # 가야 하는 최소거리가 이동횟수보다 길다면 최단거리로 가도 도착못함.
    if abs(x - r) + abs(y - c) > k:
        return 'impossible'
    
    # BFS를 위해 queue 선언 
    q = deque()

    # q에는 현재 x, y좌표, 이동한 위치를 나타내는 리스트, 몇번 이동했는지가 들어감 
    q.append((x, y, list(), 0))
    move = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    dir = ['d', 'l', 'r', 'u']

    # BFS 시작
    while q:
        now_x, now_y, answer, count = q.popleft()

        # count가 6에 도달하고, 위치에 도착했다면 break
        if count == k:
            if now_x == r and now_y == c:
                break

        # 아니라면 계속 탐색
        else:
            for i in range(4):
                new_x = now_x + move[i][0]
                new_y = now_y + move[i][1]

                # 미로를 벗어나지 않으면서
                if 0 < new_x <= n and 0 < new_y <= m:

                    # 다음 위치에서 목적지에서 멀어지더라도 갈 수 있는 거리라면 이동
                    if abs(new_x - r) + abs(new_y - c) + count + 1 <= k:
                        q.append((new_x, new_y, answer + [dir[i]], count + 1))
                        # break를 통한 가지치기
                        # 어차피 갈 수 있는 범위라면, 사전순으로 가장 빠른 순서로 가는 것만이 의미있는 이동
                        break

    return "".join(answer)