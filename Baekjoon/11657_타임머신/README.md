# [11657] 타임머신

### **난이도**
골드 4
## **📝문제**
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다. 둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다. 
### **출력**
만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
```

**예제 출력1**

```
4
3
```

**예제 입력2**

```
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
3 2
1 2 4
1 2 3
```

**예제 출력3**

```
3
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

min_dist = [float('inf')] * (N+1)
min_dist[1] = 0

for i in range(N):
    for j in range(M):
        now_node = edges[j][0]
        next_node = edges[j][1]
        dist = edges[j][2]

        if min_dist[now_node] != float('inf') and min_dist[next_node] > min_dist[now_node] + dist:
            min_dist[next_node] = min_dist[now_node] + dist
            if i == N-1:
                print(-1)
                exit()

for i in range(2, N+1):
    if min_dist[i] == float('inf'):
        print(-1)
    else:
        print(min_dist[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111972|284|PyPy3|665
#### **📝해설**

**알고리즘**
```
1. 최단 거리 알고리즘 (벨만-포드)
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
INF = int(1e8)

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distance = [INF] * (n+1)
distance[1] = 0
iscycle = False
for i in range(n):
    for a, b, c in edges:
        if distance[a] != INF and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c
            if i == n-1:
                iscycle = True

if iscycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i] if distance[i] != INF else -1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
htg1616|111240|132|PyPy3|568
#### **📝해설**

```python
N, M = map(int, input().split())
edges = []

# 간선 정보를 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 최단거리 초기화
min_dist = [float('inf')] * (N+1)
min_dist[1] = 0

# 한번에 모든 간선 정보를 갱신함
for i in range(N):
    for j in range(M):
        now_node = edges[j][0]
        next_node = edges[j][1]
        dist = edges[j][2]

        # 도달한 적 있는 노드이고, 최단거리가 갱신 가능하다면 갱신
        if min_dist[now_node] != float('inf') and min_dist[next_node] > min_dist[now_node] + dist:
            min_dist[next_node] = min_dist[now_node] + dist

            # 음수로 무한히 갱신 가능한 경우
            if i == N-1:
              # 종료
                print(-1)
                exit()

for i in range(2, N+1):
    if min_dist[i] == float('inf'):
        print(-1)
    else:
        print(min_dist[i])
```