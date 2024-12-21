import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

word_count = Counter(words)
result = sorted((word for word in word_count if len(word) >= M), key=lambda x: (-word_count[x], -len(x), x))

print('\n'.join(result))