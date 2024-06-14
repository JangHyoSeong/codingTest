# [1932] 정수 삼각형

### **난이도**
실버 1
## **📝문제**
```
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
```
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
### **입력**
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
### **출력**
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```

**예제 출력1**

```
30
```

### **출처**
Olympiad > International Olympiad in Informatics > IOI 1994 > Day 1 1번

Olympiad > USA Computing Olympiad > 2005-2006 Season > USACO December 2005 Contest > Bronze ?번

Olympiad > USA Computing Olympiad > 1999-2000 Season > USACO Fall 1999 Contest > Gold 1번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (i+1) for i in range(N)]

dp[0][0] = triangle[0][0]

if N == 1:
    print(triangle[0][0])
    exit()

dp[1][0] = dp[0][0] + triangle[1][0]
dp[1][1] = dp[0][0] + triangle[1][1]

if N == 2:
    print(max(dp[1]))
    exit()

for i in range(2, N):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[N-1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|40628|124|Python3|560
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N = int(input())
prev = [*map(int, input().split())]

for i in range(1, N):
  nums = [*map(int, input().split())]
  b = [max(prev[j-1], prev[j])+nums[j] for j in range(1, i)]
  prev = [prev[0]+nums[0], *b, prev[-1]+nums[-1]]

print(max(prev))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
amgkd9|30616|84|Python3|281
#### **📝해설**

```python
N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

# 삼각형의 크기만큼 dp 배열 선언
dp = [[0] * (i+1) for i in range(N)]

# 초기값 설정
dp[0][0] = triangle[0][0]

# N == 1인 경우, 답이 하나
if N == 1:
    print(triangle[0][0])
    exit()

# 가장 왼쪽과 오른쪽의 경우 더하는 경우의 수가 하니이기 때문에 미리 처리
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

# 가운데 숫자들의 DP를 구함
for i in range(1, N):
    for j in range(1, i):
        # 위의 두 수 중에서 큰 수를 골라서 더함
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

# 마지막 줄에서 최대값을 출력
print(max(dp[N-1]))
```