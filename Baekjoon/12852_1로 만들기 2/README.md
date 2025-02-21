# [12852] 1로 만들기 2

### **난이도**
골드 5
## **📝문제**
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
### **입력**
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.
### **출력**
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.
### **예제입출력**

**예제 입력1**

```
2
```

**예제 출력1**

```
1
2 1
```

**예제 입력2**

```
10
```

**예제 출력2**

```
3
10 9 3 1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
visited = [-1] * (N+1)
visited[N] = 0

q = deque([N])

while q:
    now = q.popleft()

    if now == 1:
        break

    if now == 0:
        continue

    if now % 3 == 0:
        next = now // 3
        if visited[next] == -1:
            q.append(next)
            visited[next] = now

    if now % 2 == 0:
        next = now // 2
        if visited[next] == -1:
            q.append(next)
            visited[next] = now
    
    next = now - 1
    if visited[next] == -1:
        q.append(next)
        visited[next] = now

count = -1
now = 1
result = []
while visited[now] != -1:
    count += 1
    result.append(now)
    now = visited[now]

print(count)
print(" ".join(map(str, reversed(result))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42144|76|Python3|754
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
N = int(input())

queue = [[0, N, []]]
ans = []

i= 0
num_visited = {N:1}

while queue:
    count, cur, visited = queue.pop(0)
    new_visited = visited[:]
    if cur == 1:
        new_visited.append(cur)
        ans.append([count, new_visited])
        break
    elif cur > 1:
        new_visited.append(cur)
        if cur % 3 == 0 and cur//3 not in num_visited:
            queue.append([count+1, cur//3, new_visited])
            num_visited[cur//3] = 1
        if cur % 2 == 0 and cur//2 not in num_visited:
            queue.append([count+1, cur//2, new_visited])
            num_visited[cur//2] = 1
        if cur-1 not in num_visited:
            queue.append([count+1, cur-1, new_visited])
            num_visited[cur-1] = 1

ans_sort = sorted(ans)
print(ans_sort[0][0])
for num in ans_sort[0][1]:
    print(num, end=" ")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
gyeongmin951|31120|40|Python3|831
#### **📝해설**

```python
from collections import deque

# 입력받기
N = int(input())

# 방문하지 않았던 노드는 -1, 방문한다면 이전에 출발한 숫자를 저장
visited = [-1] * (N+1)

# 시작점 초기화
visited[N] = 0

# BFS를 위한 queue 선언
q = deque([N])

# BFS
while q:
    now = q.popleft()

    # 1이 되었다면 종료
    if now == 1:
        break
    
    # 1보다 작아진다면 무시
    if now == 0:
        continue
    
    # 3으로 나누어 떨어질경우
    if now % 3 == 0:
        # 3으로 나눈 몫을 방문처리
        next = now // 3
        if visited[next] == -1:
            q.append(next)
            visited[next] = now

    # 2로 나누어 떨어질 경우
    if now % 2 == 0:
        next = now // 2
        if visited[next] == -1:
            q.append(next)
            visited[next] = now
    
    # 1을 빼는 경우
    next = now - 1
    if visited[next] == -1:
        q.append(next)
        visited[next] = now

# 이동횟수
count = -1

# 시작점
now = 1

# 방문한 숫자들을 저장할 리스트
result = []

# 역순으로 경로를 추적
while visited[now] != -1:
    count += 1
    result.append(now)
    now = visited[now]

print(count)
print(" ".join(map(str, reversed(result))))
```

### **🔖정리**

1. 배운점