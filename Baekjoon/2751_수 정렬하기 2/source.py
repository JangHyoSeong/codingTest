import sys

N = int(sys.stdin.readline().rstrip())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

numbers.sort()
for number in numbers:
    print(number)