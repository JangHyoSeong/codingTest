# [25187] 고인물이 싫어요

### **난이도**
골드 4
## **📝문제**
재형이는 청정수를 좋아하고 고인물을 싫어한다. 오늘도 청정수를 구하기 위해 물탱크들이 있는 마을에 방문한다.

마을에는 
$N$개의 물탱크가 존재하고, 각 물탱크는 청정수 또는 고인물을 저장하고 있다. 그리고 물탱크는 공급의 편의를 위해 
$M$개의 파이프로 서로 연결되어 있다.

청정수를 얻기 위해 
$K$번 물탱크에 방문했을 때, 
$K$번 물탱크와 
$K$번 물탱크에서 
$0$개 이상의 파이프를 거쳐 이동 가능한 물탱크 중, 청정수가 담긴 물탱크의 수가 고인물이 담긴 물탱크의 수보다 더 많은 경우 청정수를 얻을 수 있다.

방문할 예정인 물탱크에 대한 정보가 주어질 때마다, 청정수를 얻을 수 있는지 구해보자. 
### **입력**
첫째 줄에 물탱크의 수 
$N(1 \leq N \leq 100\,000)$과 파이프의 수 
$M(0 \leq M \leq 200\,000)$, 그리고 물탱크에 방문할 횟수 
$Q(1 \leq Q \leq 100\,000)$가 주어진다. 

둘째 줄에 
$1$번부터 
$N$번 물탱크까지 순서대로 들어있는 물의 종류가 주어진다. 청정수는 1, 고인물은 0으로 주어진다. 

다음 
$3$번째부터 
$M+2$번째 줄까지 파이프가 연결하는 두 물탱크의 번호 
$u, v(1\leq u, v \leq N, u \neq v)$가 주어진다. 같은 두 물탱크를 연결하는 파이프가 여러 개 존재할 수 있다. 

 
$M+3$번째부터 
$M+Q+2$번째 줄까지 방문할 물탱크의 번호 
$K(1 \leq K \leq N)$가 주어진다.  
### **출력**
 
$Q$개의 줄에 각 물탱크에 방문했을 때 청정수를 얻을 수 있다면 1을, 아니면 0을 주어진 정보 순서대로 출력한다. 
### **예제입출력**

**예제 입력1**

```
5 3 3
1 0 1 1 0
1 2
3 4
4 5
1
5
4
```

**예제 출력1**

```
0
1
1
```

**예제 입력2**

```
5 5 3
1 0 1 1 0
1 2
1 3
1 4
2 3
3 4
1
5
4
```

**예제 출력2**

```
1
0
1
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M, Q = map(int, sys.stdin.readline().rstrip().split())
water = list(map(int, sys.stdin.readline().rstrip().split()))
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

parent = list(range(N))
size = [1] * N
clean_count = [water[i] for i in range(N)]
dirty_count = [1-water[i] for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        clean_count[root_x] += clean_count[root_y]
        dirty_count[root_x] += dirty_count[root_y]

for pipe in pipes:
    union(pipe[0]-1, pipe[1]-1)

for query in queries:
    query -= 1
    root_query = find(query)

    if clean_count[root_query] > dirty_count[root_query]:
        print(1)
    else:
        print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|142948|408|PyPy3|1063
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, Q = map(int, input().split())
    water = [-1] + [*map(int, input().split())]
    R = [-1] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur < vr:
            water[ur] += water[vr]
            R[ur] += R[vr]
            R[vr] = ur
        elif ur > vr:
            water[vr] += water[ur]
            R[vr] += R[ur]
            R[ur] = vr
    for _ in range(Q):
        K = int(input())
        kr = find_root(K, R)
        print(1 if -R[kr] // 2 < water[kr] else 0)

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tkqmfp26|33832|308|Python3|735
#### **📝해설**

```python
import sys

# 입력받기
N, M, Q = map(int, sys.stdin.readline().rstrip().split())
water = list(map(int, sys.stdin.readline().rstrip().split()))
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

# 분리집합의 부모를 저장할 리스트
parent = list(range(N))

# 파이프로 연결된 물탱크의 수를 저장할 리스트
size = [1] * N

# 청정수와 고인물의 개수를 저장할 리스트
clean_count = [water[i] for i in range(N)]
dirty_count = [1-water[i] for i in range(N)]

# 입력받은 노드의 부모를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 노드를  합치는 함수
def union(x, y):

    # 두 노드의 부모를 찾음
    root_x = find(x)
    root_y = find(y)

    # 같은 집합이 아니라면
    if root_x != root_y:

        # 항상 큰 노드가 앞으로 가게끔 함
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x

        # 부모, 크기, 청정수, 고인물의 숫자를 합쳐줌
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        clean_count[root_x] += clean_count[root_y]
        dirty_count[root_x] += dirty_count[root_y]

for pipe in pipes:
    union(pipe[0]-1, pipe[1]-1)

for query in queries:
    query -= 1
    root_query = find(query)

    # 청정수가 고인물보다 많으면 1출력, 아니라면 0출력
    if clean_count[root_query] > dirty_count[root_query]:
        print(1)
    else:
        print(0)
```

### **🔖정리**

1. 배운점