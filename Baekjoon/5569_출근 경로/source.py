w, h = map(int, input().split())
MOD = 100000

dp = [[[[0]*2 for _ in range(2)] for _ in range(w+1)] for _ in range(h+1)]

if w > 1:
    dp[1][2][0][0] = 1

if h > 1:
    dp[2][1][1][0] = 1

for y in range(1, h+1):
    for x in range(1, w+1):
        for dir in range(2):
            for turn in range(2):
                val = dp[y][x][dir][turn]

                if val == 0:
                    continue

                if dir == 0:
                    if x + 1 <= w:
                        dp[y][x+1][0][0] = (dp[y][x+1][0][0] + val) % MOD
                    
                    if turn == 0 and y + 1 <= h:
                        dp[y+1][x][1][1] = (dp[y+1][x][1][1] + val) % MOD
                    
                else:
                    if y + 1 <= h:
                        dp[y+1][x][1][0] = (dp[y+1][x][1][0] + val) % MOD
                    
                    if turn == 0 and x + 1 <= w:
                        dp[y][x+1][0][1] = (dp[y][x+1][0][1] + val) % MOD

result = (dp[h][w][0][0] + dp[h][w][0][1] + dp[h][w][1][0] + dp[h][w][1][1]) % MOD
print(result)