N, K = map(int, input().split())
number = list(input())

count = 0
stack = []

for i in range(N):
    if stack == []:
        stack.append(int(number[i]))
    else:
        while stack and stack[-1] < int(number[i]) and count < K:
            stack.pop()
            count += 1
        stack.append(int(number[i]))
            

if count < K:
    for _ in range(count, K):
        stack.pop()

print("".join(map(str, stack)))