# [13549] 숨바꼭질 3

### **난이도**
골드 5
## **📝문제**
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
### **출력**
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 17
```

**예제 출력1**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())

visited = [-1] * (100001)
visited[N] = 0

q = deque([N])

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break

    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:
        q.appendleft(now * 2)
        visited[now * 2] = visited[now]

    for next in (now-1, now+1):
        if 0 <= next < 100001 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|38164|120|Python3|501
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
def solve(n, k):
    if n >= k: return n-k
    if n == 0: return 1 + solve(n+1, k)
    if k%2 == 0: return min(k-n, solve(n, k//2))
    return 1 + min(solve(n, k+1), solve(n, k-1))

n, k = map(int, input().split())
print(solve(n, k))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|31120|36|Python3|1333
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())

# 방문시 이동 횟수를 저장하는 리스트
visited = [-1] * (100001)
visited[N] = 0

# BFS를 위한 queue 선언
q = deque([N])

# BFS
while q:
    now = q.popleft()

    # 목표에 도착했다면 종료
    if now == K:
        print(visited[now])
        break

    # *2는 이동횟수가 추가되지 않음. 따라서 따로 계산
    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:

        # queue의 왼쪽에 삽입해서 우선적으로 처리하게끔 함
        q.appendleft(now * 2)
        visited[now * 2] = visited[now]

    # ++, -- 연산 수행
    for next in (now-1, now+1):
        if 0 <= next < 100001 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
```