import sys

N, D = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort()

left = 0
max_happiness = 0
now_happiness = 0

for right in range(N):
    now_happiness += arr[right][1]

    while arr[right][0] - arr[left][0] >= D:
        now_happiness -= arr[left][1]
        left += 1
    
    max_happiness = max(max_happiness, now_happiness)

print(max_happiness)