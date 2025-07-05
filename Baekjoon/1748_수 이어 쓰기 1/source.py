N = int(input())

digit = 1
start = 1
length = 0

while start <= N:
    end = min(N, start * 10 - 1)
    count = end - start + 1
    length += count * digit
    digit += 1
    start *= 10

print(length)