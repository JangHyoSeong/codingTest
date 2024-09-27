# [9251] LCS

### **난이도**
골드 5
## **📝문제**
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
### **입력**
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
### **출력**
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
ACAYKP
CAPCAK
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
str_1 = input()
str_2 = input()

n = len(str_1)
m = len(str_2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str_1[i-1] == str_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|55708|484|Python3|314
#### **📝해설**

**알고리즘**
```
1. DP
2. LCS
```

#### **📝해설**

```python
str_1 = input()
str_2 = input()

n = len(str_1)
m = len(str_2)

# 이차원 배열로 DP배열 선언
dp = [[0] * (m+1) for _ in range(n+1)]


# 문자열을 모두 순회하면서
for i in range(1, n+1):
    for j in range(1, m+1):

      # 현재 인덱스에서 같다면, 전의 인덱스 + 1
        if str_1[i-1] == str_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        # 아니라면 전의 인덱스 중 최대값을 고름
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
```