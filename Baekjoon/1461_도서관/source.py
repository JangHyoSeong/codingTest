from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

negative = []
positive = []

for x in arr:

    if x > 0:
        positive.append(x)
    elif x < 0:
        negative.append(x)

negative.sort()
positive.sort(reverse=True)

result = 0

for i in range(0, len(negative), M):
    result += abs(negative[i]) * 2

for i in range(0, len(positive), M):
    result += positive[i] * 2

if negative and positive:
   result -= max(abs(negative[0]), positive[0])
elif negative:
    result -= abs(negative[0])
elif positive:
    result -= positive[0]

print(result)