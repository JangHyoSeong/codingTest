# [5569] 출근 경로

### **난이도**
골드 4
## **📝문제**
상근이가 사는 도시는 남북 방향으로 도로가 w개, 동서 방향으로 도로가 h개 있다. 

남북 방향 도로는 서쪽부터 순서대로 번호가 1, 2, ..., w로 매겨져 있다. 또, 동서 방향 도로는 남쪽부터 순서대로 번호가 1, 2, ..., h로 매겨져 있다. 서쪽에서 i번째 남북 방향 도로와 남쪽에서 j번째 동서 방향 도로가 만나는 교차로는 (i, j)이다.

상근이는 교차로 (1, 1)에 살고 있고, 교차로 (w, h)에 있는 회사에 차로 다니고 있다. 차는 도로로만 이동할 수 있다. 상근이는 회사에 최대한 빨리 가기 위해서, 동쪽 또는 북쪽으로만 이동할 수 있다. 또, 이 도시는 교통 사고를 줄이기 위해서 교차로를 돈 차량은 그 다음 교차로에서 다시 방향을 바꿀 수 없다. 즉, 교차로에서 방향을 바꾼 후, 1 블록만 이동한 후 다시 방향을 바꿀 수 없다.

상근이가 회사에 출근할 수 있는 경로의 수는 몇 가지 일까?

w와 h가 주어졌을 때, 가능한 출근 경로의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 w와 h가 주어진다. (2 ≤ w, h ≤ 100)
### **출력**
첫째 줄에 상근이가 출근할 수 있는 경로의 개수를 100000로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
```

**예제 출력1**

```
5
```

**예제 입력2**

```
15 15
```

**예제 출력2**

```
43688
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
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
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36504|76|Python3|1083
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
mod = int(1e5)

n,m = map(int,input().split())
dp = [[[0]*4 for _ in range(m)] for _ in range(n)]
for i in range(n):
    dp[i][0][0] = 1
for j in range(m):
    dp[0][j][1] = 1

for i in range(1,n):
    for j in range(1,m):
        dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][2])%mod
        dp[i][j][1] = (dp[i][j-1][1] + dp[i][j-1][3])%mod
        dp[i][j][2] = dp[i-1][j][1]
        dp[i][j][3] = dp[i][j-1][0]

print(sum(dp[-1][-1])%mod)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jjkmk1013|34456|44|Python3|438
#### **📝해설**

```python
w, h = map(int, input().split())
MOD = 100000

# DP배열 선언
# dp[y][x][dir][turn] : (x, y) : 좌표, dir : 현재 이동 방향(0: 동쪽, 1: 서쪽), turn: 이전 교차로에서 방향을 바꿨는지 여부
dp = [[[[0]*2 for _ in range(2)] for _ in range(w+1)] for _ in range(h+1)]

# 초기 위치는 경우의 수가 하나
if w > 1:
    dp[1][2][0][0] = 1

if h > 1:
    dp[2][1][1][0] = 1

# x, y좌표에 대해 모두 순회하면서(서쪽 아래부터)
for y in range(1, h+1):
    for x in range(1, w+1):

        # 모든 방향, 방향전환 여부도 검사
        for dir in range(2):
            for turn in range(2):

                # 현재 dp배열 값
                val = dp[y][x][dir][turn]

                # 한번도 방문하지 않은 곳이라면(방문이 불가능한 장소) 넘김
                if val == 0:
                    continue
                
                # 동쪽으로 진행할 때
                if dir == 0:

                    # 동쪽으로 더 이동 가능하다면
                    if x + 1 <= w:

                        # dp배열 갱신
                        dp[y][x+1][0][0] = (dp[y][x+1][0][0] + val) % MOD
                    
                    # 방향전환이 가능하고, 북쪽으로 더 이동가능하다면
                    if turn == 0 and y + 1 <= h:

                        # 갱신
                        dp[y+1][x][1][1] = (dp[y+1][x][1][1] + val) % MOD
                
                # 북쪽으로 진행할 때
                else:

                    # 이동 가능하다면
                    if y + 1 <= h:
                        dp[y+1][x][1][0] = (dp[y+1][x][1][0] + val) % MOD
                    
                    # 방향전환이 가능하다면
                    if turn == 0 and x + 1 <= w:
                        dp[y][x+1][0][1] = (dp[y][x+1][0][1] + val) % MOD

# 결과값을 모두 더하고 출력
result = (dp[h][w][0][0] + dp[h][w][0][1] + dp[h][w][1][0] + dp[h][w][1][1]) % MOD
print(result)
```