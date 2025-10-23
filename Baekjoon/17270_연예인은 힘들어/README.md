# [17270] 연예인은 힘들어

### **난이도**
골드 3
## **📝문제**
연예인 김영광을 너무 닮아서 길거리에서 매번 사진이 찍히는 지헌이는 사람들에게 노출되는 것을 매우 꺼려한다. 하지만 친구인 성하와 약속을 하면 성하는 매번 늦기 때문에 길거리에 나온 지헌이는 매번 성하를 기다린다. 약속 장소에서 성하에게 전화를 하면 매번 “가는 중” 이라는 대답만 듣고 기다리는 동안 길거리에서 사람들에게 사진을 찍히는 지헌이는 스트레스를 심하게 받고 있다. 참지 못한 지헌이는 성하의 핸드폰을 해킹하여서 항상 어디 있는지 알 수 있게 되었다.

스트레스가 심해진 지헌이는 성하와의 약속 장소를 바꾸려고 한다. 그 위치는 다음과 같은 조건을 만족해야 한다. 장소의 번호는 1부터 차례대로 붙어 있다.

1. 지헌이의 출발 위치와 성하의 출발 위치는 새로운 약속 장소가 될 수 없다.
2. 성품도 훌륭한 지헌이는 새로운 약속 장소는 지헌이가 걸리는 최단 시간과 성하가 걸리는 최단 시간의 합이 최소가 되도록 하고 싶다.
3. 지헌이가 더 늦게 도착하면 성하에게 안좋은 소리를 들을 것이 뻔하기에, 1번과 2번 조건을 만족하는 장소 중에서도 지헌이가 성하보다 늦게 도착하는 곳은 약속 장소가 될 수 없다.
4. 위의 세 조건을 모두 만족하는 약속 장소가 여러 곳이 있다면, 그 중에 지헌이로부터 가장 가까운 곳이 최종 약속 장소가 된다. 그런 장소도 여러 곳이 있다면, 그 중에 번호가 가장 작은 장소가 최종 약속 장소가 된다.

