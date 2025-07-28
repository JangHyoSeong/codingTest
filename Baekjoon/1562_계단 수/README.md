# [1562] 계단 수

### **난이도**
골드 1
## **📝문제**
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 0으로 시작하는 수는 계단수가 아니다.
### **입력**
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
10
```

**예제 출력1**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
MOD = 1000000000

N = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, N+1):
    for digit in range(10):
        for bit in range(1 << 10):
            if digit > 0:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit - 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD
            
            if digit < 9:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit + 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD

result = 0
for i in range(10):
    result = (result + dp[N][i][(1 << 10) - 1]) % MOD

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116588|128|PyPy3|705
#### **📝해설**

**알고리즘**
```
1. DP
2. 비트마스킹
```

### **다른 풀이**

```python
N = int(input())
dp = [[[0]*4 for _ in range(10)] for _ in range(100)]
dp[0][0][1] = dp[0][9][2] = 1
for i in range(1, 9):
    dp[0][i][0] = 1
for i in range(N-1):
    for visited in range(4):
        dp[i+1][0][visited|1] += dp[i][1][visited]
        dp[i+1][9][visited|2] += dp[i][8][visited]
        for j in range(1, 9):
            dp[i+1][j][visited] += dp[i][j-1][visited]+dp[i][j+1][visited]
res = 0
for i in range(1, 10):
    res = (res+dp[N-1][i][-1])%1000000000
print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|30616|36|Python3|483
#### **📝해설**

```python
MOD = 1000000000

N = int(input())

# dp배열
# dp[length][digit][bit] : length만큼 길이의 숫자이고, digit으로 끝나며, bit에 포함되는 숫자를 사용한 경우의 수
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]

# 초기 정보 삽입
for i in range(1, 10):
    dp[1][i][1 << i] = 1

# 길이가 2부터 채워나감
for length in range(2, N+1):

    # 마지막 숫자를 모두 사용하면서
    for digit in range(10):

        # 모든 비트를 검사
        for bit in range(1 << 10):

            # DP배열을 채움
            if digit > 0:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit - 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD
            
            if digit < 9:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit + 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD

# 0~9까지 모든 숫자를 사용한 경우, 결과에 더해서 출력
result = 0
for i in range(10):
    result = (result + dp[N][i][(1 << 10) - 1]) % MOD

print(result)
```