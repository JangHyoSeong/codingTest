# [17404] RGB거리 2

### **난이도**
골드 4
## **📝문제**
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
### **입력**
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
3
26 40 83
49 60 57
13 89 99
```

**예제 출력1**

```
110
```

**예제 입력2**

```
3
1 100 100
100 1 100
100 100 1
```

**예제 출력2**

```
3
```

**예제 입력3**

```
3
1 100 100
100 100 100
1 100 100
```

**예제 출력3**

```
201
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = float('inf')
result = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    
    dp[0][first_color] = costs[0][first_color]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for last_color in range(3):
        if first_color != last_color:
            result = min(result, dp[N-1][last_color])

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|40|Python3|631
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

n = int(input())

costList = []

for _ in range(n):
    costList.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n)]

answer = sys.maxsize

for i in range(3):
    for j in range(3):
        dp[0][j] = sys.maxsize
    dp[0][i] = costList[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + costList[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + costList[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + costList[j][2]
    
    for j in range(3):
        if i != j:
            answer = min(answer, dp[n - 1][j])
            #print(dp[n - 1][j], i, j)

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sk3456|31120|32|Python3|686
#### **📝해설**

```python
import sys

# 입력받기
N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 최소값을 구하기 위해 큰 값을 하나 선정
INF = float('inf')
result = INF

# 시작 색깔 하나하나 모두 검사
for first_color in range(3):
    # dp배열 선언 (dp[i][j] i색깔을 j집까지 칠했을 때 최소비용)
    dp = [[INF] * 3 for _ in range(N)]
    
    # 초기 정보
    dp[0][first_color] = costs[0][first_color]
    
    # 색깔을 칠함
    for i in range(1, N):
        # 각각 이전의 집과 다른 색깔을 칠했을 때 최소비용
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 색깔은 첫번째 색깔과 달라야 하기에 따로처리
    for last_color in range(3):
        if first_color != last_color:
            result = min(result, dp[N-1][last_color])

# 결과
print(result)
```