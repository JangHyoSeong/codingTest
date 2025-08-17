from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

counter = Counter(cards)
max_len = max(counter.values())

for i in range(N):
    for j in range(i + 1, N):
        diff = cards[j] - cards[i]
        step = j - i

        if diff % step != 0:
            continue

        d = diff // step

        length = 0
        for k in range(N):
            if cards[i] + (k - i) * d == cards[k]:
                length += 1
        
        max_len = max(max_len, length)

print(N - max_len)