# [2758] 로또

### **난이도**
골드 4
## **📝문제**
선영이는 매주 엄청난 돈을 로또에 투자한다. 선영이가 하는 로또는 1부터 m까지 숫자 중에 n개의 수를 고르는 로또이다.

이렇게 열심히 로또를 하는데, 아직까지 한 번도 당첨되지 않은 이유는 수를 고를 때 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.

예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.

- 1 2 4 8
- 1 2 4 9
- 1 2 4 10
- 1 2 5 10

따라서 선영이는 로또를 4개 산다. 

선영이는 돈이 엄청나게 많기 때문에, 수를 고르는 방법의 수 만큼 로또를 구매하며, 같은 방법으로 2장이상 구매하지 않는다.

n과 m이 주어졌을 때, 선영이가 구매하는 로또의 개수를 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 n과 m으로 이루어져 있다.
### **출력**
각 테스트 케이스에 대해 선영이가 로또를 몇 개나 구매하는지 한 줄에 하나씩 출력한다.
### **예제입출력**

**예제 입력1**

```
1
4 10
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

cases = [list(map(int, input().split())) for _ in range(T)]

max_n = max(case[0] for case in cases)
max_m = max(case[1] for case in cases)

dp = [[0] * (max_m + 1) for _ in range(max_n+1)]

for j in range(1, max_m + 1):
    dp[1][j] = 1

for i in range(2, max_n + 1):
    for j in range(1, max_m + 1):
        for k in range(1, j // 2 + 1):
            dp[i][j] += dp[i-1][k]

answer = [[0] * (max_m + 1) for _ in range(max_n + 1)]
for i in range(1, max_n + 1):
    for j in range(1, max_m + 1):
        answer[i][j] = answer[i][j - 1] + dp[i][j]

for n, m in cases:
    print(answer[n][m])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34456|1620|Python3|608
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
from sys import stdin

def main():
    dp = [[0]*(2001) for _ in range(11)]
    dp[0] = [1]*2001
    for i in range(1, 11):
        for j in range(1, 2001):
            dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
    for _ in range(int(stdin.readline())):
        n, m = map(int, stdin.readline().split())
        print(dp[n][m])

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dyddn2015|32140|32|Python3|331
#### **📝해설**

```python
T = int(input())

cases = [list(map(int, input().split())) for _ in range(T)]

# n, m의 최대값을 구함
max_n = max(case[0] for case in cases)
max_m = max(case[1] for case in cases)

# dp[i][j] : 길이가 i이고 마지막 수가 j인 수열의 개수
dp = [[0] * (max_m + 1) for _ in range(max_n+1)]

# 초기값
for j in range(1, max_m + 1):
    dp[1][j] = 1

# 이후 dp배열을 채움
for i in range(2, max_n + 1):
    for j in range(1, max_m + 1):
        for k in range(1, j // 2 + 1):
            dp[i][j] += dp[i-1][k]

# 정답의 개수를 누적합으로 미리 구함
answer = [[0] * (max_m + 1) for _ in range(max_n + 1)]
for i in range(1, max_n + 1):
    for j in range(1, max_m + 1):
        answer[i][j] = answer[i][j - 1] + dp[i][j]

# 출력
for n, m in cases:
    print(answer[n][m])
```