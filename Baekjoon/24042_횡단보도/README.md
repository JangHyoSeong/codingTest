# [24042] 횡단보도

### **난이도**
골드 1
## **📝문제**
당신은 집으로 가는 도중 복잡한 교차로를 만났다! 이 교차로에는 사람이 지나갈 수 있는 
$N$ 개의 지역이 있고 그 지역 사이를 잇는 몇 개의 횡단보도가 있다. 모든 지역은 횡단보도를 통해 직, 간접적으로 연결되어 있다. 편의상 
$N$ 개의 지역을 
$1$부터 
$N$까지로 번호를 붙이자.



당신은 이미 멀리서 교차로의 신호를 분석했기 때문에 횡단보도에 파란불이 들어오는 순서를 알고 있다. 횡단보도의 주기는 총 
$M$ 분이며 
$1$분마다 신호가 바뀐다. 각 주기의 
$1+i (0 \le i < M)$ 번째 신호는 
$i, M+i, 2M+i, 3M+i, \cdots$ 분에 시작해서 
$1$분 동안 
$A_i$번 지역과 
$B_i$번 지역을 잇는 횡단보도에 파란불이 들어오고, 다른 모든 횡단보도에는 빨간불이 들어온다. 한 주기 동안 같은 횡단보도에 파란불이 여러 번 들어올 수 있다.

횡단보도에 파란불이 들어오면 당신은 해당 횡단보도를 이용하여 반대편 지역으로 이동할 수 있으며 이동하는 데 
$1$분이 걸린다. 횡단보도를 건너는 도중에 신호가 빨간불이 되면 안되기 때문에 신호가 
$s \sim e$ 시간에 들어온다면 반드시 
$s \sim e-1$ 시간에 횡단보도를 건너기 시작해야 한다.

횡단보도와 신호의 정보가 주어질 때, 시간 
$0$분 에서 시작해서 
$1$번 지역에서 
$N$번 지역까지 가는 최소 시간을 구하는 프로그램을 작성하여라.
### **입력**
첫 번째 줄에는 지역의 수 
$N$, 횡단보도의 주기 
$M$이 공백으로 구분되어 주어진다.

두 번째 줄부터 
$M$ 개의 줄 중 
$1+i$ 번째 줄에는 
$i, M+i, 2M+i, 3M+i, \cdots$ 분에 시작해서 
$1$분동안 파란불이 들어오는 횡단보도의 두 끝점 
$A_i$, 
$B_i$가 공백으로 주어진다.
### **출력**
첫 번째 줄에 
$1$ 번 지역에서 
$N$ 번 지역까지 가는데 필요한 최소 시간을 분단위로 출력한다.
### **예제입출력**

**예제 입력1**

```
4 5
1 2
3 4
1 3
4 1
2 3
```

**예제 출력1**

```
4
```

**예제 입력2**

```
8 12
3 4
5 6
7 8
2 3
1 5
4 8
1 2
6 7
2 3
7 8
1 2
6 7
```

**예제 출력2**

```
18
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for time in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append([time, b])
    edges[b].append([time, a])

dist = [21e8] * (N+1)
dist[1] = 0

pq = []
heappush(pq, (0, 1))

while pq:
    time, now = heappop(pq)

    if now == N:
        break

    if time > dist[now]:
        continue

    for period, next in edges[now]:
        wait_time = (period - (time % M)) % M
        next_time = time + wait_time + 1

        if next_time < dist[next]:
            dist[next] = next_time
            heappush(pq, (next_time, next))

print(dist[-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|276412|1956|PyPy3|721
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
from heapq import heappush, heappop 
import sys 
input = sys.stdin.readline 

n, T = map(int, input().split(' ')) 

edge = [[] for _ in range(n + 1)] # 1번부터 n번까지. 
for i in range(T):
    a, b = map(int, input().split(' ')) 
    edge[a].append((b, i)) 
    edge[b].append((a, i)) 

# parsing 완료. 

dist = [float('inf') for _ in range(n + 1)] 
visited = [False for _ in range(n + 1)] 

# 1번에서 N번까지 가는 것이 목표. 
dist[1] = 0 
queue =[(0, 1)] 
while(queue): 
    d, node = heappop(queue) 
    if(visited[node]): 
        continue 
    elif(node == n): 
        print(d) 
        break 
    
    visited[node] = True 
    for nx, t in edge[node]: 
        if(visited[nx]):
            continue 
        # t + xT가 d 이상이 되는 최소의 x값을 구해야함. 
        # -> (d - t) // T
    
        x = (d - t) // T 
        if(t + x * T < d): 
            x += 1
        # print(F"디버그 : {node, nx, t, x, t + x * T}")
        # 이것이 의미하는 바? 
        # 시각이 t + x*T가 되어야 건널 수 있음. 이때 x는 
        # 이러한 성질을 만족하는 최소의 값. 

        if(dist[nx] > t + x * T + 1): 
            dist[nx] = t + x * T + 1 
            heappush(queue, (t + x * T + 1, nx)) 
        # 도달하는 데에는 1분이 걸림에 유의. 
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rock5858|219192|1076|PyPy3|1321
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())

# 간선 정보 저장
edges = [[] for _ in range(N+1)]

# 양방향 그래프라서 양방향 간선정보 삽입
for time in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # 간선을 건널 수 있는 시간을 기준으로 삽입
    edges[a].append([time, b])
    edges[b].append([time, a])

# 최소거리를 저장할 리스트
# int보다 클 수 있어서 float로 초기화
dist = [float('inf')] * (N+1)
dist[1] = 0

# 다익스트라에 사용할 우선순위 큐
pq = []
heappush(pq, (0, 1))

# 다익스트라 시작
while pq:
    time, now = heappop(pq)

    # 마지막 노드에 도달했다면 종료
    if now == N:
        break

    # 현재가 최소거리보다 길다면 continue
    if time > dist[now]:
        continue

    # 갈 수 있는 간선을 모두 탐색
    for period, next in edges[now]:

        # 아직 건너갈 수 없다면 그만큼 기다리고 시간을 더함
        wait_time = (period - (time % M)) % M

        # 기다린 시간을 더함
        next_time = time + wait_time + 1

        # 최소거리보다 짧다면 갱신
        if next_time < dist[next]:
            dist[next] = next_time
            heappush(pq, (next_time, next))

print(dist[N])
```

### **🔖정리**

1. 힙큐를 사용할 때, 처음 값을 기준으로 들어간다. 이걸 까먹어서 계속 틀렸음,,