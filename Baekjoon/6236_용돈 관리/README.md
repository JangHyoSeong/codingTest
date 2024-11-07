# [6236] 용돈 관리

### **난이도**
실버 1
## **📝문제**
현우는 용돈을 효율적으로 활용하기 위해 계획을 짜기로 하였다. 현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼서 쓰기로 하였다. 현우는 통장에서 K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다. 다만 현우는 M이라는 숫자를 좋아하기 때문에, 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다. 현우는 돈을 아끼기 위해 인출 금액 K를 최소화하기로 하였다. 현우가 필요한 최소 금액 K를 계산하는 프로그램을 작성하시오.
### **입력**
1번째 줄에는 N과 M이 공백으로 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)

2번째 줄부터 총 N개의 줄에는 현우가 i번째 날에 이용할 금액이 주어진다. (1 ≤ 금액 ≤ 10000)
### **출력**
첫 번째 줄에 현우가 통장에서 인출해야 할 최소 금액 K를 출력한다.
### **예제입출력**

**예제 입력1**

```
7 5
100
400
300
100
500
101
400
```

**예제 출력1**

```
500
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left, right = max(arr), sum(arr)

while left <= right:
    mid = (left+right) // 2
    count, total = 1, 0

    for i in range(N):
        if total + arr[i] > mid:
            count += 1
            total = 0
        total += arr[i]


    if count <= M:
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112440|156|PyPy3|420
#### **📝해설**

**알고리즘**
```
1. 이분탐색
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    now = 0
    for i in range(n):
        if l[i] > now:
            now = x
            ret += 1
            if now < l[i]: return False
            now -= l[i]
        else:
            now -= l[i]
    
    return ret <= m
        


n,m = map(int, input().split())
l = [int(input()) for _ in range(n)]

left = 0
right = int(1e9)

while left + 1 < right:
    mid = (left + right)//2

    if check(mid):
        right = mid
    else:
        left = mid

print(right)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
gyoseon123|111288|124|PyPy3|533
#### **📝해설**

```python
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 최소, 최대값을 정해두고 이분탐색
left, right = max(arr), sum(arr)

while left <= right:

    # 중간값을 저장
    mid = (left+right) // 2

    # 인출횟수, 현재 총액
    count, total = 1, 0

    # 사용할 돈을 순회하면서
    for i in range(N):

        # 만약 이번에 사용할 돈이 인출금액보다 크다면
        if total + arr[i] > mid:

            # 사용해야함
            count += 1
            # 사용할 돈을 초기화
            total = 0

        # 사용할 금액을 추가
        total += arr[i]


    if count <= M:
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)
```