# [15990] 1, 2, 3 더하기 5

### **난이도**
실버 1
## **📝문제**
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

1+2+1
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.
### **출력**
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
4
7
10
```

**예제 출력1**

```
3
9
27
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
MOD = 1000000009

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_n = max(numbers)

# dp[i][j]: i를 만들 때 마지막에 사용한 수가 j인 경우의 수
dp = [[0] * 4 for _ in range(max_n + 1)]

if max_n >= 1:
    dp[1][1] = 1

if max_n >= 2:
    dp[2][2] = 1

if max_n >= 3:
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

for i in range(4, max_n + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

for n in numbers:
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|52648|292|Python3|604
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
MOD = 1000000009

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_n = max(numbers)

# dp[i][j]: i를 만들 때 마지막에 사용한 수가 j인 경우의 수
dp = [[0] * 4 for _ in range(max_n + 1)]

# 초기값 설정
if max_n >= 1:
    dp[1][1] = 1

if max_n >= 2:
    dp[2][2] = 1

if max_n >= 3:
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

# 4부터 시작
for i in range(4, max_n + 1):
    # 1을 더하는 경우, 앞의 숫자가 2, 3으로 끝난 경우에만 더할 수 있음
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    # 2, 3도 동일
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

for n in numbers:
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)
```