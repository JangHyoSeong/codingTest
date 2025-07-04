import sys
from collections import defaultdict

counter = defaultdict(int)
total = 0

for line in sys.stdin:
    tree = line.strip()
    if tree:
        counter[tree] += 1
        total += 1

for tree in sorted(counter):
    print(f"{tree} {counter[tree] / total * 100:.4f}")