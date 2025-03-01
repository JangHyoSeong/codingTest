import sys
import bisect

N, Q = map(int, sys.stdin.readline().rstrip().split())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

towns.sort(key=lambda x: x[1])
town_positions = [x for _, x in towns]

prefix_population = [0] * (N+1)
prefix_weighted_distance = [0] * (N+1)

for i in range(1, N+1):
    a, x = towns[i-1]
    prefix_population[i] = prefix_population[i-1] + a
    prefix_weighted_distance[i] = prefix_weighted_distance[i-1] + a*x

results = []
for q in queries:
    idx = bisect.bisect_left(town_positions, q)

    left_population = prefix_population[idx]
    left_distance = prefix_weighted_distance[idx]
    left_cost = left_population * q - left_distance

    right_population = prefix_population[N] - left_population
    right_distance = prefix_weighted_distance[N] - left_distance
    right_cost = right_distance - right_population * q

    results.append(left_cost + right_cost)

print("\n".join(map(str, results)))