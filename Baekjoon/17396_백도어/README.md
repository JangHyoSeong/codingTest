# [17396] 백도어

### **난이도**
골드 5
## **📝문제**
유섭이는 무척이나 게으르다. 오늘도 할 일을 모두 미뤄둔 채 열심히 롤을 하던 유섭이는 오늘까지 문제를 내야 한다는 사실을 깨달았다. 그러나 게임은 시작되었고 지는 걸 무척이나 싫어하는 유섭이는 어쩔 수 없이 백도어를 해 게임을 최대한 빠르게 끝내기로 결심하였다.

최대한 빨리 게임을 끝내고 문제를 출제해야 하기 때문에 유섭이는 최대한 빨리 넥서스가 있는 곳으로 달려가려고 한다. 유섭이의 챔피언은 총 N개의 분기점에 위치할 수 있다. 0번째 분기점은 현재 유섭이의 챔피언이 있는 곳을, N-1 번째 분기점은 상대편 넥서스를 의미하며 나머지 1, 2, ..., N-2번째 분기점은 중간 거점들이다. 그러나 유섭이의 챔피언이 모든 분기점을 지나칠 수 있는 것은 아니다. 백도어의 핵심은 안 들키고 살금살금 가는 것이기 때문에 적 챔피언 혹은 적 와드(시야를 밝혀주는 토템), 미니언, 포탑 등 상대의 시야에 걸리는 곳은 지나칠 수 없다.

입력으로 각 분기점을 지나칠 수 있는지에 대한 여부와 각 분기점에서 다른 분기점으로 가는데 걸리는 시간이 주어졌을 때, 유섭이가 현재 위치에서 넥서스까지 갈 수 있는 최소 시간을 구하여라.
### **입력**
첫 번째 줄에 분기점의 수와 분기점들을 잇는 길의 수를 의미하는 두 자연수 N과 M이 공백으로 구분되어 주어진다.(1 ≤ N ≤ 100,000, 1 ≤ M ≤ 300,000)

두 번째 줄에 각 분기점이 적의 시야에 보이는지를 의미하는 N개의 정수 a0, a1, ..., aN-1가 공백으로 구분되어 주어진다. ai가 0이면 i 번째 분기점이 상대의 시야에 보이지 않는다는 뜻이며, 1이면 보인다는 뜻이다. 추가적으로 a0 = 0, aN-1 = 1이다., N-1번째 분기점은 상대 넥서스이기 때문에 어쩔 수 없이 상대의 시야에 보이게 되며, 또 유일하게 상대 시야에 보이면서 갈 수 있는 곳이다.

다음 M개의 줄에 걸쳐 세 정수 a, b, t가 공백으로 구분되어 주어진다. (0 ≤ a, b < N, a ≠ b, 1 ≤ t ≤ 100,000) 이는 a번째 분기점과 b번째 분기점 사이를 지나는데 t만큼의 시간이 걸리는 것을 의미한다. 연결은 양방향이며, 한 분기점에서 다른 분기점으로 가는 간선은 최대 1개 존재한다.
### **출력**
첫 번째 줄에 유섭이의 챔피언이 상대 넥서스까지 안 들키고 가는데 걸리는 최소 시간을 출력한다. 만약 상대 넥서스까지 갈 수 없으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 7
0 0 0 1 1
0 1 7
0 2 2
1 2 4
1 3 3
1 4 6
2 3 2
3 4 1
```

**예제 출력1**

```
12
```

**예제 입력2**

```
5 7
0 1 0 1 1
0 1 7
0 2 2
1 2 4
1 3 3
1 4 6
2 3 2
3 4 1
```

**예제 출력2**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

N, M = map(int, input().split())
visible = list(map(int, input().split()))

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

pq = [(0, 0)]
dist = [float('inf')] * N
dist[0] = 0

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        if visible[next_node] and next_node != N - 1:
            continue

        new_dist = now_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(dist[N - 1] if dist[N - 1] != float('inf') else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|156740|688|PyPy3|762
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```
#### **📝해설**

```python
from heapq import heappush, heappop

# 입력받음
N, M = map(int, input().split())
visible = list(map(int, input().split()))

# 간선의 정보를 저장할 리스트
edges = [[] for _ in range(N)]

# 간선 정보 삽입
for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

# 다익스트라를 위한 우선순위 큐
pq = [(0, 0)]
dist = [float('inf')] * N
dist[0] = 0


# 다익스트라 시작
while pq:

    # 현재 이동거리, 현재 노드
    now_dist, now_node = heappop(pq)

    # 만약 이미 최소값보다 크다면 고려하지 않음
    if now_dist > dist[now_node]:
        continue

    # 이동할 수 있는 노드 검사
    for next_dist, next_node in edges[now_node]:

        # 갈수 없다면 고려하지 않음
        if visible[next_node] and next_node != N - 1:
            continue
        
        # 이동
        new_dist = now_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(dist[N - 1] if dist[N - 1] != float('inf') else -1)
```