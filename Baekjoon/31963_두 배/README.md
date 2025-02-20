# [31963] 두 배

### **난이도**
골드 4
## **📝문제**
길이 
$N$인 양의 정수열 
$A_1, \dots , A_N$이 주어진다. 이 수열을 오름차순으로 만들려 한다. 수열 
$A_1, \dots , A_N$이 오름차순이라는 것은, 각 
$i$ (
$1 ≤ i ≤ N - 1$)에 대해 
$A_i ≤ A_{i+1}$이라는 것이다.

수열 
$A$를 오름차순으로 만들기 위해, 수열 
$A$에 다음 연산을 몇 번이든 반복해서 적용할 수 있다.

어떤 
$i$ (
$1 ≤ i ≤ N$)에 대해 
$A_i$에 
$2$를 곱한다.
연산을 최소 횟수로 적용해서 
$A$를 오름차순으로 만들고 싶다. 이때, 최소 횟수를 구하라.
### **입력**
첫 번째 줄에 
$N$이 주어진다.

두 번째 줄에 
$A_1, \dots , A_N$이 주어진다.
### **출력**
첫 번째 줄에 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
3 1 4 1 5
```

**예제 출력1**

```
4
```

**예제 입력2**

```
5
3 1 5 1 5
```

**예제 출력2**

```
6
```

**예제 입력3**

```
5
1 2 3 4 5
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
import math

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
count_arr = [0] * N

count = 0
for i in range(1, N):
    ratio = math.ceil(math.log2(arr[i-1] / arr[i])) + count_arr[i-1]
    if ratio > 0:
        count_arr[i] = max(0, ratio)
        count += count_arr[i]

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|157608|180|PyPy3|343
#### **📝해설**

**알고리즘**
```
1. 수학
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
from math import log2,ceil
input = sys.stdin.readline
n = int(input())
sq = [log2(int(x)) for x in input().split()]
rst = 0
prv = 0
for i in range(1,n):
    prv = max(ceil(sq[i-1]-sq[i]) + prv,0)
    rst += prv
print(rst)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jun83|134104|156|PyPy3|232
#### **📝해설**

```python
import sys
import math

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 몇번 곱했는지 저장할 리스트
count_arr = [0] * N

# 총 횟수
count = 0

# 숫자를 순회하면서
for i in range(1, N):

    # 앞의 숫자에 2를 곱해야 하는 횟수를 계산
    ratio = math.ceil(math.log2(arr[i-1] / arr[i])) + count_arr[i-1]

    # 앞의 숫자가 더 크다면
    if ratio > 0:
        # 2를 곱할 비율을 리스트에 저장
        count_arr[i] = max(0, ratio)

        # 총 횟수 증가
        count += count_arr[i]

print(count)
```