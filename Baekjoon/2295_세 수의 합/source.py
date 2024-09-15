N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

two_sum = set()
for i in range(N):
    for j in range(i, N):
        two_sum.add(numbers[i] + numbers[j])

for i in range(N-1, -1, -1):
    for j in range(i+1):
        if numbers[i] - numbers[j] in two_sum:
            print(numbers[i])
            exit()