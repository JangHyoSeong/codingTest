# [1916] 최소비용 구하기

### **난이도**
골드 5
## **📝문제**
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
### **입력**
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
### **출력**
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush

N = int(input())
M = int(input())

INF = 21e8

edges = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append([cost, end])

start, end = map(int, input().split())

pq = [(0, start)]
cost = [INF] * (N+1)
cost[start] = 0

while pq:
    now_cost, now_node = heappop(pq)

    if now_cost > cost[now_node]:
        continue

    for edge in edges[now_node]:
        next_cost, next_node = edge
        temp_sum_cost = now_cost + next_cost

        if temp_sum_cost < cost[next_node]:
            cost[next_node] = temp_sum_cost
            heappush(pq, [temp_sum_cost, next_node])

print(cost[end])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|134288|428|PyPy3|692
#### **📝해설**

**알고리즘**
```
1. 최단경로
```

### **🔖정리**

1. 중복제거를 할 때, 미리 정리하면 NlogN이지만, 다익스트라 내부에서 검사하면 pq를 통해 하기 때문에 더 빠르다