import sys

N = int(sys.stdin.readline().rstrip())
numbers = [list(map(int, sys.stdin.readline().rstrip().split("."))) for _ in range(N)]

for number in numbers:
    if len(number) == 1:
        number.append(-1)

numbers.sort()

for number in numbers:
    if number[1] != -1:
        print(f'{number[0]}.{number[1]}')
    else:
        print(number[0])