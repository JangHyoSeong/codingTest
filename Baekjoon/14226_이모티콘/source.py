from collections import deque

S = int(input())

screen = 1

visited = [[False] * (S+1) for _ in range(S+1)]
visited[1][0] = True

# 현재 이모티콘 개수, 초, 클립보드 상태
q = deque([[1, 0, 0]])

while q:
    now, count, clipboard = q.popleft()

    if now == S:
        print(count)
        break
    
    if now != clipboard and not visited[now][now]:
        q.append([now, count+1, now])
    
    next = now + clipboard
    if next < S+1 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True
    
    next = now - 1
    if next > 0 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True