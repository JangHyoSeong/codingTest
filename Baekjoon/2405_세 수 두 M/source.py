import sys

N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

numbers.sort()

max_gap = 0
for i in range(1, N-1):
    avg_min = (numbers[0] + numbers[i] + numbers[i+1])
    avg_max = (numbers[i-1] + numbers[i] + numbers[N-1])

    max_gap = max(max_gap, abs(avg_max - numbers[i]*3), abs(avg_min - numbers[i]*3))

print(max_gap)