![이미지](https://upload.acmicpc.net/fe6c7237-d6f3-417c-9eeb-a368228bc999/-/preview/)

위와 같은 상황이 있다고 했을 때 새로 바꿀 약속 장소를 찾아보자.

- (조건 1) 3번과 6번은 지헌이와 성하의 출발지이기 때문에 새로운 약속 장소 후보에서 제외된다.
- (조건 2) 위 상황에서 성하와 지헌의 최단 거리의 합의 최소는 6분이다. 이 때, 조건을 만족하는 약속 장소는 1번, 2번, 5번, 7번이다.
- (조건 3) 5번은 성하가 먼저 도착하여서 기달리고 있기 때문에 지헌이는 꾸중을 들을 위험이 있다. 그래서 5번은 약속 장소 후보에서 제외된다.
- (조건 4) 2번 위치는 성하와 지헌이가 동시에 도착, 7번은 지헌이는 2분 걸려서 도착하고 성하는 4분 걸려서 도착한다. 1번은 지헌이는 1분, 성하는 5분 걸려서 도착한다. 따라서, 지헌이가 원하는 이상적인 약속 장소는 1번이 된다.

연예인을 닮아서 고통받는 지헌이를 위해 새로운 약속장소를 찾아주자.
### **입력**
첫 번째 줄에는 약속 장소 후보의 수 V와 약속 장소를 연결하는 총 길의 수 M이 주어진다. (2 ≤ V ≤ 100, 1 ≤ M ≤ 1,000)

그리고 다음 M개의 각 줄에는 a, b, c 가 주어진다. a, b는 길의 시작과 끝이며 c는 그 길을 지나가는 데 걸리는 시간을 나타낸다.

(1 ≤ a, b ≤ V, c는 10,000이하의 자연수, 길은 양방향이다)

그리고 그 다음 줄에는 지헌이의 위치 J 와 성하의 위치 S 가 주어진다. (1 ≤ J, S ≤ V)

지현이와 성하가 항상 만날 수 있는 입력만 주어진다.
### **출력**
연예인을 닮아서 고통받는 지헌이를 위한 이상적인 약속 장소의 위치를 출력한다. 만약 조건을 만족하는 약속 장소가 없다면 -1을 출력하라.
### **예제입출력**

**예제 입력1**

```
8 10
1 2 2
2 6 3
2 7 2
1 3 1
3 7 2
4 7 5
5 6 2
5 7 2
7 8 2
5 8 2
3 6
```

**예제 출력1**

```
1
```

**예제 입력2**

```
5 6
1 2 3
1 5 1
2 5 3
2 3 4
3 4 2
4 5 1
2 4
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

INF = int(21e8)

V, M = map(int, input().split())

edges = [[] for _ in range(V+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
J, S = map(int, input().split())

def find_min_dist(start_node):
    dist = [INF] * (V+1)
    dist[start_node] = 0

    pq = [(0, start_node)]
    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = dist[now_node] + next_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist
    
    return dist

J_dist = find_min_dist(J)
S_dist = find_min_dist(S)

min_dist = INF
min_dist_nodes = []

for v in range(1, V+1):

    if v not in [J, S]:
        now_dist_sum = J_dist[v] + S_dist[v]

        if min_dist > now_dist_sum:
            min_dist = now_dist_sum
            min_dist_nodes = [v]
        
        elif min_dist == now_dist_sum:
            min_dist_nodes.append(v)

min_J_dist = INF
answer_node = 0

for node in min_dist_nodes:
    if J_dist[node] > S_dist[node]:
        continue

    if min_J_dist > J_dist[node]:
        min_J_dist = J_dist[node]
        answer_node = node

print(answer_node if answer_node else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35508|64|Python3|1387
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
import sys, heapq
input = sys.stdin.readline

def dijkstra(G, start):
    hq = [(0, start)]
    dp = [1e9] * len(G)
    dp[start] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    V, M = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    J, S = map(int, input().split())
    jtime = dijkstra(G, J)
    stime = dijkstra(G, S)
    candi = []
    dist = 2e9
    for i in range(1, V + 1):
        if i == J or i == S:
            continue
        hap = jtime[i] + stime[i]
        if hap < dist:
            dist = hap
            candi = [i]
        elif hap == dist:
            candi.append(i)
    ans = -1
    for c in candi:
        if jtime[c] > stime[c]:
            continue
        if ans == -1 or jtime[c] < jtime[ans]:
            ans = c
    print(ans)

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tkqmfp26|33212|40|Python3|1137
#### **📝해설**

```python
from heapq import heappush, heappop

# 임의의 큰 값
INF = int(21e8)

# 입력받기
V, M = map(int, input().split())

edges = [[] for _ in range(V+1)]

# 간선정보 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
J, S = map(int, input().split())

# 다익스트라 알고리즘으로 각 노드까지의 최단거리를 구함
def find_min_dist(start_node):
    dist = [INF] * (V+1)
    dist[start_node] = 0

    pq = [(0, start_node)]
    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = dist[now_node] + next_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist
    
    # 각 노드까지의 최단거리 리스트를 리턴
    return dist

# 각각 J, S에서 시작해서 최단거리를 확인
J_dist = find_min_dist(J)
S_dist = find_min_dist(S)

# 최단 거리 합의 최소가 될 값
min_dist = INF

# 최소인 값이 여러 개인 경우, 노드들을 전부 저장
min_dist_nodes = []

# 모든 노드를 확인하면서
for v in range(1, V+1):

    # 시작 지점을 제외하고
    if v not in [J, S]:
        now_dist_sum = J_dist[v] + S_dist[v]

        # 최단 거리 갱신이 가능하다면 갱신
        if min_dist > now_dist_sum:
            min_dist = now_dist_sum
            min_dist_nodes = [v]
        
        # 거리가 같다면 노드 후보로 저장
        elif min_dist == now_dist_sum:
            min_dist_nodes.append(v)

# J가 가장 가까운 노드를 찾기 위해 확인
min_J_dist = INF
answer_node = 0

# 후보 노드들을 확인하면서
for node in min_dist_nodes:

    # J가 S보다 더 많이 이동하는 경우는 제외
    if J_dist[node] > S_dist[node]:
        continue

    # J의 최단 거리를 확인하면서 갱신
    if min_J_dist > J_dist[node]:
        min_J_dist = J_dist[node]
        answer_node = node

# 조건을 만족하는 노드가 없다면 -1 출력, 아니라면 정답 출력
print(answer_node if answer_node else -1)
```