N = int(input())
tower = list(map(int, input().split()))

stack = []
result = []
for i in range(N):
    if not stack:
        result.append(0)
        stack.append([tower[i], i+1])
    else:
        if stack[-1][0] > tower[i]:
            result.append(stack[-1][1])
            stack.append([tower[i], i+1])
        else:
            while stack and stack[-1][0] < tower[i]:
                stack.pop()
            if stack:
                result.append(stack[-1][1])
            else:
                result.append(0)            
            stack.append([tower[i], i+1])

print(" ".join(map(str, result)))