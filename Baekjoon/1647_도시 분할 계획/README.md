# [1647] 도시 분할 계획

### **난이도**
골드 4
## **📝문제**
동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그러다가 평화로운 마을에 가게 되었는데, 그곳에서는 알 수 없는 일이 벌어지고 있었다.

마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 각 길마다 길을 유지하는데 드는 유지비가 있다. 임의의 두 집 사이에 경로가 항상 존재한다.

마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다. 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.

그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다. 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다. 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다. 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.

임의의 두 집 사이에 경로가 항상 존재하는 입력만 주어진다.
### **출력**
첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
```

**예제 출력1**

```
8
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
parent = [i for i in range(N + 1)]
total = 0
max_cost = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost
        max_cost = max(max_cost, cost)

print(total - max_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|268416|4008|PyPy3|699
#### **📝해설**

**알고리즘**
```
1. 최소 신장 트리
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
p = [i for i in range(N+1)]
x=[[] for _ in range(1001)]
answer = 0

def par(n):
    if p[n] == n:
        return n
    p[n] = par(p[n])
    return p[n]

for i in range(M):
    a, b, c = map(int,input().split())
    x[c].append([a,b])

for i in range(1,1001):
    if N == 2:
        break
    for b, c in x[i]:
        if N == 2:
            break
        b = par(b)
        c = par(c)
        if b == c:
            continue
        p[b] = c
        answer += i
        N -= 1

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tyoungs|222376|1004|PyPy3|564
#### **📝해설**

```python
import sys

'''
최소 스패닝 트리를 만든 뒤, 가장 가중치가 큰 간선을 끊으면
가중치가 최소가 되도록 두 마을로 나눌 수 있다
'''
N, M = map(int, sys.stdin.readline().rstrip().split())

# 입력받기
edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

# 유니온파인드 부모 노드를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드를 합치는 함수
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 가중치 기준으로 정렬
edges.sort()

# 각 노드의 부모 노드
parent = [i for i in range(N + 1)]

# 총 간선 가중치
total = 0

# 간선 중 가장 큰 가중치
max_cost = 0

# 간선들을 확인하면서
for cost, a, b in edges:

    # 아직 하나의 집합이 아니라면, 합침
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost
        max_cost = max(max_cost, cost)

# 간선의 가중치가 가장 큰 값을 뺌
print(total - max_cost)
```