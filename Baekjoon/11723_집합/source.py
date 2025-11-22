import sys

M = int(sys.stdin.readline().rstrip())

s = set()
for _ in range(M):
    data = sys.stdin.readline().rstrip()
    if data == "all":
        s = set(range(1, 21))
    
    elif data == "empty":
        s = set()
    
    else:
        op, num = data.split()

        num = int(num)
        if op == "add":
            s.add(num)
        
        elif op == "remove":
            if num in s:
                s.remove(num)
        
        elif op == "check":
            if num in s:
                print(1)
            else:
                print(0)
        
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)