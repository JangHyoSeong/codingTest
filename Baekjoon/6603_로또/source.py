from itertools import combinations

while True:
    k, *arr = list(map(int, input().split()))

    if k == 0:
        break

    combs = combinations(arr, 6)
    for comb in combs:
        print(" ".join(map(str, comb)))
    print()