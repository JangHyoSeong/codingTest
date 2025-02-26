from itertools import combinations
from collections import deque

N = int(input())
populations = [0] + list(map(int, input().split()))

edges = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    edges[i] = data[1:]

min_population = int(21e8)

for i in range(1, N//2 + 1):
    for subset in combinations(range(1, N+1), i):
        area1 = set(subset)
        area2 = set(range(1, N+1)) - area1

        queue = deque([next(iter(area1))])
        visited = set(queue)

        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        if visited != area1:
            continue

        queue = deque([next(iter(area2))])
        visited = set(queue)
        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area2 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        if visited != area2:
            continue

        pop1 = sum(populations[i] for i in area1)
        pop2 = sum(populations[i] for i in area2)
        min_population = min(min_population, abs(pop1 - pop2))

print(min_population if min_population != int(21e8) else -1)