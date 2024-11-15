# [14430] 자원 캐기

### **난이도**
실버 2
## **📝문제**
인류의 차세대 인공지능 자원 캐기 로봇인 WOOK은 인간 대신 자원을 캐는 로봇이다. WOOK은 언제나 제한된 범위 내에서 자원을 탐색하며, 왼쪽 위 (1, 1)부터 오른쪽 아래 (N, M)까지 자원을 탐색한다. WOOK은 한 번에 오른쪽 또는 아래쪽으로 한 칸 이동할 수 있으며, 그 외의 방향으로 움직이는 것은 불가능하다. WOOK은 자신이 위치한 (x, y)에 자원이 있는 경우에만 해당 자원을 채취할 수 있다. WOOK이 탐사할 영역에 대한 정보가 주어질 때, WOOK이 탐색할 수 있는 자원의 최대 숫자를 구해라!
### **입력**
첫째 줄에 WOOK이 탐사할 영역의 세로길이 N(1≤N≤300)과 가로길이 M(1≤M≤300)이 주어진다. 그 다음 N행 M열에 걸쳐 탐사영역에 대한 정보가 주어진다. 숫자는 공백으로 구분된다. (자원은 1, 빈 땅은 0으로 표시된다)
### **출력**
WOOK이 수집할 수 있는 최대 광석의 개수를 출력하라.
### **예제입출력**

**예제 입력1**

```
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = table[0][0]

for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    if table[i][0]:
        dp[i][0] += 1

for i in range(1, M):
    dp[0][i] += dp[0][i-1]
    if table[0][i]:
        dp[0][i] += 1

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if table[i][j]:
            dp[i][j] += 1
print(dp[N-1][M-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|92|Python3|499
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# DP배열. 각 위치에서 얻을 수 있는 최대자원
dp = [[0] * M for _ in range(N)]
dp[0][0] = table[0][0]


# 초기값 삽입
for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    if table[i][0]:
        dp[i][0] += 1

for i in range(1, M):
    dp[0][i] += dp[0][i-1]
    if table[0][i]:
        dp[0][i] += 1

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if table[i][j]:
            dp[i][j] += 1
print(dp[N-1][M-1])
```