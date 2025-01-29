from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())

combs = combinations(arr, L)
result = []
for comb in combs:
    vowel = 0
    for c in list(comb):
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1

    if 1 <= vowel <= L-2:
        result.append(sorted(list(comb)))

result.sort()
for answer in result:
    print("".join(map(str, answer)))