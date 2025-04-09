from collections import deque

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, int(21e8)
answer = right

while left <= right:
    mid = (left + right) // 2
    K = mid

    visited = [False] * N
    q = deque([0])
    visited[0] = True

    while q:
        now = q.popleft()
        for next in range(now + 1, N):
            cost = (next - now) * (1 + abs(arr[now] - arr[next]))
            if cost > K:
                continue
            if not visited[next]:
                visited[next] = True
                q.append(next)

    if visited[N-1]:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)