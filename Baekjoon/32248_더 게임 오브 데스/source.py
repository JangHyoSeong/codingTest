N, T = map(int, input().split())
arr = list(map(int, input().split()))

visited = [-1] * (N+1)
path = []
current = 1

while visited[current] == -1:
    visited[current] = len(path)
    path.append(current)
    current = arr[current-1]

cycle_start = visited[current]
cycle_length = len(path) - cycle_start

if T < cycle_start:
    print(path[T])
else:
    idx = (T - cycle_start) % cycle_length
    print(path[cycle_start + idx])