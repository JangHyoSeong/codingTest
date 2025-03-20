import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

counter = Counter(cards)
most_common = counter.most_common()
max_count = most_common[0][1]

min_most_frequent = min(num for num, count in most_common if count == max_count)

print(min_most_frequent)