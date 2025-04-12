import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

room = set()
count = 0
memo = [-1] * N

for i in range(N):
    if arr[i]:
        room.add(i)
        count += arr[i]
        memo[i] = 0

if len(room) == 0:
    print(N // 2)
    exit()

if N == 2:
    if len(room) == 1:
        count += 1
    print(count)
    exit()

start = 0
for i in range(N):
    if i in room:
        start = i
        break

for i in range(start, start + N):
    idx = i % N
    if memo[idx] == -1:
        left = (idx - 1) % N
        right = (idx + 1) % N
        if memo[left] != 1 and memo[right] != 1:
            memo[idx] = 1
            count += 1

print(count)