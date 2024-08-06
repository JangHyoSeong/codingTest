from itertools import combinations

N = int(input())

arr = []
for i in range(1, 11):
    for comb in combinations(range(10), i):
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        arr.append(num)

    
arr.sort()

if N >= len(arr):
    print(-1)
else:
    print(arr[N])