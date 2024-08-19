from collections import deque

a, b, c, d = map(int, input().split())

q = deque()
q.append([0, 0, 0])

visited = {}
visited[(0, 0)] = True

while q:
    now_a, now_b, count = q.popleft()

    if now_a == c and now_b == d:
        print(count)
        break

    if now_a > 0 and now_b != b:
        temp_a = now_a
        temp_b = now_b

        if b - now_b <= now_a:
            temp_a -= (b-temp_b)
            temp_b = b
        else:
            temp_b += temp_a
            temp_a = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True

    if now_b > 0 and now_a != a:
        temp_a = now_a
        temp_b = now_b

        if a - now_a <= now_b:
            temp_b -= (a-temp_a)
            temp_a = a
        else:
            temp_a += temp_b
            temp_b = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True


    if now_a > 0:
        if visited.get((0, now_b)) is None:
            q.append([0, now_b, count+1])
            visited[(0, now_b)] = True
    
    if now_b > 0:
        if visited.get((now_a, 0)) is None:
            q.append([now_a, 0, count+1])
            visited[(now_a, 0)] = True

    if now_a < a:
        if visited.get((a, now_b)) is None:
            q.append([a, now_b, count+1])
            visited[(a, now_b)] = True

    if now_b < b:
        if visited.get((now_a, b)) is None:
            q.append([now_a, b, count+1])
            visited[(now_a, b)] = True
else:
    print(-1)