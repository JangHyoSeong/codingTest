N = int(input())
words = [input() for _ in range(N)]

count = 0
for word in words:
    stack = []
    
    for c in word:
        if not stack:
            stack.append(c)
        
        else:
            if stack[-1] != c:
                stack.append(c)

            else:
                stack.pop()
    
    if not stack:
        count += 1

print(count)