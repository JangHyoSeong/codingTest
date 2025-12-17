from itertools import product

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for p in product(arr, repeat=M):
    print(*p)