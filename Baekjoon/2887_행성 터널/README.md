# [2887] 행성 터널

### **난이도**
플래티넘 5
## **📝문제**
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 
### **출력**
첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
```

**예제 출력1**

```
4
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
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

    return True

N = int(sys.stdin.readline().rstrip())
planets = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

edges = []
for dim in range(3):
    planets.sort(key=lambda p: p[dim])
    for i in range(N-1):
        cost = abs(planets[i][dim] - planets[i+1][dim])
        edges.append((cost, planets[i][3], planets[i+1][3]))

edges.sort()

parent = list(range(N))
total_cost = 0
count = 0

for cost, a, b in edges:
    if union(parent, a, b):
        total_cost += cost
        count += 1
        if count == N - 1:
            break

print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|167924|1264|PyPy3|893
#### **📝해설**

**알고리즘**
```
1. MST
2. 그래프
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

# 초기값 설정
N = int(input()) # 행성의 개수
planets = [] # 행성별 비용
costs = [] # 터널 비용 목록
parent = [] # 부모 목록

for i in range(N):
    x, y, z =  map(int, input().split())
    planets.append((x, y, z, i)) # i = 행성 번호
    parent.append(i) # 초기 부모는 자기 자신

#####

# find : 부모 찾기
def find(parent:list, x:int):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union : 부모를 같게 만들기
def union(parent:list, x:int, y:int):
    x = find(parent, x)
    y = find(parent, y)

    if x < y: # 둘 중 작은 쪽이 부모가 되도록 갱신
        parent[y] = x
    else:
        parent[x] = y
    
# 크루스칼 알고리즘을 이용한 행성 터널 계산
def planet_tunnel():
    for i in range(3):
        planets.sort(key=lambda x: x[i]) # 가장 차이가 적은 값끼리만 비교

        for j in range(1, N):
            costs.append((planets[j][3], planets[j-1][3], abs(planets[j][i]-planets[j-1][i])))


    costs.sort(key=lambda x:x[2])
    total_cost = 0 # 총 비용
    cnt = 0 # 연결된 수
    
    for i in range(len(costs)):
        a, b, cost = costs[i]

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            cnt += 1

        if cnt >= N-1: # 모든 노드가 연결되었으면 탐색 종료
            break

    print(total_cost)


# main
planet_tunnel()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ifindary|90240|812|Python3|1507
#### **📝해설**

```python
import sys

# 유니온파인드
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

    return True

N = int(sys.stdin.readline().rstrip())
planets = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

# 간선 정보를 하나의 리스트에 저장
edges = []

# x, y, z 세 축에 대해 모두 정렬
for dim in range(3):
    planets.sort(key=lambda p: p[dim])

    # 정렬되었을 때, 인접한 노드만이 MST를 구성하는데 사용될 가능성이 있음
    for i in range(N-1):
        cost = abs(planets[i][dim] - planets[i+1][dim])
        edges.append((cost, planets[i][3], planets[i+1][3])) # 비용, 행성1, 행성2

# 간선 정렬
edges.sort()

# 부모 노드
parent = list(range(N))
total_cost = 0
count = 0

# 모든 간선을 확인하면서
for cost, a, b in edges:

    # 노드가 합쳐졌다면
    if union(parent, a, b):

        # 비용을 더해줌
        total_cost += cost
        count += 1

        # 이미 모든 노드가 만들어졌다면 종료
        if count == N - 1:
            break

print(total_cost)
```

### **🔖정리**

1. 배운점