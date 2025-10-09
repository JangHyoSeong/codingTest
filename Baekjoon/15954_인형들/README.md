# [15954] 인형들

### **난이도**
실버 1
## **📝문제**
카카오프렌즈 스토어에서는 N종류의 인형을 팔고 있다. N개의 인형들 중에서는 잘 팔리는 인형과 그렇지 않은 인형들이 섞여 있어서 잘 팔리는 인형은 상대적으로 사람들이 많이 볼 수 있는 곳에 배치하고, 잘 팔리지 않는 인형은 상대적으로 사람들이 적게 볼 수 있는 곳에 배치한다. 그러므로 배치된 곳이 가까운 두 인형은 상대적으로 판매량이 비슷하다고 할 수 있다.

좋은 배치를 정하기 위해서 어느 날, 여러 명의 사람들을 대상으로 인형의 선호도를 조사하였다. 조사 결과 각 인형에 대해서 선호하는 사람의 수를 모두 구하였고, 그에 따라 인형의 배치를 정하려고 한다.

카카오프렌즈 스토어를 관리하는 브라이언은 어떠한 특정한 곳에 인형들을 배치하고자 하는데, 그곳에 인형들을 선택하는 방법은 다음과 같다:

- 먼저 비슷한 인형이 가깝게 위치하도록 서로 다른 N개의 인형을 종류당 한 개씩 일렬로 배치한다.
- 그 후, 선호하는 사람의 수의 표준편차가 최소가 되는, K개 이상의 연속된 위치에 있는 인형들을 선택하여 그들을 같은 곳에 배치한다.

위의 방법으로 인형들을 선택했을 때, 선택된 인형들의 선호하는 사람의 수의 표준편차를 구하여라.

N개의 수 a1, a2, …, aN이 주어져 있을 때, 통계학에서 (산술) 평균은 (a1 + a2 + … + aN) / N 으로 정의한다. 이를 m으로 정의하자. 또한, 분산은 ((a1 - m)2 + (a2 - m)2 + … + (aN - m)2) / N으로 정의하고, 표준 편차는 분산의 음이 아닌 제곱근으로 정의한다.
### **입력**
첫 번째 줄에 N과 K가 주어진다. N은 1 이상 500 이하의 정수이고, K는 1 이상 N 이하의 정수이다.

두 번째 줄에는 N개의 정수가 입력되며, 이는 인형이 일렬로 나열된 순서대로 인형을 선호하는 사람의 수이다. 각 수는 모두 106 이하의 음이 아닌 정수이다.
### **출력**
선택된 인형들을 선호하는 사람의 수의 표준 편차를 출력한다. 출력한 결과와 실제 답을 비교하였을 때의 상대/절대 오차가 10-6 이하인 경우에만 정답으로 인정한다.
### **예제입출력**

**예제 입력1**

```
5 3
1 2 3 4 5
```

**예제 출력1**

```
0.81649658092
```

**예제 입력2**

```
10 3
1 4 1 5 9 2 6 5 3 5
```

**예제 출력2**

```
0.94280904158
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import math

N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

min_std = float('inf')

for length in range(K, N + 1):
    for start in range(0, N - length + 1):
        end = start + length
        now_sum = prefix_sum[end] - prefix_sum[start]
        now_avg = now_sum / length

        now_var_sum = 0
        for j in range(start, end):
            now_var_sum += (arr[j] - now_avg) ** 2
        now_var = now_var_sum / length
        now_std = math.sqrt(now_var)

        if now_std < min_std:
            min_std = now_std

print(min_std)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110760|336|PyPy3|670
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
from sys import stdin
from math import sqrt

input = stdin.readline
n, k = map(int, input().split())
dolls = list(map(int, input().split()))

s = [0 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] = s[i - 1] + dolls[i - 1]
    e[i] = e[i - 1] + dolls[i - 1] ** 2

def calculate(start, end):
    length = end - start
    squared_val = e[end] - e[start]
    sum_val = s[end] - s[start]
    return (length * squared_val - sum_val ** 2) / length ** 2


result = float("inf")
# i는 인형의 시작 지점
for start in range(n - k + 1):
    # j는 k개 이상만큼
    for end in range(start + k, n + 1):
        v = calculate(start, end)
        result = min(result, v)

print(sqrt(result))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jyajoo|33240|108|Python3|730
#### **📝해설**

```python
import math

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 최소 표준편차
min_std = float('inf')

# 현재 확인할 구간의 길이
for length in range(K, N + 1):

    # 확인할 구간의 시작점
    for start in range(0, N - length + 1):

        # 끝점
        end = start + length

        # 현재 합
        now_sum = prefix_sum[end] - prefix_sum[start]

        # 현재 평균
        now_avg = now_sum / length

        # 현재 분산
        now_var_sum = 0
        for j in range(start, end):
            now_var_sum += (arr[j] - now_avg) ** 2
        now_var = now_var_sum / length

        # 표준편차
        now_std = math.sqrt(now_var)

        if now_std < min_std:
            min_std = now_std

print(min_std)
```