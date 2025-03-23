from collections import defaultdict

N, K = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

genre_dict = defaultdict(list)

for price, genre in books:
    genre_dict[genre].append(price)

prefix_sums = {}
for genre in genre_dict:
    genre_dict[genre].sort(reverse=True)
    prefix_sums[genre] = [0] * (len(genre_dict[genre]) + 1)
    for i in range(1, len(prefix_sums[genre])):
        prefix_sums[genre][i] = prefix_sums[genre][i-1] + genre_dict[genre][i-1]
    
dp = [0] * (K+1)

for genre, prices in genre_dict.items():
    m = len(prices)
    new_dp =dp[:]
    for t in range(1, min(m, K) + 1):
        total_price = prefix_sums[genre][t] + (t-1) * t
        for j in range(K, t-1, -1):
            new_dp[j] = max(new_dp[j], dp[j-t] + total_price)
    dp = new_dp

print(dp[K])