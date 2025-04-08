import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
cards = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_sum = 0
result = 0

for i in range(N):
    card = cards[i]
    comb = combinations(card, 3)
    
    temp_max = 0
    for numbers in comb:
        temp_sum = sum(numbers) % 10
        temp_max = max(temp_max, temp_sum)
    
    if temp_max >= max_sum:
        result = i + 1
        max_sum = temp_max

print(result)