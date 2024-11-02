import sys
from heapq import heappop, heappush


N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

leftheap, rightheap = [], []
result = []

heappush(leftheap, -numbers[0])
result.append(numbers[0])

for i in range(1, N):
    num = numbers[i]

    if num <= -leftheap[0]:
        heappush(leftheap, -num)
    else:
        heappush(rightheap, num)

    if len(leftheap) > len(rightheap) + 1:
        heappush(rightheap, -heappop(leftheap))
    elif len(leftheap) < len(rightheap):
        heappush(leftheap, -heappop(rightheap))

    result.append(-leftheap[0])

print("\n".join(map(str, result)))
