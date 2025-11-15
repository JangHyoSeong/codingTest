# [1197] 최소 스패닝 트리

### **난이도**
골드 4
## **📝문제**
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
### **입력**
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
### **출력**
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 2 1
2 3 2
1 3 3
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        
        return True
    return False

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(V+1))

total_cost = 0
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|50824|312|Python3|757
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = list(range(v + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[b] = a
    return True

ans = 0
for cost, a, b in edges:
    if union(a, b):
        ans += cost

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
djtka97|49576|288|Python3|531
#### **📝해설**

```python
import sys
sys.setrecursionlimit(10**6)

# 최소 스패닝 트리 kruskal 알고리즘을 위한 유니온파인드
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        
        return True
    return False

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []

# 간선정보 입력
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # 가중치로 정렬하기 위해 가중치를 맨 앞으로 이동
    edges.append((c, a, b))

# 가중치 기준으로 정렬
edges.sort()

parent = list(range(V+1))

# 총 가격
total_cost = 0

# 최소 스패닝 트리를 만듦
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)
```