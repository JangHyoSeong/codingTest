from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

result = list(permutations(numbers, M))

for num in result:
    print(' '.join(map(str, num)))