# [1368] 물대기

### **난이도**
골드 2
## **📝문제**
선주는 자신이 운영하는 N개의 논에 물을 대려고 한다. 물을 대는 방법은 두 가지가 있는데 하나는 직접 논에 우물을 파는 것이고 다른 하나는 이미 물을 대고 있는 다른 논으로부터 물을 끌어오는 법이다.

각각의 논에 대해 우물을 파는 비용과 논들 사이에 물을 끌어오는 비용들이 주어졌을 때 최소의 비용으로 모든 논에 물을 대는 것이 문제이다.
### **입력**
첫 줄에는 논의 수 N(1 ≤ N ≤ 300)이 주어진다. 다음 N개의 줄에는 i번째 논에 우물을 팔 때 드는 비용 Wi(1 ≤ Wi ≤ 100,000)가 순서대로 들어온다. 다음 N개의 줄에 대해서는 각 줄에 N개의 수가 들어오는데 이는 i번째 논과 j번째 논을 연결하는데 드는 비용 Pi,j(1 ≤ Pi,j ≤ 100,000, Pi,j = Pj,i, Pi,i = 0)를 의미한다.
### **출력**
첫 줄에 모든 논에 물을 대는데 필요한 최소비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
5
4
4
3
0 2 2 2
2 0 3 3
2 3 0 4
2 3 4 0
```

**예제 출력1**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

N = int(input())
W = [int(input()) for _ in range(N)]
table = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N

pq = []

for i in range(N):
    heappush(pq, (W[i], i))

answer = 0
count = 0

while pq and count < N:
    cost, u = heappop(pq)
    if visited[u]:
        continue

    visited[u] = True
    answer += cost
    count += 1

    for v in range(N):
        if not visited[v]:
            heappush(pq, (table[u][v], v))

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|41016|96|Python3|505
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
```

### **다른 풀이**

```python
import sys
import heapq

input = sys.stdin.readline

N = int(input())
# 각 집에서 우물을 파는 비용 (가상의 노드 0과 연결하는 비용)
well = [int(input()) for _ in range(N)]
# 집과 집 사이의 파이프 설치 비용
road = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
visited = [False] * (N+1)  # 1번부터 N번 집, 가상의 노드 0은 시작 노드로 처리
dist = [INF] * (N+1)  # 각 집을 MST에 연결하는 최소 비용
pq = []  # (비용, 노드) 형태의 우선순위 큐

# 가상의 노드 0에서 각 집으로 연결하는 비용은 우물 비용입니다.
# 노드 번호를 1부터 사용하므로, 초기 dist[i] = well[i-1]으로 설정합니다.
for i in range(1, N+1):
    dist[i] = well[i-1]
    heapq.heappush(pq, (dist[i], i))

total_cost = 0
while pq:
    cost, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True
    total_cost += cost

    # 현재 노드 u와 연결된 다른 집 v에 대해
    # MST에 연결되지 않은 노드 v의 연결 비용을 road[u-1][v-1]과 비교하여 갱신합니다.
    for v in range(1, N+1):
        if not visited[v] and road[u-1][v-1] < dist[v]:
            dist[v] = road[u-1][v-1]
            heapq.heappush(pq, (dist[v], v))

print(total_cost)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mathnobi|37556|64|Python3|1301
#### **📝해설**

```python
from heapq import heappush, heappop

# 입력받기
N = int(input())
W = [int(input()) for _ in range(N)]
table = [list(map(int, input().split())) for _ in range(N)]

# i번 논이 물이 대져있는지 확인하는 리스트
visited = [False] * N

# pq를 통해 MST 구현(비용, 논 번호)
pq = []

# 일단 모든 논을 힙에 저장
for i in range(N):
    heappush(pq, (W[i], i))

# 비용, 횟수
answer = 0
count = 0

# mst를 구현
while pq and count < N:

    # 현재 비용, 노드
    cost, u = heappop(pq)

    # 이미 물이 대져있다면 넘어감
    if visited[u]:
        continue

    # 현재 방문처리
    visited[u] = True

    # 비용 추가
    answer += cost
    count += 1

    # 다른 논들을 확인했을 때
    for v in range(N):

        # 아직 물이 대져있지 않다면 힙에 추가
        if not visited[v]:
            heappush(pq, (table[u][v], v))

print(answer)
```