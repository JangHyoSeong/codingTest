import sys
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = sorted(sys.stdin.readline().rstrip() for _ in range(N))

answer = 0
for _ in range(M):
    query = sys.stdin.readline().rstrip()
    idx = bisect_left(arr, query)

    if idx < N and arr[idx].startswith(query):
        answer += 1

print(answer)