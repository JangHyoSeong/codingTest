import bisect

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[1])
end_times = [meeting[1] for meeting in meetings]

dp = [0] * (N + 1)
for i in range(1, N + 1):
    start, end, people = meetings[i - 1]
    idx = bisect.bisect_right(end_times, start) - 1    
    dp[i] = max(dp[i - 1], dp[idx + 1] + people)

print(dp[N])