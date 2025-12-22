import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
cards = Counter(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for num in arr:
    print(cards[num], end=" ")