N  = int(input())
arr = [int(input()) for _ in range(N)]

idx = 1
stack = []
result = []

for num in arr:
    while idx <= num:
        stack.append(idx)
        result.append('+')
        idx += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result = False
        break

if result:
    for c in result:
        print(c)
else:
    print('NO')