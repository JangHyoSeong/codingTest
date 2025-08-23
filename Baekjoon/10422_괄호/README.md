# [10422] 괄호

### **난이도**
골드 4
## **📝문제**
‘(‘, ‘)’ 문자로만 이루어진 문자열을 괄호 문자열이라 한다. 올바른 괄호 문자열이란 다음과 같이 정의된다. ()는 올바른 괄호 문자열이다. S가 올바른 괄호 문자열이라면, (S)도 올바른 괄호 문자열이다. S와 T가 올바른 괄호 문자열이라면, 두 문자열을 이어 붙인 ST도 올바른 괄호 문자열이다. (()())()은 올바른 괄호 문자열이지만 (()은 올바른 괄호 문자열이 아니다. 괄호 문자열이 주어졌을 때 올바른 괄호 문자열인지 확인하는 방법은 여러 가지가 있다.

하지만 우리가 궁금한 것은 길이가 L인 올바른 괄호 문자열의 개수이다. 길이 L이 주어졌을 때 길이가 L인 서로 다른 올바른 괄호 문자열의 개수를 출력하는 프로그램을 만들어 보자.
### **입력**
첫 번째 줄에 테스트케이스의 개수를 나타내는 T (1 ≤ T ≤ 100)가 주어진다. 두 번째 줄부터 각 테스트케이스마다 괄호 문자열의 길이를 나타내는 L이 주어진다. (1 ≤ L ≤ 5000) 
### **출력**
각 테스트 케이스에 대해 길이가 L인 올바른 괄호 문자열의 개수를 1,000,000,007로 나눈 나머지를 출력하시오.
### **예제입출력**

**예제 입력1**

```
3
1
2
4
```

**예제 출력1**

```
0
1
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
MOD = 1000000007

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers) // 2
dp = [0] * (max_num + 1)

dp[0] = 1
for i in range(1, max_num + 1):
    for j in range(i):
        dp[i] = (dp[i] + dp[j] * dp[i-1-j]) % MOD 

for num in numbers:
    print(0 if num % 2 else dp[num // 2])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|1064|Python3|311
#### **📝해설**

**알고리즘**
```
1. 카탈란 수
2. DP
```

### **다른 풀이**

```python
import sys

MOD = 1_000_000_007

def precompute_fact(max_n):
    # 팩토리얼과 역팩토리얼을 0..max_n 까지 전처리
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    ifact = [1] * (max_n + 1)
    ifact[max_n] = pow(fact[max_n], MOD - 2, MOD)  # 페르마 소정리로 역원
    for i in range(max_n, 0, -1):
        ifact[i - 1] = ifact[i] * i % MOD
    return fact, ifact

def nCr(n, r, fact, ifact):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD

def catalan(n, fact, ifact):
    # Cn = comb(2n, n) / (n+1)
    return nCr(2*n, n, fact, ifact) * pow(n + 1, MOD - 2, MOD) % MOD

def main():
    data = sys.stdin.read().strip().split()
    T = int(data[0])
    Ls = list(map(int, data[1:1+T]))
    # 전처리 범위: 최대 L에 대해 2n = L 이므로 팩토리얼은 L_max 까지
    L_max = max(Ls)
    max_fact = L_max  # = 2 * (L_max // 2)
    fact, ifact = precompute_fact(max_fact)

    out_lines = []
    for L in Ls:
        if L % 2 == 1:
            out_lines.append("0")
        else:
            n = L // 2
            out_lines.append(str(catalan(n, fact, ifact)))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wjdalsdk70|33432|36|Python3|1271
#### **📝해설**

```python
MOD = 1000000007

'''
카탈란 수와 관련된 문제
이는 카탈란 수를 DP로 구함
'''

T = int(input())
numbers = [int(input()) for _ in range(T)]

# DP배열의 길이를 잡기 위한 최대값
# 홀수는 어차피 0이니까 고려하지 않고 괄호 한 쌍을 기준
max_num = max(numbers) // 2
dp = [0] * (max_num + 1)

dp[0] = 1

# 괄호가 1쌍에서부터 최대값까지 일떄
for i in range(1, max_num + 1):

    # DP 배열 채우기
    for j in range(i):

        # 기존 갯수 + 괄호가 j쌍일 때 * 뒤의 괄호는 i-1-j쌍
        dp[i] = (dp[i] + dp[j] * dp[i-1-j]) % MOD 

# 출력
for num in numbers:
    print(0 if num % 2 else dp[num // 2])
```