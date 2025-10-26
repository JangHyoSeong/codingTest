import sys
from bisect import bisect_left

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = []
for num in arr:
    idx = bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(N - len(dp))