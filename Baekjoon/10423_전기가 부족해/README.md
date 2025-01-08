# [10423] 전기가 부족해

### **난이도**
골드 3
## **📝문제**
세계에서 GDP가 가장 높은 서강 나라는 소프트웨어와 하드웨어 기술이 모두 최고라서 IT강국이라 불리고, 2015년부터 세상에서 가장 살기 좋은 나라 1등으로 꼽히고 있다. 

살기 좋은 나라 1등으로 꼽힌 이후 외국인 방문객들이 많아졌고, 그에 따라 전기 소비율이 증가하여 전기가 많이 부족한 상황이 되었다. 따라서 서강 나라의 대통령은 최근 개발이 완료된 YNY발전소 프로젝트를 진행 하기로 하였다. 발전소를 만들 때 중요한 것은 발전소 건물과 도시로 전기를 공급해 줄 케이블이다. 발전소는 이미 특정 도시에 건설되어 있고, 따라서 추가적으로 드는 비용은 케이블을 설치할 때 드는 비용이 전부이다. 이 프로젝트의 문제는 케이블을 설치할 때 드는 비용이 굉장히 크므로 이를 최소화해서 설치하여 모든 도시에 전기를 공급하는 것이다. 여러분은 N개의 도시가 있고 M개의 두 도시를 연결하는 케이블의 정보와 K개의 YNY발전소가 설치된 도시가 주어지면 케이블 설치 비용을 최소로 사용하여 모든 도시에 전기가 공급할 수 있도록 해결해야 한다. 중요한 점은 어느 한 도시가 두 개의 발전소에서 전기를 공급받으면 낭비가 되므로 케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다. 아래 Figure 1를 보자. 9개의 도시와 3 개의 YNY발전소(A,B,I)가 있고, 각각의 도시들을 연결할 때 드는 비용이 주어진다.


![img](https://www.acmicpc.net/upload/images2/E1.png)
Figure 1


![img](https://www.acmicpc.net/upload/images2/E2.png)
Figure 2

이 예제에서 모든 도시에 전기를 공급하기 위하여 설치할 케이블의 최소 비용은 22이고, Figure 2의 굵은 간선이 연결한 케이블이다. B 도시는 연결된 도시가 하나도 없지만, 발전소가 설치된 도시는 전기가 공급될 수 있기 때문에 상관없다.
### **입력**
첫째 줄에는 도시의 개수 N(1 ≤ N ≤ 1,000)과 설치 가능한 케이블의 수 M(1 ≤ M ≤ 100,000)개, 발전소의 개수 K(1 ≤ K ≤ N)개가 주어진다. 둘째 줄에는 발전소가 설치된 도시의 번호가 주어진다. 셋째 줄부터 M개의 두 도시를 연결하는 케이블의 정보가 u, v, w로 주어진다. 이는 u도시와 v도시를 연결하는 케이블을 설치할 때 w의 비용이 드는 것을 의미한다. w는 10,000보다 작거나 같은 양의 정수이다.
### **출력**
모든 도시에 전기를 공급할 수 있도록 케이블을 설치하는 데 드는 최소비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
9 14 3
1 2 9
1 3 3
1 4 8
2 4 10
3 4 11
3 5 6
4 5 4
4 6 10
5 6 5
5 7 4
6 7 7
6 8 4
7 8 5
7 9 2
8 9 5
```

**예제 출력1**

```
22
```

**예제 입력2**

```
4 5 1
1
1 2 5
1 3 5
1 4 5
2 3 10
3 4 10
```

**예제 출력2**

```
15
```

**예제 입력3**

```
10 9 5
1 4 6 9 10
1 2 3
2 3 8
3 4 5
4 5 1
5 6 2
6 7 6
7 8 3
8 9 4
9 10 1
```

**예제 출력3**

```
16
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        else:
            parent[root_y] = root_x
            rank[root_x] += 1


N, M, K = map(int, sys.stdin.readline().rstrip().split())
generators = list(map(int, sys.stdin.readline().rstrip().split()))

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x : x[2])

parent = list(range(N+1))
rank = [0] * (N+1)

virtual_node = 0
for generator in generators:
    union(parent, rank, virtual_node, generator)

min_cost = 0
for u, v, w in edges:
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        min_cost += w

print(min_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|122072|292|PyPy3|986
#### **📝해설**

**알고리즘**
```
1. MST
2. 크루스칼 알고리즘
```

### **다른 풀이**

```python
# MST - 10423번 - 전기가 부족해
import sys
from heapq import *

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e, e_num = map(int, input().split())
electric = list(map(int, input().split()))
edges = []
q = []
for i in range(e):
    s, e, c = map(int, input().split())
    heappush(q, (c, s, e))

## 발전소라면 parent가 0이다 -> 발전소를 항상 parent로 만들기 위해서!!!
cycle = [i for i in range(v+1)]
for i in electric:
    cycle[i] = 0
# print(cycle)


## 유니온 파인드
def get_parent(v):
    if cycle[v] != v:
        cycle[v] = get_parent(cycle[v])
    return cycle[v]


def union_parent(v1, v2):
    v1_parent = get_parent(v1)
    v2_parent = get_parent(v2)
    if v1_parent != v2_parent:
        if v1_parent > v2_parent:
            cycle[v1_parent] = v2_parent
        else:
            cycle[v2_parent] = v1_parent
        return True
    return False


edge_cnt = 0
ans = 0
while q:
    c, s, e = heappop(q)
    if union_parent(s, e):
        ans += c
        edge_cnt += 1
    if edge_cnt == v-e_num:
        break
print(ans)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
leedrkr323|48308|164|Python3|1084
#### **📝해설**

```python
import sys

def find(parent, x):
    # 유니온 파인드를 위한 함수 선언
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# 입력받음
N, M, K = map(int, sys.stdin.readline().rstrip().split())
generators = list(map(int, sys.stdin.readline().rstrip().split()))

# 크루스칼 알고리즘을 위해 간선을 가중치로 오름차순 정렬
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x : x[2])

# 유니온파인드를 위한 리스트 선언
parent = list(range(N+1))
rank = [0] * (N+1)

# 모든 발전소를 가상의 노드로 묶어서 간주함
# 이러면, 모든 발전소를 하나의 노드로 여길 수 있음
virtual_node = 0
for generator in generators:
    union(parent, rank, virtual_node, generator)

# 최소 비용을 위한 변수
min_cost = 0

# 모든 간선을 순회하면서
for u, v, w in edges:

    # 사이클에 속하지 않았다면
    if find(parent, u) != find(parent, v):

        # 하나의 집합으로 합치고, 최소비용을 더함
        union(parent, rank, u, v)
        min_cost += w

# 최소비용 계산
print(min_cost)
```

### **🔖정리**

1. 크루스칼 알고리즘을 사용할 때, 출발 노드가 여러개라면 하나의 노드로 묶어야 한다는 것을 알았다.