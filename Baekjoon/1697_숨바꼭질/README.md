# [1697] 숨바꼭질

### **난이도**
실버 1
## **📝문제**
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

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
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
visited = [False] * (100002)
visited[N] = True

while q:
    now, count = q.popleft()
    if now == K:
        print(count)
        break

    for next in [now-1, now+1, now*2]:
        if 0 <= next <= 100001 and not visited[next]:
            q.append((next, count+1))
            visited[next] = True

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34612|120|Python3|388
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
def find(n,m):
    if n>=m :
        return (n-m)
    elif m == 1:
        return 1
    elif m%2 == 0: #짝수면
        return min(m-n , find(n,m//2)+1)
    else: #홀수면
        return min(find(n,m-1),find(n,m+1))+1
print(find(n,m))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
steptofly|31120|40|Python3|310
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())

# BFS를 위해 queue 선언
q = deque([(N, 0)])

# 방문 여부를 검사
visited = [False] * (100002)
visited[N] = True

# BFS 시작
while q:
    now, count = q.popleft()

    # 도착지에 도달했다면 종료
    if now == K:
        print(count)
        break

    # 다음으로 이동할 장소를 확인
    for next in [now-1, now+1, now*2]:
        if 0 <= next <= 100001 and not visited[next]:
            q.append((next, count+1))
            visited[next] = True

```