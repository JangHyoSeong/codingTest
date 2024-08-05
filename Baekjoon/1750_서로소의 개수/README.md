# [1750] 서로소의 개수

### **난이도**
골드 3
## **📝문제**
어떤 수열 S가 주어진다. 이때, 한 개 이상을 선택했을 때, 선택한 수의 최대공약수가 1이 되는 것의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 수열의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에 수열의 각 원소 Si가 주어진다. 같은 수가 들어올 수도 있다. (1 ≤ N ≤ 50, 1 ≤ Si ≤ 100,000)
### **출력**
첫째 줄에 정답을 10,000,003으로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
2
4
3
```

**예제 출력1**

```
3
```

**예제 입력2**

```
1
1
```

**예제 출력2**

```
1
```

**예제 입력3**

```
6
2
5
98872
23298
32872
23111
```

**예제 출력3**


```
45
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:

#### **📝해설**

**알고리즘**
```
1. 정수론
2. 유클리드 호제법
3. DP
```

### **다른 풀이**

```python
from collections import Counter


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


_, *nums = [*open(0)]
dp = Counter()
for i in map(int, nums):
    for j, v in list(dp.items()):
        dp[gcd(i, j)] += v
    dp[i] += 1
print(dp[1] % 10_000_003)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
2changaeng|34016|68|268
#### **📝해설**

```python
from math import gcd

MOD = 10000003

def count_gcd_one_subsets(S):
    N = len(S)

    # 숫자의 최대값이 100000
    max_g = 100000

    # dp 수열 초기화
    dp = [0] * (max_g + 1)
    dp[0] = 1

    # 각 원소 s에 대해
    for s in S:

        # 새로운 dp 배열을 생성
        new_dp = dp[:]

        # dp를 역순으로 순회하면서
        for g in range(max_g, 0, -1):

            if dp[g] > 0:
                # 현재 수와 dp배열의 최대공약수를 찾음
                new_g = gcd(g, s)
                # 최소 공약수 개수를 더해줌
                new_dp[new_g] = (new_dp[new_g] + dp[g]) % MOD
        
        # 나누기
        new_dp[s] = (new_dp[s] + dp[0]) % MOD
        dp = new_dp
    
    return dp[1]

# 입력 받기
N = int(input())
S = [int(input()) for _ in range(N)]

# 결과 출력
result = count_gcd_one_subsets(S)
print(result)
```