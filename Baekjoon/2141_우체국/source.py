import sys

N = int(sys.stdin.readline().rstrip())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

towns.sort(key=lambda x : x[0])

total_population = sum(town[1] for town in towns)

current_population = 0
for town in towns:
    current_population += town[1]
    if current_population >= (total_population + 1) // 2:
        print(town[0])
        break