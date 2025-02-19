import bisect

N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
wires.sort()

b_values = [b for _, b in wires]

dp = []
for num in b_values:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

max_lis = len(dp)
print(N - max_lis)