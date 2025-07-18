N = int(input())

power = 1
while power * 2 <= N:
    power *= 2

if N == power:
    print(N)
else:
    print(2 * (N - power))