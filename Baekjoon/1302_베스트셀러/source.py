from collections import Counter

N = int(input())
books = [input().strip() for _ in range(N)]

counter = Counter(books)
max_count = max(counter.values())

candidates = [book for book, cnt in counter.items() if cnt == max_count]

print(min(candidates))