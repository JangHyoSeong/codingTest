# [14621] 나만 안되는 연애

### **난이도**
골드 3
## **📝문제**
깽미는 24살 모태솔로이다. 깽미는 대마법사가 될 순 없다며 자신의 프로그래밍 능력을 이용하여 미팅 어플리케이션을 만들기로 결심했다. 미팅 앱은 대학생을 타겟으로 만들어졌으며 대학교간의 도로 데이터를 수집하여 만들었다.

이 앱은 사용자들을 위해 사심 경로를 제공한다. 이 경로는 3가지 특징을 가지고 있다.

1. 사심 경로는 사용자들의 사심을 만족시키기 위해 남초 대학교와 여초 대학교들을 연결하는 도로로만 이루어져 있다.
2. 사용자들이 다양한 사람과 미팅할 수 있도록 어떤 대학교에서든 모든 대학교로 이동이 가능한 경로이다.
시간을 낭비하지 않고 미팅할 수 있도록 이 경로의 길이는 최단 거리가 되어야 한다.
3. 만약 도로 데이터가 만약 왼쪽의 그림과 같다면, 오른쪽 그림의 보라색 선과 같이 경로를 구성하면 위의 3가지 조건을 만족하는 경로를 만들 수 있다.

이때, 주어지는 거리 데이터를 이용하여 사심 경로의 길이를 구해보자.
### **입력**
입력의 첫째 줄에 학교의 수 N와 학교를 연결하는 도로의 개수 M이 주어진다. (2 ≤ N ≤ 1,000) (1 ≤ M ≤ 10,000)

둘째 줄에 각 학교가 남초 대학교라면 M, 여초 대학교라면 W이 주어진다.

다음 M개의 줄에 u v d가 주어지며 u학교와 v학교가 연결되어 있으며 이 거리는 d임을 나타낸다. (1 ≤ u, v ≤ N) , (1 ≤ d ≤ 1,000)
### **출력**
깽미가 만든 앱의 경로 길이를 출력한다. (모든 학교를 연결하는 경로가 없을 경우 -1을 출력한다.)
### **예제입출력**

**예제 입력1**

```
5 7
M W W W M
1 2 12
1 3 10
4 2 5
5 2 5
2 5 10
3 4 3
5 4 7
```

**예제 출력1**

```
34
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
# 유니온-파인드(Union-Find) 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# 입력 처리
N, M = map(int, input().split())
schools = ['0'] + input().split()  # 학교 정보, 남초(M) 여초(W)

edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if schools[u] != schools[v]:  # 남초-여초 학교 간 연결만 허용
        edges.append((d, u, v))

# 크루스칼 알고리즘을 사용하여 최소 신장 트리(MST) 구성
edges.sort()  # 거리를 기준으로 오름차순 정렬
parent = [i for i in range(N + 1)]  # 유니온-파인드용 부모 배열
rank = [0] * (N + 1)

mst_weight = 0
edge_count = 0

for edge in edges:
    weight, u, v = edge
    if find(parent, u) != find(parent, v):  # 사이클이 생기지 않도록 체크
        union(parent, rank, u, v)
        mst_weight += weight
        edge_count += 1
        if edge_count == N - 1:  # N-1개의 간선을 선택하면 MST 완성
            break

# 결과 출력
if edge_count == N - 1:
    print(mst_weight)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111588|132|PyPy3|1456
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
2. 유니온 파인드
3. 크루스칼 알고리즘
```
### **다른 풀이**

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mw = [1 if i == 'M' else 0 for i in input().split()]
g = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if mw[u - 1] + mw[v - 1] == 1:
        edges.append((u - 1, v - 1, d))

edges.sort(key=lambda x: x[2])

par = [i for i in range(n)]


def find(a):
    if par[a] == a:
        return a
    p = find(par[a])
    par[a] = p
    return p


def merge(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    par[b] = a
    return True


ans = 0
cnt = 0
for u, v, d in edges:
    if merge(u, v):
        ans += d
        cnt += 1

if cnt == n - 1:
    print(ans)
else:
    print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
imjaegon|32140|44|Python3|721