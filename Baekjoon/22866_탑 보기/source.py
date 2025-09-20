import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = [0] * N
nearest = [0] * N

stack = []
for i in range(N):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        nearest[i] = stack[-1] + 1
    stack.append(i)

stack = []
for i in range(N - 1, -1, -1):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        
        if nearest[i] == 0:
            nearest[i] = stack[-1] + 1
        else:
            left_dist = abs((nearest[i] - 1) - i)
            right_dist = abs((stack[-1]) - i)
            if right_dist < left_dist or (right_dist == left_dist and stack[-1] + 1 < nearest[i]):
                nearest[i] = stack[-1] + 1
    stack.append(i)

for i in range(N):
    if count[i] == 0:
        print(0)
    else:
        print(count[i], nearest[i])