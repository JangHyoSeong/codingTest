import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.extend(arr[:k-1])

current_window = defaultdict(int)
count = 0
max_count = 0

for i in range(k):
    if current_window[arr[i]] == 0:
        count += 1
    current_window[arr[i]] += 1

if current_window[c] == 0:
    max_count = count + 1
else:
    max_count = count

for i in range(1, N):
    removed_sushi = arr[i-1]
    current_window[removed_sushi] -= 1
    if current_window[removed_sushi] == 0:
        count -= 1

    added_sushi = arr[i+k-1]
    if current_window[added_sushi] == 0:
        count += 1
    current_window[added_sushi] += 1

    if current_window[c] == 0:
        max_count = max(max_count, count + 1)
    else:
        max_count = max(max_count, count)

print(max_count)