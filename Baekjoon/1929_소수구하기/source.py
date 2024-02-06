from math import sqrt

def primeNumber(M, N):

    numbers = [1 for _ in range(0, N+1)]

    numbers[0] = 0
    numbers[1] = 0

    prime = 2
    while prime <= sqrt(N):
        if numbers[prime] == 0:
            prime += 1
            continue

        for idx in range(prime*prime, N+1):
            if idx % prime == 0:
                numbers[idx] = 0
        prime += 1

    for i in range(N+1):
        if i >= M and numbers[i] == 1:
            print(i)

M, N = map(int, input().split())
primeNumber(M, N)