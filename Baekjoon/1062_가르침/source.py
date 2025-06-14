from itertools import combinations

N, K = map(int, input().split())
words = [input() for _ in range(N)]

essential = {"a", "n", "t", "i", "c"}

if K < 5:
    print(0)
    exit()

mid_parts = []
for word in words:
    mid = word[4:-4]
    mid_parts.append(set(mid) - essential)

max_count = 0
all_chars = set('abcdefghijklmnopqrstuvwxyz') - essential

for comb in combinations(all_chars, K-5):
    teach = set(comb)
    count = 0

    for mid in mid_parts:
        if mid.issubset(teach):
            count += 1
    
    max_count = max(max_count, count)

print(max_count)