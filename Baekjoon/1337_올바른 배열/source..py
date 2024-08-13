N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()


min_add = 21e8

for i in range(N):
    end_value = numbers[i] + 4
    count = 0
    for j in range(i, N):
        if numbers[j] > end_value:
            break
        count += 1
    min_add = min(min_add, 5-count)

print(min_add)