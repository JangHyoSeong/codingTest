from sys import stdin

N = int(stdin.readline().rstrip())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]


stack = []
count = 0

for i in range(N):

    same_height = 1

    while stack and stack[-1][0] <= arr[i]:
        count += stack[-1][1]

        if stack[-1][0] == arr[i]:
            same_height += stack[-1][1]

        stack.pop()

    if stack:
        count += 1
    
    stack.append([arr[i], same_height])

print(count)