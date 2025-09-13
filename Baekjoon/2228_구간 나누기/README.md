# [2228] 구간 나누기

### **난이도**
골드 3
## **📝문제**
N(1 ≤ N ≤ 100)개의 수로 이루어진 1차원 배열이 있다. 이 배열에서 M(1 ≤ M ≤ ⌈(N/2)⌉)개의 구간을 선택해서, 구간에 속한 수들의 총 합이 최대가 되도록 하려 한다. 단, 다음의 조건들이 만족되어야 한다.

1. 각 구간은 한 개 이상의 연속된 수들로 이루어진다.
2. 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
3. 정확히 M개의 구간이 있어야 한다. M개 미만이어서는 안 된다.

N개의 수들이 주어졌을 때, 답을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 배열을 이루는 수들이 차례로 주어진다. 배열을 이루는 수들은 -32768 이상 32767 이하의 정수이다.
### **출력**
첫째 줄에 구간에 속한 수들의 총 합의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
6 2
-1
3
1
2
4
-1
```

**예제 출력1**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + arr[i]

dp = [[float('-inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(M+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])

        if j > 0:
            for k in range(1, i+1):
                if k >= 2:
                    dp[i][j] = max(dp[i][j], dp[k-2][j-1] + (prefix[i] - prefix[k-1]))
                elif k == 1 and j == 1:
                    dp[i][j] = max(dp[i][j], prefix[i])

print(dp[N][M])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|152|Python3|599
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
con = [[0]+[-1e9]*m for i in range(n+1)]
notcon = [[0]+[-1e9]*m for i in range(n+1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        notcon[i][j]=max(con[i-1][j], notcon[i-1][j])
        con[i][j]=max(con[i-1][j], notcon[i-1][j-1])+num
print(max(con[n][m], notcon[n][m]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hyoungwoncho|31120|32|Python3|394
#### **📝해설**

```python
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 누적합을 미리 구함
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + arr[i]

# DP배열 선언. dp[i][j]: i번째 수까지 j구간을 정했을 때 최대값
dp = [[float('-inf')] * (M + 1) for _ in range(N + 1)]

# 초기에 아무것도 선택하지 않은 상태
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(M+1):

        # 이전 상태를 그래도 가져옴
        dp[i][j] = max(dp[i][j], dp[i-1][j])

        # 새로운 구간을 만들면서 i에서 끝나는 형태로 추가
        if j > 0:

            # k~i를 구간으로 만듦
            for k in range(1, i+1):
                if k >= 2:
                    dp[i][j] = max(dp[i][j], dp[k-2][j-1] + (prefix[i] - prefix[k-1]))
                elif k == 1 and j == 1:
                    dp[i][j] = max(dp[i][j], prefix[i])

print(dp[N][M])
```