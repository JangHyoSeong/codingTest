import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    commands = list(sys.stdin.readline().rstrip().split())
    command = commands[0]

    if command == "push":
        stack.append(int(commands[1]))
    
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command == "size":
        print(len(stack))
    
    elif command == "empty":
        print(0 if stack else 1)
    
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)