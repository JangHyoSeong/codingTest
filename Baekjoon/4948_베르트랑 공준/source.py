numbers = []

while True:
    N = int(input())
    if N == 0:
        break

    numbers.append(N)

max_num = max(numbers)

size = 2 * max_num + 1
is_prime = [True] * size
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(size ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, size, i):
            is_prime[j] = False

for n in numbers:
    count = sum(1 for i in range(n+1, 2*n + 1) if is_prime[i])
    print(count)