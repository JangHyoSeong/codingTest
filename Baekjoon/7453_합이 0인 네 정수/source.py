import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
arr = [list(x) for x in zip(*(map(int, sys.stdin.readline().rstrip().split()) for _ in range(N)))]

sum_AB = defaultdict(int)
for a in arr[0]:
    for b in arr[1]:
        sum_AB[a+b] += 1

count = 0
for c in arr[2]:
    for d in arr[3]:
        target = -(c + d)

        if target in sum_AB:
            count += sum_AB[target]

print(count)