# [14950] 정복자

### **난이도**
골드4
## **📝문제**
서강 나라는 N개의 도시와 M개의 도로로 이루어졌다. 모든 도시의 쌍에는 그 도시를 연결하는 도로로 구성된 경로가 있다. 각 도로는 양방향 도로이며, 각 도로는 사용하는데 필요한 비용이 존재한다. 각각 도시는 1번부터 N번까지 번호가 붙여져 있다. 그 중에서 1번 도시의 군주 박건은 모든 도시를 정복하고 싶어한다.

처음 점거하고 있는 도시는 1번 도시 뿐이다. 만약 특정 도시 B를 정복하고 싶다면, B와 도로로 연결된 도시들 중에서 적어도 하나를 정복하고 있어야 한다. 조건을 만족하는 도시 중에서 하나인 A를 선택하면, B를 정복하는 과정에서 A와 B를 연결하는 도로의 비용이 소모된다. 박건은 한번에 하나의 도시만 정복을 시도하고 언제나 성공한다. 한 번 도시가 정복되면, 모든 도시는 경계를 하게 되기 때문에 모든 도로의 비용이 t만큼 증가하게 된다. 한 번 정복한 도시는 다시 정복하지 않는다.

이때 박건이 모든 도시를 정복하는데 사용되는 최소 비용을 구하시오.
### **입력**
첫째 줄에 도시의 개수 N과 도로의 개수 M과 한번 정복할 때마다 증가하는 도로의 비용 t가 주어진다. N은 10000보다 작거나 같은 자연수이고, M은 30000보다 작거나 같은 자연수이다. t는 10이하의 자연수이다.

M개의 줄에는 도로를 나타내는 세 자연수 A, B, C가 주어진다. A와 B사이에 비용이 C인 도로가 있다는 뜻이다. A와 B는 N이하의 서로 다른 자연수이다. C는 10000 이하의 자연수이다.
### **출력**
모든 도시를 정복하는데 사용되는 최소 비용을 출력하시오.
### **예제입출력**

**예제 입력1**

```
4 5 8
1 2 3
1 3 2
2 3 2
2 4 4
3 4 1
```

**예제 출력1**

```
29
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush

N, M, t = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

total_cost = 0
visited = [False] * (N+1)
heap = []
visited_cities = 1
current_increase = 0

visited[1] = True
for cost, next in edges[1]:
    heappush(heap, (cost, next))

while visited_cities < N:
    cost, city = heappop(heap)

    if visited[city]:
        continue

    total_cost += cost + current_increase
    visited[city] = True
    visited_cities += 1
    current_increase += t

    for next_cost, next in edges[city]:
        if not visited[next]:
            heappush(heap, (next_cost, next))

print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116680|232|PyPy3|745
#### **📝해설**

**알고리즘**
```
1. 최소 신장 트리
2. 프림 알고리즘
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_by_rank(parent, rank, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:
        return False

    if rank[a] < rank[b]:
        a, b = b, a

    parent[b] = a

    if rank[a] == rank[b]:
        rank[a] += 1

    return True

def solution(N, M, t, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    cnt = 0
    answer = (N - 2) * (N - 1) // 2 * t
    for a, b, c in edges:
        if not union_by_rank(parent, rank, a, b):
            continue
        cnt += 1
        answer += c
        if cnt == N - 1:
            break

    return answer


if __name__ == "__main__":
    N, M, t = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    answer = solution(N, M, t, edges)
    print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
arkddkwl2029|38528|88|Python3|1006
#### **📝해설**

```python
from heapq import heappop, heappush

N, M, t = map(int, input().split())
edges = [[] for _ in range(N+1)]

# 힙을 사용하기 위해 가중치를 앞에두고 간선 정보 삽입
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

# 방문도시, 총비용 등 선언
total_cost = 0
visited = [False] * (N+1)
heap = []
visited_cities = 1
current_increase = 0

# 첫 도시는 방문처리
visited[1] = True

# 첫 도시에서 갈 수 있는 곳을 힙에 push
for cost, next in edges[1]:
    heappush(heap, (cost, next))


# 모든 도시를 방문할 때까지
while visited_cities < N:

    # 힙에서 pop
    cost, city = heappop(heap)

    # 방문했던 도시라면 continue
    if visited[city]:
        continue

    # 방문하지 않았던 도시라면 방문처리.
    total_cost += cost + current_increase
    visited[city] = True
    visited_cities += 1
    current_increase += t

    # 이 도시에서 갈 수 있는 도시들을 힙에 삽입
    for next_cost, next in edges[city]:
        if not visited[next]:
            heappush(heap, (next_cost, next))

# 출력
print(total_cost)
```