import operator
from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

visited = {}
visited[s] = ''
visited[0] = '-'
if s != 1:
    visited[1] = '/'
visited[2*s] = '+'
visited[s*s] = '*'

q = deque()
q.append(s)
q.append(s*s)
q.append(2*s)
q.append(0)
q.append(1)

operations = {
    '*': operator.mul,
    '+': operator.add,
}

calcs = ['*', '+']

while q:
    now = q.popleft()

    if now == t:
        break

    for calc in calcs:
        next = operations[calc](now, now)
        if next > t:
            continue

        if visited.get(next) is None:
            visited[next] = visited[now] + calc
            q.append(next)

if visited.get(t) is None:
    print(-1)
else:
    print(visited[t])
