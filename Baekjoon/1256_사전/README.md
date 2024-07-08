# [1256] 사전

### **난이도**
골드2
## **📝문제**
동호와 규완이는 212호에서 문자열에 대해 공부하고 있다. 김진영 조교는 동호와 규완이에게 특별 과제를 주었다. 특별 과제는 특별한 문자열로 이루어 진 사전을 만드는 것이다. 사전에 수록되어 있는 모든 문자열은 N개의 "a"와 M개의 "z"로 이루어져 있다. 그리고 다른 문자는 없다. 사전에는 알파벳 순서대로 수록되어 있다.

규완이는 사전을 완성했지만, 동호는 사전을 완성하지 못했다. 동호는 자신의 과제를 끝내기 위해서 규완이의 사전을 몰래 참조하기로 했다. 동호는 규완이가 자리를 비운 사이에 몰래 사전을 보려고 하기 때문에, 문자열 하나만 찾을 여유밖에 없다.

N과 M이 주어졌을 때, 규완이의 사전에서 K번째 문자열이 무엇인지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 세 정수 N, M, K가 순서대로 주어진다.
1 ≤ N, M ≤ 100  
1 ≤ K ≤ 1,000,000,000
### **출력**
첫째 줄에 규완이의 사전에서 K번째 문자열을 출력한다. 만약 규완이의 사전에 수록되어 있는 문자열의 개수가 K보다 작으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
2 2 2
```

**예제 출력1**

```
azaz
```

**예제 입력2**

```
2 2 6
```

**예제 출력2**

```
zzaa
```

**예제 입력3**

```
10 10 1000000000
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import math

def find_kth_string(N, M, K):
    def binomial(n, k):
        if k > n:
            return 0
        return math.comb(n, k)
    
    if binomial(N + M, M) < K:
        return -1
    
    result = []
    
    while N > 0 and M > 0:
        
        count_a = binomial(N + M - 1, M)
        
        if K <= count_a:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            M -= 1
            K -= count_a
    
    result.extend(['a'] * N)
    result.extend(['z'] * M)
    
    return ''.join(result)

N, M, K = map(int, input().split())
print(find_kth_string(N, M, K))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33240|44|Python3|630
#### **📝해설**

**알고리즘**
```
1. 조합
2. DP
```

### **다른 풀이**

```python
n, m, k = map(int, input().split())


dp = [([1] + [0] * m)  for _ in range(n + 1)]

dp[0] = [0] + [1] * m

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

x, y = n, m
ans = ""

if dp[n][m] < k:
    print(-1)
    exit()

while x != 0 or y != 0:
    if x == 0:
        y -= 1
        ans += "z"
        continue
    if y == 0:
        x -= 1
        ans += "a"
        continue
    
    if dp[x - 1][y] >= k:
        ans += "a"
        x -= 1
    
    else:
        ans += "z"
        
        k -= dp[x - 1][y]
        y -= 1

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
seyeon|31120|40|Python3|595
#### **📝해설**

```python
import math

def find_kth_string(N, M, K):
    
    # 이상 함수를 계산
    def binomial(n, k):
        if k > n:
            return 0
        return math.comb(n, k)
    
    # 문자열 개수가 K보다 작으면 -1 리턴
    if binomial(N + M, M) < K:
        return -1
    
    result = []
    
    # 각 자릿수를 반복
    while N > 0 and M > 0:
        
        # 현재 문자열의 개수를 저장
        count_a = binomial(N + M - 1, M)
        
        # K가 문자열의 개수보다 적다면 A추가
        if K <= count_a:
            result.append('a')
            N -= 1
        
        # 아니라면 Z추가
        else:
            result.append('z')
            M -= 1
            K -= count_a
    
    # 나머지 숫자를 채움
    result.extend(['a'] * N)
    result.extend(['z'] * M)
    
    return ''.join(result)

N, M, K = map(int, input().split())
print(find_kth_string(N, M, K))
```