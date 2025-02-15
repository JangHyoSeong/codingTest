from collections import Counter

N, C = map(int, input().split())
numbers = list(map(int, input().split()))

count = Counter(numbers)
sorted_numbers = sorted(numbers, key=lambda x : (-count[x], numbers.index(x)))
print(*sorted_numbers)