import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

max_honey = 0

for i in range(2, N):
    max_honey = max(max_honey, (prefix[N] - arr[0] - arr[i - 1]) + (prefix[N] - prefix[i]))
    max_honey = max(max_honey, (prefix[i] - arr[0]) + (prefix[N - 1] - prefix[i - 1]))
    max_honey = max(max_honey, prefix[i - 1] + (prefix[N - 1] - arr[i - 1]))

print(max_honey)