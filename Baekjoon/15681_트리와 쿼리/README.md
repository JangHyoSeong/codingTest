# [15681] 트리와 쿼리

### **난이도**
골드 5
## **📝문제**
간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.

- 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.  
만약 이 문제를 해결하는 데에 어려움이 있다면, 하단의 힌트에 첨부한 문서를 참고하자.
### **입력**
트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)

이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)

이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.

이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)

입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.
### **출력**
Q줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력한다.
### **예제입출력**

**예제 입력1**

```
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8
```

**예제 출력1**

```
9
4
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

queries = [int(sys.stdin.readline()) for _ in range(Q)]

dp = [0] * (N + 1)

def dfs(node, parent):
    dp[node] = 1
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node] += dp[child]

dfs(R, -1)

print("\n".join(str(dp[u]) for u in queries))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|73480|348|Python3|536
#### **📝해설**

**알고리즘**
```
1. DFS
2. DP
3. 트리
```

### **다른 풀이**

```python
def main():
    import os
    import io

    stdin = io.BufferedReader(io.FileIO(0), 1 << 18)
    N, R, Q = map(int, stdin.readline().split())
    head = [-1] * (N + 1)
    link = []
    ep = []
    for i in range(N - 1):
        u, v = map(int, stdin.readline().split())
        link.append(head[u])
        link.append(head[v])
        head[u] = i * 2
        head[v] = i * 2 + 1
        ep.append(v)
        ep.append(u)
    sz = [1] * (N + 1)
    dfsu = [R]
    dfse = [head[R]]
    dfsr = [-1]
    while dfse:
        e = dfse[-1]
        if e == -1:
            dfse.pop()
            dfsr.pop()
            v = dfsu.pop()
            if dfsu:
                sz[dfsu[-1]] += sz[v]
        else:
            dfse[-1] = link[e]
            if e == dfsr[-1]:
                continue
            v = ep[e]
            dfsu.append(v)
            dfse.append(head[v])
            dfsr.append(e ^ 1)
    os.write(1, " ".join(str(sz[int(u)]) for u in stdin).encode("ascii"))
    os._exit(0)


main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|138888|164|PyPy3|999
#### **📝해설**

```python
import sys
# 재귀함수 사용시 recursionError를 방지하기 위해 재귀 횟수를 늘려줌
sys.setrecursionlimit(10**6)

# 입력
N, R, Q = map(int, sys.stdin.readline().split())

# 트리의 간선정보를 저장할 리스트
tree = [[] for _ in range(N + 1)]

# 간선정보 저장
for _ in range(N-1):
    # 입출력 이많아서 stdin으로 입력해줌
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

# 쿼리 저장할 리스트
queries = [int(sys.stdin.readline()) for _ in range(Q)]

# 각 노드의 서브트리 정점의 개수를 저장할 리스트
dp = [0] * (N + 1)

# DFS를 통해 각 노드의 정점을 구함
def dfs(node, parent):

    # 일단 1로 초기화
    dp[node] = 1

    # 자식들을 모두 살피면서
    for child in tree[node]:

        # 자식이 있다면
        if child != parent:

            # 자식으로 이동
            dfs(child, node)

            # 현재 노드의 자식 노드 정점의 개수를 더함
            dp[node] += dp[child]

# DFS 시작
dfs(R, -1)

# 출력
print("\n".join(str(dp[u]) for u in queries))
```

### **🔖정리**

1. 이유없이 시간초과가 나면 입출력을 바꿔보자