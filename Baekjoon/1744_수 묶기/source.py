N = int(input())

positive = []
negative = []
one = 0
zero = 0

for _ in range(N):
    num = int(input())

    if num > 1:
        positive.append(num)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        negative.append(num)

positive.sort()
negative.sort(reverse=True)

result = 0
while len(positive) > 1:
    result += positive.pop() * positive.pop()
if positive:
    result += positive[0]

while len(negative) > 1:
    result += negative.pop() * negative.pop()

if negative:
    if zero == 0:
        result += negative[0]

result += one
print(result)