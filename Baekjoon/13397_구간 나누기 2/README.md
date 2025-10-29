# [13397] 구간 나누기 2

### **난이도**
골드 4
## **📝문제**
N개의 수로 이루어진 1차원 배열이 있다. 이 배열을 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 하려고 한다. 구간은 다음과 같은 조건을 만족해야 한다.

1. 하나의 구간은 하나 이상의 연속된 수들로 이루어져 있다.
2. 배열의 각 수는 모두 하나의 구간에 포함되어 있어야 한다.

구간의 점수란 구간에 속한 수의 최댓값과 최솟값의 차이이다.

예를 들어, 배열이 [1, 5, 4, 6, 2, 1, 3, 7] 이고, M = 3인 경우가 있다.

이때, [1, 5], [4, 6, 2], [1, 3, 7]로 구간을 나누면 각 구간의 점수는 4, 4, 6점이 된다. 이때, 최댓값은 6점이다.

만약, [1, 5, 4], [6, 2, 1], [3, 7]로 구간을 나누었다면, 각 구간의 점수는 4, 5, 4점이 되고, 이때 최댓값은 5점이 된다.

두 경우 중에서 최댓값이 최소인 것은 5점인 것이고, 5점보다 최댓값을 작게 만드는 방법은 없다.

배열과 M이 주어졌을 때, 구간의 점수의 최댓값의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 배열의 크기 N과 M이 주어진다. (1 ≤ N ≤ 5,000, 1 ≤ M ≤ N)

둘째 줄에 배열에 들어있는 수가 순서대로 주어진다. 배열에 들어있는 수는 1보다 크거나 같고, 10,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 구간의 점수의 최댓값의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
8 3
1 5 4 6 2 1 3 7
```

**예제 출력1**

```
5
```

**예제 입력2**

```
4 2
1 1 1 1
```

**예제 출력2**

```
0
```

**예제 입력3**

```
7 4
1 2 3 1 2 3 1
```

**예제 출력3**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def is_possible(limit):
    count = 1
    min_val = arr[0]
    max_val = arr[0]

    for num in arr[1:]:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

        if max_val - min_val > limit:
            count += 1
            min_val = num
            max_val = num
    
    return count <= M

N, M = map(int, input().split())
arr = list(map(int, input().split()))

min_score, max_score = 0, max(arr) - min(arr)
answer = max_score

while min_score <= max_score:
    mid = (min_score + max_score) // 2

    if is_possible(mid):
        answer = mid
        max_score = mid - 1
    
    else:
        min_score = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33564|48|Python3|658
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def isValid(midValue):
    global result
    low = arr[0]
    high = arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i

        if low > i:
            low = i
        
        if high - low > midValue:
            d += 1
            low = i
            high = i

    return m >= d

n, m = map(int, input().split())

arr = list(map(int, input().split()))

r = max(arr)
l = 0

result = r
while l <= r:
    mid = (l + r) // 2

    if isValid(mid):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1

print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kkk5474096|31252|40|Python3|611
#### **📝해설**

```python

# 현재의 차이를 기준으로 M개 이하 구간으로 만들 수 있는지 검증
def is_possible(limit):

    # 한개의 구간으로 시작
    count = 1

    # 구간에서 최대, 최소값
    min_val = arr[0]
    max_val = arr[0]

    # 숫자들을 확인하면서
    for num in arr[1:]:

        # 현재 구간의 최소값, 최대값을 확인
        min_val = min(min_val, num)
        max_val = max(max_val, num)

        # 설정한 값을 넘긴다면 새로운 구간을 만듦
        if max_val - min_val > limit:
            count += 1
            min_val = num
            max_val = num
    
    # 구간의 개수가 M개를 넘는지 확인
    return count <= M

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 이분 탐색을 위해 값을 최대 최소로 잡음
min_score, max_score = 0, max(arr) - min(arr)
answer = max_score

# 이분탐색
while min_score <= max_score:
    mid = (min_score + max_score) // 2

    # M개의 구간으로 만드는 것이 가능하다면
    if is_possible(mid):

        # 일단 정답 저장
        answer = mid
        # 값을 더 줄여서 확인해봄
        max_score = mid - 1
    
    # M개의 구간으로 만드는 경우가 불가능하다면
    else:

        # 값을 더 키움
        min_score = mid + 1

print(answer)
```