# [12913] 매직 포션

### **난이도**
골드 3
## **📝문제**
0부터 N-1까지 번호가 매겨져있는 N개의 도시가 있다. 도시는 모두 연결되어 있기 때문에, 임의의 두 도시를 여행하는 것은 항상 가능하다.

모든 도시 사이를 이동하는데 걸리는 시간과 가지고 있는 매직 포션의 개수 K가 주어진다. 매직 포션은 평소보다 두 배 빠르게 움직일 수 있게 해준다. 한 도시에서 다른 도시로 이동할 때, 매직 포션을 하나 사용할 수 있다. 

도시 0에서 도시 1을 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오. 모든 매직 포션을 다 마실 필요는 없다.
### **입력**
첫째 줄에 도시의 개수 N과 가지고 있는 매직 포션의 개수 K가 주어진다. (2 ≤ N ≤ 50, 0 ≤ K ≤ 50)

둘째 줄부터 N개의 줄에는 도시사이의 거리가 주어진다. i번 줄의 j번째 수는 i번 도시에서 j번 도시를 가는데 걸리는 시간이다. 시간은 0보다 크거나 같고, 9보다 작거나 같은 자연수이다.

i번째 줄의 j번째 수는 j번째 줄의 i번째 수와 같으며, i번째 줄의 i번째 수는 항상 0이다.
### **출력**
첫째 줄에 도시 0에서 1을 가는데 가장 빠른 시간을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

### **예제입출력**

**예제 입력1**

```
3 1
094
904
440
```

**예제 출력1**

```
4.5
```

**예제 입력2**

```
3 2
094
904
440
```

**예제 출력2**

```
4.0
```

**예제 입력3**

```
6 1
076237
708937
680641
296059
334508
771980
```

**예제 출력3**

```
3.5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush

N, K = map(int, input().split())
adj = [list(map(int, input())) for _ in range(N)]

pq = []
INF = 21e8

distance = [[INF] * N for _ in range(K+1)]

# node, dist, potion
heappush(pq, (0, 0, 0))

while pq:
    now_node, now_dist, now_potion = heappop(pq)

    if now_dist > distance[now_potion][now_node]:
        continue

    for next_node in range(N):
        if next_node != now_node:
            if now_potion < K:
                weight = adj[now_node][next_node] / 2
                new_dist = now_dist + weight

                if new_dist < distance[now_potion+1][next_node]:
                    distance[now_potion+1][next_node] = new_dist
                    heappush(pq, (next_node, new_dist, now_potion+1))
            
            weight = adj[now_node][next_node]
            new_dist = now_dist + weight

            if new_dist < distance[now_potion][next_node]:
                distance[now_potion][next_node] = new_dist
                heappush(pq, (next_node, new_dist, now_potion))

min_dist = distance[0][1]
for i in range(1, K+1):
    min_dist = min(min_dist, distance[i][1])

print(min_dist)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36532|252|Python3|1150
#### **📝해설**

**알고리즘**
```
1. 최단거리
```

### **다른 풀이**

```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
city = [list(map(int, list(input().strip()))) for _ in range(N)]

time = [[float('inf')] * (K+1) for _ in range(N)]
time[0][0] = 0

pq = []
heappush(pq, (0, 0, 0))

while pq:
    t, now, k = heappop(pq)

    if t > time[now][k]:
        continue

    for next in range(N):
        if next == now:
            continue

        if t + city[now][next] < time[next][k]:
            time[next][k] = t + city[now][next]
            heappush(pq, (t + city[now][next], next, k))

        if k < K:
            if t + city[now][next] / 2 < time[next][k+1]:
                time[next][k+1] = t + city[now][next] / 2
                heappush(pq, (t + city[now][next] / 2, next, k+1))

print(min(time[1]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yujeong55|33188|100|Python3|802
#### **📝해설**

```python
from heapq import heappop, heappush

# 입력
N, K = map(int, input().split())
adj = [list(map(int, input())) for _ in range(N)]

# 우선순위 큐
pq = []
# 임의의 큰 값 상수
INF = 21e8

# 포션을 사용한 횟수에 따라 최단거리를 따로 구함
distance = [[INF] * N for _ in range(K+1)]

# node, dist, potion
heappush(pq, (0, 0, 0))


# 다익스트라 알고리즘
while pq:
    now_node, now_dist, now_potion = heappop(pq)

    if now_dist > distance[now_potion][now_node]:
        continue

    for next_node in range(N):
        if next_node != now_node:

            # 아직 포션 사용 횟수가 남았다면, 거리를 반으로 줄이고 다익스트라 적용
            if now_potion < K:
                weight = adj[now_node][next_node] / 2
                new_dist = now_dist + weight

                if new_dist < distance[now_potion+1][next_node]:
                    distance[now_potion+1][next_node] = new_dist
                    heappush(pq, (next_node, new_dist, now_potion+1))
            
            # 포션 사용 횟수가 없거나, 남았어도 거리를 그대로 하고 다익스트라 적용
            weight = adj[now_node][next_node]
            new_dist = now_dist + weight

            if new_dist < distance[now_potion][next_node]:
                distance[now_potion][next_node] = new_dist
                heappush(pq, (next_node, new_dist, now_potion))


# 모든 포션 사용 횟수 중에서 최소값을 출력
min_dist = distance[0][1]
for i in range(1, K+1):
    min_dist = min(min_dist, distance[i][1])

print(min_dist)
```