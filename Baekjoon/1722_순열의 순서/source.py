from math import factorial

N = int(input())
k, *arr = map(int, input().split())

if k == 1:
    c = arr[0] - 1
    result = []
    numbers = list(range(1, N + 1))

    for i in range(N):
        fact = factorial(N - 1 - i)
        idx = c // fact
        result.append(numbers[idx])
        numbers.pop(idx)
        c %= fact

    print(*result)

else:
    perm = arr
    count = 0
    numbers = list(range(1, N + 1))

    for i in range(N):
        idx = numbers.index(perm[i])
        count += idx * factorial(N - 1 - i)
        numbers.pop(idx)

    print(count + 1)