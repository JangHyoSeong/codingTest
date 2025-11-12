# [14002] 가장 긴 증가하는 부분 수열 4

### **난이도**
골드 4
## **📝문제**
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
### **입력**
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
### **출력**
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.
### **예제입출력**

**예제 입력1**

```
6
10 20 10 30 20 50
```

**예제 출력1**

```
4
10 20 30 50
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

max_len = max(dp)
index = dp.index(max_len)

lis = []
while index != -1:
    lis.append(arr[index])
    index = prev[index]

lis.reverse()
print(max_len)
print(" ".join(map(str, lis)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|112|Python3|417
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def find_idx(val):
    ret = 0
    i = 0
    f = len(lis)
    while i <= f:
        mid = (i+f)//2
        if lis[mid] >= val:
            ret = mid
            f = mid - 1
        else:
            i = mid + 1
    return ret

N = int(input())
A = list(map(int, input().split()))
B = [1]
#C는 count의 약자
lis = [A[0]]
for i in range(1,N):
    if A[i] > lis[-1]:
        lis.append(A[i])
        B.append(len(lis))
    else:
        tmp = find_idx(A[i])
        lis[tmp] = A[i]
        B.append(tmp+1)
tmp_max = max(B)
C = []
for i in range(len(B)-1, -1, -1):
    if tmp_max == 0:
        break
    if B[i] == tmp_max:
        C.append(A[i])
        tmp_max -= 1
print(len(lis))        
print(*C[::-1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
spakr_1130|30616|36|Python3|745
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# dp배열 선언. dp[i] : i번째 숫자에서 LIS의 길이
dp = [1] * N

# 해당 인덱스 직전의 숫자의 인덱스를 저장
prev = [-1] * N

# DP배열 작성
for i in range(N):
    for j in range(i):

        # 이전 숫자보다 크고, LIS 길이가 긴 경우 갱신
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

# 출력
max_len = max(dp)
index = dp.index(max_len)

lis = []
while index != -1:
    lis.append(arr[index])
    index = prev[index]

lis.reverse()
print(max_len)
print(" ".join(map(str, lis)))
```