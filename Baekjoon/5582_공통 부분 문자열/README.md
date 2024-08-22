# [5582] 공통 부분 문자열

### **난이도**
골드 5
## **📝문제**
두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.
### **입력**
첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.
### **출력**
첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
ABRACADABRA
ECADADABRBCRDARA
```

**예제 출력1**

```
5
```

**예제 입력2**

```
UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV
```

**예제 출력2**

```
0
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
str1 = list(input())
str2 = list(input())
N, M = len(str1), len(str2)
max_len = 0

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if str1[i] == str2[j]:
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(dp[i][j], max_len)

print(max_len)

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|236384|496|PyPy3|419
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
text1 = input()
text2 = input()

max_cnt = 0

for i in range(len(text1) + len(text2) - 1):
    cnt = 0
    t1 = 0; t2 = len(text2) - 1 - i
    if t2 < 0: t1 -= t2; t2 = 0
    while t1 < len(text1) and t2 < len(text2):
        if text1[t1] == text2[t2]: cnt += 1
        else: 
            max_cnt = max(max_cnt, cnt)
            cnt = 0
        t1 += 1; t2 += 1
    else:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
eypk5683|115226|232|PyPy3|423
#### **📝해설**

```python
str1 = list(input())
str2 = list(input())
N, M = len(str1), len(str2)
max_len = 0

# DP 테이블 초기화
dp = [[0] * M for _ in range(N)]

# N^2 반복을 수행하며
for i in range(N):
    for j in range(M):

        # 숫자가 같다면
        if str1[i] == str2[j]:
          # dp 테이블을 갱신
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(dp[i][j], max_len)

print(max_len)
```