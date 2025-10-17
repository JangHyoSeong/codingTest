# [1508] 레이스

### **난이도**
골드 2
## **📝문제**
세준이는 세준항공으로 돈을 무지막지하게 번 뒤, 레이스 대회를 개최했다. 레이스 트랙은 길이가 N인 직선이다.

세준이는 심판 M명을 적절한 곳에 배치시키려고 한다. 심판은 아무 곳에나 배치시킬 수 있지 않다. 심판은 미리 정해진 K개의 곳에만 위치할 수 있다.

세준이는 심판을 배치할 때, 가장 가까운 두 심판의 거리를 최대로 하려고 한다.

심판을 어디에 배치시켜야 할지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N, M, K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, M은 K보다 작거나 같은 자연수이다. 또, K는 2보다 크거나 같고, 50보다 작거나 같다. 둘째 줄에 심판이 있을 수 있는 K개의 위치가 주어진다. K개의 위치는 N보다 작거나 같은 자연수 또는 0이며, 오름차순으로 주어진다.
### **출력**
첫째 줄에 심판을 어떻게 배치시켜야 가장 가까운 심판의 거리가 최대가 될 것이지 출력한다. 출력할 때는 예제와 같이 심판을 세울 곳에는 1을, 세우지 않을 곳에는 0을 출력한다. 만약 정답이 여러개일 경우에는 사전순으로 가장 늦는 것을 출력한다.
### **예제입출력**

**예제 입력1**

```
11 3 4
0 5 10 11
```

**예제 출력1**

```
1110
```

**예제 입력2**

```
11 2 4
0 5 10 11
```

**예제 출력2**

```
1001
```

**예제 입력3**

```
11 4 4
0 5 10 11
```

**예제 출력3**

```
1111
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

min_dist, max_dist = 0, N
result = 0

while min_dist <= max_dist:
    mid = (min_dist + max_dist) // 2
    count = 1

    before_pos = arr[0]
    for i in range(1, K):
        if arr[i] - before_pos >= mid:
            count += 1
            before_pos = arr[i]
        
        if count >= M:
            result = mid
            min_dist = mid + 1
            break

    else:
        max_dist = mid - 1

answer = "1"
before_pos = arr[0]
count = 1
for i in range(1, K):
    if count < M and arr[i] - before_pos >= result:
        answer += "1"
        before_pos = arr[i]
        count += 1
    
    else:
        answer += "0"

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|719
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
2. 그리디 알고리즘
```

### **다른 풀이**

```python
N, M, K = map(int, input().split())
A = list(map(int, input().split()))

N, K = K, M

def ok(k):
    cnt = 1
    prv = A[0]
    for i in range(1, N):
        if A[i] - prv >= k:
            cnt += 1
            prv = A[i]
    return cnt >= K

lo, hi = 0, int(1e9 + 1)

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid

cnt = 1
prv = A[0]
print(1, end='')
for i in range(1, N):
    if cnt < K and A[i] - prv >= lo:
        print(1, end='')
        prv = A[i]
        cnt += 1
    else:
        print(0, end='')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yuja|30748|36|Python3|564
#### **📝해설**

```python
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 이분 탐색으로 최소, 최대값을 정한 뒤 최대 떨어질 수 있는 거리를 구함
min_dist, max_dist = 0, N

# 최대로 떨어질 수 있는 거리
result = 0

# 이분 탐색 시작
while min_dist <= max_dist:

    # 중간값
    mid = (min_dist + max_dist) // 2

    # 항상 첫번째 자리에는 심판을 배치(놓는 경우가 그리디하게 제일 멀리 배치 가능)
    count = 1

    # 직전에 심판이 배치된 위치
    before_pos = arr[0]

    # 이후 인덱스부터 탐색
    for i in range(1, K):

        # 현재 거리상 배치가 가능하다면
        if arr[i] - before_pos >= mid:

            # 배치
            count += 1
            before_pos = arr[i]
        
        # 이미 M명이 배치 가능하다면
        if count >= M:
            result = mid

            # 거리를 더 늘려서 탐색
            min_dist = mid + 1
            break
    
    # M명이 배치 불가능하다면 거리를 줄여서 탐색
    else:
        max_dist = mid - 1

# 항상 첫번째 위치는 배치함
answer = "1"
before_pos = arr[0]
count = 1

# 거리를 기반으로 심판 배치 위치를 찾음
for i in range(1, K):

    # M명이 배치되지 않았고, 배치 가능한 위치라면 배치
    if count < M and arr[i] - before_pos >= result:
        answer += "1"
        before_pos = arr[i]
        count += 1
    
    else:
        answer += "0"
# 출력
print(answer)
```