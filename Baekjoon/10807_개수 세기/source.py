N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

count = 0
for number in numbers:
    if number == v:
        count += 1

print(count)