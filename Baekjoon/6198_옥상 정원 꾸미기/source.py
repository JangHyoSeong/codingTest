import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

stack = []
count = 0

for num in arr:
    while stack and stack[-1] <= num:
        stack.pop()

    count += len(stack)
    stack.append(num)

print(count)