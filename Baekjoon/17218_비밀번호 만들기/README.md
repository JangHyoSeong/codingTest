# [17218] 비밀번호 만들기

### **난이도**
골드 4
## **📝문제**
최근 들어 개인정보 유출에 대한 뉴스를 많이 본 수형이는 한 사이트의 비밀번호가 유출 되더라도 다른 사이트에서 똑같은 비밀번호로 접속할 수 없도록 사이트마다 비밀번호를 다르게 설정하기로 다짐했다. 많이 고민한 결과 수형이는 눈을 감고 키보드를 막 쳐서 나온 두 문자열에서 공통으로 존재하는 가장 긴 부분 문자열을 비밀번호로 하기로 하였다. 수형이가 눈을 감고 만든 두 문자열이 주어졌을 때 비밀번호를 만드는 프로그램을 만들어보자.
### **입력**
첫째 줄과 둘째 줄에 수형이가 눈을 감고 만든 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 길이는 최대 40자이다. 빈 문자열은 주어지지 않는다. 가장 긴 부분 문자열은 반드시 하나만 존재한다.
### **출력**
첫 번째 줄에 입력으로 주어진 두 문자열로 만든 비밀번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
AUTABBEHNSA
BCUAMEFKAJNA
```

**예제 출력1**

```
UAENA
```

**예제 입력2**

```
SETAPPLE 
EATMANY
```

**예제 출력2**

```
ETA
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
A = input()
B = input()

len_A = len(A)
len_B = len(B)

dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len_A, len_B
answer = []

while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        answer.append(A[i-1])
        i -= 1
        j -= 1
    
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

answer.reverse()
print(''.join(answer))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|567
#### **📝해설**

**알고리즘**
```
1. DP
2. 최장 공통 부분 수열
```

### **다른 풀이**

```python
from sys import stdin

def main():
    A, B = stdin.readline().strip(), stdin.readline().strip()
    lenA, lenB = len(A), len(B)
    dp = [[0]*(lenB+1) for _ in range(lenA+1)]
    for a in range(lenA):
        for b in range(lenB):
            dp[a+1][b+1] = dp[a][b]+1 if A[a]==B[b] else max(dp[a+1][b], dp[a][b+1])
    a, b = lenA, lenB
    reversed_answer = ""
    while dp[a][b]>0:
        if dp[a-1][b]==dp[a][b]:
            a -= 1
        elif dp[a][b-1]==dp[a][b]:
            b -= 1
        else:
            a -= 1
            b -= 1
            reversed_answer += A[a]
    print(reversed_answer[::-1])

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dyddn2015|31120|28|Python3|620
#### **📝해설**

```python
A = input()
B = input()

len_A = len(A)
len_B = len(B)

# DP배열. dp[i][j] : A문자 i번째 까지와 B문자 j번째 까지 비교했을 때 최장부분공통수열의 길이
dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

# dp테이블 채우기
for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):

        # 현재 문자가 같다면 전에꺼 + 1
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        
        # 다르다면 전에꺼 중 큰거를 고름
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len_A, len_B
answer = []

# 역추적으로 정답을 만듦
while i > 0 and j > 0:

    # 현재 같은 문자라면
    if A[i-1] == B[j-1]:
        # 정답에 추가
        answer.append(A[i-1])
        i -= 1
        j -= 1
    
    # 문자가 다를 때, dp 값이 큰 수를 줄임
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

# 역순으로 저장했으니 뒤집음
answer.reverse()
print(''.join(answer))
```