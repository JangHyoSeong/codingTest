import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

left, right = 0, 1

count = 0
while right <= N:
    now_sum = prefix_sum[right] - prefix_sum[left]
    if now_sum == M:
        count += 1
        right += 1
        left += 1
    
    elif now_sum < M:
        right += 1
    
    else:
        left += 1
    
print(count)