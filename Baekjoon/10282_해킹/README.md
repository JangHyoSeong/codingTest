# [10282] 해킹

### **난이도**
골드 4
## **📝문제**
최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 최대 100개이다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

- 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c가 주어진다(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n).
- 이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s가 주어진다(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000). 이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻한다.

각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.
### **출력**
각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력한다.
### **예제입출력**

**예제 입력1**

```
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4
```

**예제 출력1**

```
2 5
3 6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

INF = int(21e8)

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    n, d, c = map(int, sys.stdin.readline().rstrip().split())

    edges = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        edges[b].append((s, a))

    infected = [INF] * (n+1)
    infected[c] = 0
    pq = [(0, c)]

    while pq:
        now_time, now_node = heappop(pq)
        
        if now_time > infected[now_node]:
            continue

        for next_time, next_node in edges[now_node]:
            new_time = now_time + next_time

            if new_time < infected[next_node]:
                heappush(pq, (new_time, next_node))
                infected[next_node] = new_time
    
    count = 0
    last_infected = 0
    for i in range(1, n+1):
        if infected[i] != INF:
            count += 1
            last_infected = max(last_infected, infected[i])
    
    print(count, last_infected)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|49844|784|Python3|1012
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())

def virus(s):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])
    while q:
        x = q.popleft()
        for w, t in graph[x]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[x] + t
            else:
                if visited[w] > visited[x] + t:
                    visited[w] = visited[x] + t
                    q.append(w)
    return n - visited.count(0) + 1, max(visited) - 1

def main():
    global n, graph
    for _ in range(tc):
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))
        print(*virus(c))

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|137892|364|PyPy3|824
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

INF = int(21e8)

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    n, d, c = map(int, sys.stdin.readline().rstrip().split())

    edges = [[] for _ in range(n+1)]

    # 간선 정보 입력
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        edges[b].append((s, a))

    # 해당 컴퓨터가 감염될때 최소시간
    infected = [INF] * (n+1)

    # 시작
    infected[c] = 0
    pq = [(0, c)]

    # 다익스트라
    while pq:
        now_time, now_node = heappop(pq)
        
        if now_time > infected[now_node]:
            continue

        for next_time, next_node in edges[now_node]:
            new_time = now_time + next_time

            if new_time < infected[next_node]:
                heappush(pq, (new_time, next_node))
                infected[next_node] = new_time
    
    # 모든 컴퓨터를 확인하면서, 몇개가 감염됐는지, 가장 늦게 감염된 컴퓨터가 어느것인지 확인
    count = 0
    last_infected = 0
    for i in range(1, n+1):
        if infected[i] != INF:
            count += 1
            last_infected = max(last_infected, infected[i])
    
    print(count, last_infected)
```