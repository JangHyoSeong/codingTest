# [3584] 가장 가까운 공통 조상

### **난이도**
골드 4
## **📝문제**
루트가 있는 트리(rooted tree)가 주어지고, 그 트리 상의 두 정점이 주어질 때 그들의 가장 가까운 공통 조상(Nearest Common Ancestor)은 다음과 같이 정의됩니다.

- 두 노드의 가장 가까운 공통 조상은, 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드를 말합니다.

![이미지](https://upload.acmicpc.net/4f2eae58-31bf-445f-a7a3-625505e7102c/-/preview/)

예를 들어 15와 11를 모두 자손으로 갖는 노드는 4와 8이 있지만, 그 중 깊이가 가장 깊은(15와 11에 가장 가까운) 노드는 4 이므로 가장 가까운 공통 조상은 4가 됩니다.

루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요
### **입력**
첫 줄에 테스트 케이스의 개수 T가 주어집니다.

각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N이 주어집니다. (2 ≤ N ≤ 10,000)

그리고 그 다음 N-1개의 줄에 트리를 구성하는 간선 정보가 주어집니다. 한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다. (당연히 정점이 N개인 트리는 항상 N-1개의 간선으로 이루어집니다!) A와 B는 1 이상 N 이하의 정수로 이름 붙여집니다.

테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.
### **출력**
각 테스트 케이스 별로, 첫 줄에 입력에서 주어진 두 노드의 가장 가까운 공통 조상을 출력합니다.
### **예제입출력**

**예제 입력1**

```
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
```

**예제 출력1**

```
4
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(100000)

def find_lca(parent, depth, a, b):
    while depth[a] > depth[b]:
        a = parent[a]
    
    while depth[b] > depth[a]:
        b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

def dfs(parent, node, d):
    depth[node] = d
    for child in tree[node]:
        dfs(parent, child, d+1)

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())

    parent = [0] * (N+1)
    depth = [0] * (N+1)
    tree = [[] for _ in range(N+1)]

    is_root = [True] * (N+1)

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        parent[b] = a
        is_root[b] = False
        tree[a].append(b)

        root = is_root.index(True, 1)

    dfs(parent, root, 0)
    a, b = map(int, sys.stdin.readline().split())
    print(find_lca(parent, depth, a, b))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|246976|216|PyPy3|926
#### **📝해설**

**알고리즘**
```
1. 최소 공통 조상(LCA)
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        parent = [0]*(N+1)
        for _ in range(N-1):
            A, B = map(int, input().split())
            parent[B] = A
        X, Y = map(int, input().split())
        visited = [False]*(N+1)
        u = X
        while u > 0:
            visited[u] = True
            u = parent[u]
        u = Y
        while not visited[u]:
            u = parent[u]
        print(u)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31120|52|Python3|514
#### **📝해설**

```python
import sys
sys.setrecursionlimit(100000)

# 최소공통조상을 찾는 함수
def find_lca(parent, depth, a, b): # parent: 각 노드의 부모를 저장하는 리스트, depth: 각 노드의 깊이를 저장하는 리스트, # a, b: 쿼리
    
    # a와 b가 같은 깊이가 될때까지 깊이를 조정
    while depth[a] > depth[b]:
        a = parent[a]
    
    while depth[b] > depth[a]:
        b = parent[b]
    
    # 같은 깊이가 되었을 때, 부모노드로 거슬러 올라가면서 공통 조상을 찾음
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

# DFS를 통해 각 노드의 깊이를 설정하는 함수
def dfs(parent, node, d):
    depth[node] = d
    for child in tree[node]:
        dfs(parent, child, d+1)

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())

    # 부모 노드를 저장할 리스트
    parent = [0] * (N+1)

    # 각 노드의 깊이를 저장할 리스트
    depth = [0] * (N+1)

    # 각 노드의 자식을 저장할 리스트
    tree = [[] for _ in range(N+1)]

    # 루트노드가 무엇인지 검사하기 위한 리스트
    is_root = [True] * (N+1)

    # 입력받으면서
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        # 부모, 자식 정보 저장
        parent[b] = a
        is_root[b] = False
        tree[a].append(b)

        # 한번도 자식이 되지 않았던 노드가 루트노드
        root = is_root.index(True, 1)

    # DFS를 통해 depth를 저장
    dfs(parent, root, 0)
    a, b = map(int, sys.stdin.readline().split())

    # 쿼리문 실행
    print(find_lca(parent, depth, a, b))
```