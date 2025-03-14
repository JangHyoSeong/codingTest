from itertools import permutations

N, M = map(int, input().split())
results = list(permutations(range(1, N+1), M))

for result in results:
    print(" ".join(map(str, result)))