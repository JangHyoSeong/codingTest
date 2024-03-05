N, eat_num, size = map(int, input().split())

size_arr = list(map(int, input().split()))
size_arr.sort(reverse=True)

stack = []
count = 0

while count < eat_num:
    while size_arr and size_arr[-1] < size:
        stack.append(size_arr.pop())

    if stack == []:
        break

    size += stack[-1]
    stack.pop()
    count += 1

print(size)