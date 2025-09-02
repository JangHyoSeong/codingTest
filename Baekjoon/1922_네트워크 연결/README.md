# [1922] 네트워크 연결

### **난이도**
골드 4
## **📝문제**
도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다. 하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다. 그런데 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다. (a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다. a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)

그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야 컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다. 이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 모든 컴퓨터를 연결할 수 없는 경우는 없다.
### **입력**
첫째 줄에 컴퓨터의 수 N (1 ≤ N ≤ 1000)가 주어진다.

둘째 줄에는 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)가 주어진다.

셋째 줄부터 M+2번째 줄까지 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용이 주어진다. 이 비용의 정보는 세 개의 정수로 주어지는데, 만약에 a b c 가 주어져 있다고 하면 a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 든다는 것을 의미한다. a와 b는 같을 수도 있다.
### **출력**
모든 컴퓨터를 연결하는데 필요한 최소비용을 첫째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
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

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
        return True
    
    return False


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N+1)]
total_cost = 0
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|125072|316|PyPy3|754
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
```

### **다른 풀이**

```python
import sys


def find_set(parents, n):
    if parents[n] != n:
        parents[n] = find_set(parents, parents[n])
    return parents[n]


def union(parents, a, b):
    parent_a = find_set(parents, a)
    parent_b = find_set(parents, b)
    if parent_a == parent_b:
        return False
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b
    return True


def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n + 1)]
    answer = 0
    count = 0
    for u, v, weight in edges:
        if union(parents, u, v):
            answer += weight
            count += 1
        if count == n - 1:
            break

    print(answer)


solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
srlckl1814|47804|156|Python3
#### **📝해설**

```python
import sys

# 부모 노드 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

# 두 노드의 집합을 합치는 함수
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
        return True
    
    return False


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

# 가중치를 우선으로 각 간선 정보를 저장
edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

# 가중치를 기준으로 정렬
edges.sort()

# 부모 노드
parent = [i for i in range(N+1)]
total_cost = 0

# 정렬된 가중치를 기준으로 하나의 집합으로 합침
for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost

print(total_cost)
```