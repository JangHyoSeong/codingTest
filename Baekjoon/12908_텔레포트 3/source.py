from heapq import heappush, heappop

def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

teleport_map = {}
nodes = {start, end}

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = (x1, y1), (x2, y2)
    teleport_map[a] = b
    teleport_map[b] = a
    nodes.add(a)
    nodes.add(b)

dist = {}
pq = [(0, start)]

while pq:
    time, now = heappop(pq)
    if now in dist:
        continue
    dist[now] = time

    for nxt in nodes:
        if nxt not in dist:
            heappush(pq, (time + calc_dist(now, nxt), nxt))

    if now in teleport_map:
        tp = teleport_map[now]
        if tp not in dist:
            heappush(pq, (time + 10, tp))

print(dist[end])