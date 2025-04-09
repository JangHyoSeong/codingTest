# [22871] 징검다리 건너기

### **난이도**
실버 1
## **📝문제**
$N$개의 돌이 일렬로 나열 되어 있다. 
$N$개의 돌에는 왼쪽부터 차례대로 수 
$A_{1} A_{2} ... A_{i} ... A_{N}$로 부여되어 있다. 가장 왼쪽에 있는 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너가려고 한다.

1. 항상 오른쪽으로만 이동할 수 있다.
 
2. $i$번째 돌에서 $j(i < j)$번째 돌로 이동할 때 $(j - i)$ × (1 + |$A_{i} - A_{j}$|) 만큼 힘을 쓴다.
3. 돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 $K$이다.

가장 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는 모든 경우 중 $K$의 최솟값을 구해보자.
### **입력**
첫 번째 줄에 돌의 개수 $N$이 공백으로 구분되어 주어진다.

두 번째 줄에는 $N$개의 돌의 수 $A_i$가 공백으로 구분되어 주어진다.
### **출력**
가장 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는 모든 경우 중 가능한 $K$의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
1 4 1 3 1
```

**예제 출력1**

```
2
```

**예제 입력2**

```
5
1 5 2 1 6
```

**예제 출력2**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, int(21e8)
answer = right

while left <= right:
    mid = (left + right) // 2
    K = mid

    visited = [False] * N
    q = deque([0])
    visited[0] = True

    while q:
        now = q.popleft()
        for next in range(now + 1, N):
            cost = (next - now) * (1 + abs(arr[now] - arr[next]))
            if cost > K:
                continue
            if not visited[next]:
                visited[next] = True
                q.append(next)

    if visited[N-1]:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112824|3548|PyPy3|672
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
INF = 999999999
N = int(input())
A = list(map(int, input().split()))

dp = [0] + [INF] * (N - 1)

for i in range(1, N):
    for j in range(i):
        k = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
        dp[i] = min(dp[i], k)

print(dp[-1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
oj0410|110604|212|PyPy3|282
#### **📝해설**

```python
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

# 이분 탐색을 위한 K값의 최대 최소 설정
left, right = 0, int(21e8)
answer = right

# 이분탐색 시작
while left <= right:

    # K값 설정
    mid = (left + right) // 2
    K = mid

    # BFS를 위한 방문 여부 리스트
    visited = [False] * N
    q = deque([0])
    visited[0] = True

    # BFS
    while q:
        now = q.popleft()

        # 뒤에 있는 모든 징검다리를 검사
        for next in range(now + 1, N):

            # 갈때 발생하는 비용
            cost = (next - now) * (1 + abs(arr[now] - arr[next]))

            # K를 넘는 곳이라면 방문하지 않음
            if cost > K:
                continue
            
            # 아직 방문하지 않았다면 방문
            if not visited[next]:
                visited[next] = True
                q.append(next)

    # 맨 끝의 징검다리에 방문할 수 있었다면, 최대 K를 줄인 뒤 이분탐색
    if visited[N-1]:
        answer = mid
        right = mid - 1

    # 방문할 수 없었다면, K를 늘린 뒤 탐색
    else:
        left = mid + 1

print(answer)
```