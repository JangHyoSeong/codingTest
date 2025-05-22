# [2169] 로봇 조종하기

### **난이도**
골드 2
## **📝문제**
NASA에서는 화성 탐사를 위해 화성에 무선 조종 로봇을 보냈다. 실제 화성의 모습은 굉장히 복잡하지만, 로봇의 메모리가 얼마 안 되기 때문에 지형을 N×M 배열로 단순화 하여 생각하기로 한다.

지형의 고저차의 특성상, 로봇은 움직일 때 배열에서 왼쪽, 오른쪽, 아래쪽으로 이동할 수 있지만, 위쪽으로는 이동할 수 없다. 또한 한 번 탐사한 지역(배열에서 하나의 칸)은 탐사하지 않기로 한다.

각각의 지역은 탐사 가치가 있는데, 로봇을 배열의 왼쪽 위 (1, 1)에서 출발시켜 오른쪽 아래 (N, M)으로 보내려고 한다. 이때, 위의 조건을 만족하면서, 탐사한 지역들의 가치의 합이 최대가 되도록 하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N, M(1≤N, M≤1,000)이 주어진다. 다음 N개의 줄에는 M개의 수로 배열이 주어진다. 배열의 각 수는 절댓값이 100을 넘지 않는 정수이다. 이 값은 그 지역의 가치를 나타낸다.
### **출력**
첫째 줄에 최대 가치의 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15
```

**예제 출력1**

```
319
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = table[0][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + table[0][j]

for i in range(1, N):
    left_to_right = [0] * M
    left_to_right[0] = dp[i-1][0] + table[i][0]

    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + table[i][j]

    right_to_left = [0] * M
    right_to_left[M-1] = dp[i-1][M-1] + table[i][M-1]

    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + table[i][j]
    
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])
    
print(dp[N-1][M-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|94980|1096|Python3|777
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

# 첫 번째 행의 dp 초기화
dp[0][0] = board[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + board[0][j]

# 두 번째 행부터 dp 계산
for i in range(1, N):
    left = [0] * M
    right = [0] * M

    # 왼쪽에서 오른쪽으로 가는 최대 경로 합계 계산
    left[0] = dp[i-1][0] + board[i][0]
    for j in range(1, M):
        left[j] = max(left[j-1], dp[i-1][j]) + board[i][j]

    # 오른쪽에서 왼쪽으로 가는 최대 경로 합계 계산
    right[M-1] = dp[i-1][M-1] + board[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(right[j+1], dp[i-1][j]) + board[i][j]

    # 현재 행의 dp 값 업데이트
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[-1][-1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
terry9508|128752|208|PyPy3|909
#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# DP배열 초기화. dp[i][j] : (i, j) 위치까지의 최대값
dp = [[0] * M for _ in range(N)]

# (0, 0)부터 시작
dp[0][0] = table[0][0]

# 맨 윗줄의 값을 채움
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + table[0][j]

# 2번째 줄부터
for i in range(1, N):

    # 왼쪽에서 오른쪽으로 이동할 때 값
    left_to_right = [0] * M
    left_to_right[0] = dp[i-1][0] + table[i][0]

    # 왼쪽에서 이동해서 온 경우, 위에서 이동해서 온 경우 중 큰값을 고름
    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + table[i][j]

    # 오른쪽도 똑같은 방식으로 구함
    right_to_left = [0] * M
    right_to_left[M-1] = dp[i-1][M-1] + table[i][M-1]

    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + table[i][j]
    
    # 왼쪽에서 이동한 경우, 오른쪽에서 이동한 경우 중 큰 값을 고름
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

# 마지막 위치의 값 출력
print(dp[N-1][M-1])
```