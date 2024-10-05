# [14395] 4연산

### **난이도**
골드 4
## **📝문제**
정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.

사용할 수 있는 연산은 아래와 같다.

1. s = s + s; (출력: +)
2. s = s - s; (출력: -)
3. s = s * s; (출력: *)
4. s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)
### **입력**
첫째 줄에 s와 t가 주어진다. (1 ≤ s, t ≤ 109)
### **출력**
첫째 줄에 정수 s를 t로 바꾸는 방법을 출력한다. s와 t가 같은 경우에는 0을, 바꿀 수 없는 경우에는 -1을 출력한다. 가능한 방법이 여러 가지라면, 사전 순으로 앞서는 것을 출력한다. 

연산의 아스키 코드 순서는 '*', '+', '-', '/' 이다.
### **예제입출력**

**예제 입력1**

```
7 392
```

**예제 출력1**

```
+*+
```

**예제 입력2**

```
7 256
```

**예제 출력2**

```
/+***
```

**예제 입력3**

```
4 256
```

**예제 출력3**

```
**
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import operator
from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

visited = {}
visited[s] = ''
visited[0] = '-'
if s != 1:
    visited[1] = '/'
visited[2*s] = '+'
visited[s*s] = '*'

q = deque()
q.append(s)
q.append(s*s)
q.append(2*s)
q.append(0)
q.append(1)

operations = {
    '*': operator.mul,
    '+': operator.add,
}

calcs = ['*', '+']

while q:
    now = q.popleft()

    if now == t:
        break

    for calc in calcs:
        next = operations[calc](now, now)
        if next > t:
            continue

        if visited.get(next) is None:
            visited[next] = visited[now] + calc
            q.append(next)

if visited.get(t) is None:
    print(-1)
else:
    print(visited[t])

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34088|60|Python3|750
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
from _collections import deque

si = sys.stdin.readline

s, t = map(int, si().strip().split())


def bfs(s, t):
    if s == t: return 0

    """
    s < t , 1부터시작하는경우와 s 에서부터 시작하는 경우 둘다  
    s == t 
    s > t ,1 부터 시작하는 경우와 2배, 제곱해서 갈수있는경우 1,2,4,8,16
    
    """
    ans = []

    q = deque([])
    vis = {s}
    q.append((s, ""))
    while q:
        integer, operators = q.popleft()
        if integer == t:
            ans.append(operators)
            continue
        if integer ** 2 <= int(1e9) and integer ** 2 not in vis:
            vis.add(integer ** 2)
            q.append((integer ** 2, operators + "*"))
        if 2 * integer <= int(1e9) and 2 * integer not in vis:
            vis.add(integer * 2)
            q.append((integer * 2, operators + "+"))
        if 1 not in vis:
            vis.add(1)
            q.append((1, operators + '/'))

    ans.sort(key=lambda x: (len(x), x))
    #print(ans)
    if not ans: return -1
    return ans[0]


print(bfs(s, t))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jahy5352|31252|32|Python3|1073
#### **📝해설**

```python
import operator
from collections import deque

s, t = map(int, input().split())
# s, t가 같으면 0을 출력하고 종료
if s == t:
    print(0)
    exit()

# 이미 만들었던 숫자인지 검증
visited = {}

# 초기값 삽입

# /, -연산은 항상 0과 1.
# 따라서 앞으로의 연산에 포함될 필요가 없음
# 미리 계산
visited[s] = ''
visited[0] = '-'
if s != 1:
    visited[1] = '/'

# 사전순 정렬을 위해 값을 덮어씌워줌
visited[2*s] = '+'
visited[s*s] = '*'

# 큐에 삽입
q = deque()
q.append(s)
q.append(s*s)
q.append(2*s)
q.append(0)
q.append(1)

# 문자열 연산자를 사용하기 위해 만든 딕셔너리
operations = {
    '*': operator.mul,
    '+': operator.add,
}

calcs = ['*', '+']

# BFS
while q:
    now = q.popleft()

    if now == t:
        break

    # 곱하기와 덧셈만 진행
    for calc in calcs:
        next = operations[calc](now, now)

        # 이미 만들어야 할 수를 넘겼다면 고려하지않음
        if next > t:
            continue

        # 방문하지 않았다면 방문
        if visited.get(next) is None:
            # 기존의 연산자 문자열에 추가
            visited[next] = visited[now] + calc
            q.append(next)

# 방문하지 않았다면 -1 아니라면 방문처리 문자열 출력
if visited.get(t) is None:
    print(-1)
else:
    print(visited[t])

```

### **🔖정리**

1. 엣지 케이스를 잘 생각해보자