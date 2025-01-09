from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * W)
weight = 0
time = 0

for truck in trucks:
    while True:
        time += 1
        weight -= bridge.popleft()

        if weight + truck <= L:
            bridge.append(truck)
            weight += truck
            break
        else:
            bridge.append(0)

time += W

print(time)