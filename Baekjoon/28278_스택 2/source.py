import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    
    op = arr[0]

    if op == 1:
        stack.append(arr[1])
    
    elif op == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif op == 3:
        print(len(stack))
    
    elif op == 4:
        if stack:
            print(0)
        else:
            print(1)
    
    else:
        if stack:
            print(stack[-1])
        
        else:
            print(-1)