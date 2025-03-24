# [14938] 서강그라운드

### **난이도**
골드 4
## **📝문제**
예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다. 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다. 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다. 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는 낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만 어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.

각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다. 예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.

[이미지](https://upload.acmicpc.net/ef3a5124-833a-42ef-a092-fd658bc8e662/-/preview/)

주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. ( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다) 예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다. (4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.) 이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.
### **입력**
첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.

둘째 줄에는 n개의 숫자가 차례대로 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.

세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.

지역의 번호는 1이상 n이하의 정수이다. 두 지역의 번호가 같은 경우는 없다.
### **출력**
예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3
```

**예제 출력1**

```
23
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N, M, R = map(int, sys.stdin.readline().rstrip().split())
items = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((l, b))
    edges[b].append((l, a))

max_item = 0
for i in range(1, N+1):
    dist = [int(21e8)] * (N+1)
    dist[i] = 0

    pq = [(0, i)]

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist

    temp_item = 0
    for i in range(1, N+1):
        if dist[i] <= M:
            temp_item += items[i]

    max_item = max(max_item, temp_item)

print(max_item)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112020|152|PyPy3|965
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
def dfs(s):
    global ans
    stack = []
    stack.append([0,s])
    v_cost_lst = [float('inf')] * (N + 1)
    v_lst = [0] * (N + 1)
    v_cost_lst[s] = 0
    v_lst[s] = 1
    while stack:
        c_cost, c_position = stack.pop()
        if v_cost_lst[c_position] < c_cost:
            continue
        for cost, n_position in edge_lst[c_position]:
            n_cost = cost + c_cost
            if n_cost <= M and v_cost_lst[n_position] > n_cost:
                v_cost_lst[n_position] = n_cost
                v_lst[n_position] = 1
                stack.append([n_cost, n_position])
    cnt = 0
    for i in range(1,1+N):
        if v_lst[i]:
            cnt += item_lst[i]
    ans = max(cnt, ans)
    return


N, M, R = map(int,input().split())
item_lst = [0] + list(map(int,input().split()))
edge_lst = [[]for _ in range(N+1)]
for _ in range(R):
    p, c, f_cost = map(int,input().split())
    edge_lst[p].append([f_cost,c])
    edge_lst[c].append([f_cost,p])
ans = 0
for i in range(1,1+N):
    dfs(i)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wasdl|31120|32|Python3|1017
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

N, M, R = map(int, sys.stdin.readline().rstrip().split())
items = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

# 간선 정보를 저장할 리스트
edges = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((l, b))
    edges[b].append((l, a))

# 최대로 획득할 수 있는 아이템 개수
max_item = 0

# 모든 노드에서 부터 다익스트라 알고리즘을 적용
for i in range(1, N+1):

    # 간선까지 거리
    dist = [int(21e8)] * (N+1)

    # 시작점은 0으로 초기화
    dist[i] = 0
    
    # 다익스트라 사용을 위한 우선순위 큐 (간선 거리, 현재 노드)
    pq = [(0, i)]

    # 다익스트라 알고리즘
    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist

    # 이번 노드에서 획득할 수 있는 아이템 개수
    temp_item = 0
    for i in range(1, N+1):
        if dist[i] <= M:
            temp_item += items[i]

    max_item = max(max_item, temp_item)

print(max_item)
```