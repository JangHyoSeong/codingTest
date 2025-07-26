import sys

K = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

stack = []
for i in range(K):
    if arr[i] == 0:
        stack.pop()
    
    else:
        stack.append(arr[i])

print(sum(stack))