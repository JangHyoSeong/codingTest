import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

total_time = arr[N-1] + 1 - arr[0]
gaps = []
for i in range(N-1):
    gaps.append(arr[i+1] - arr[i] - 1)

gaps.sort(reverse=True)
off_time = sum(gaps[:K-1]) if K > 1 else 0

print(total_time - off_time)