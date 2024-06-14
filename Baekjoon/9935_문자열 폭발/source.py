string = input()

boom = input()
boom_len = len(boom)

stack = []

for c in string:
    stack.append(c)
    if len(stack) >= boom_len and ''.join(stack[-boom_len:]) == boom:
        for i in range(boom_len):
            stack.pop()
    
if stack:
    print(''.join(stack))
else:
    print("FRULA")