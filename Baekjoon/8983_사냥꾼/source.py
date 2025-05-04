import sys
import bisect

M, N, L = map(int, sys.stdin.readline().rstrip().split())
shooting_places = list(map(int, sys.stdin.readline().rstrip().split()))
animals = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

shooting_places.sort()
count = 0

for animal in animals:
    x, y = animal

    if y > L:
        continue

    left = x - (L - y)
    right = x + (L - y)

    idx = bisect.bisect_left(shooting_places, left)

    if idx < M and shooting_places[idx] <= right:
        count += 1
    
print(count)