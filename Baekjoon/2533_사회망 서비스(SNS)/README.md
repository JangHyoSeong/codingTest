# [2533] 사회망 서비스(SNS)

### **난이도**
골드 3
## **📝문제**
페이스북, 트위터, 카카오톡과 같은 사회망 서비스(SNS)가 널리 사용됨에 따라, 사회망을 통하여 사람들이 어떻게 새로운 아이디어를 받아들이게 되는가를 이해하는 문제가 중요해졌다. 사회망에서 사람들의 친구 관계는 그래프로 표현할 수 있는데,  이 그래프에서 사람은 정점으로 표현되고, 두 정점을 잇는 에지는 두 정점으로 표현되는 두 사람이 서로 친구 관계임을 표현한다. 

예를 들어, 철수와 영희, 철수와 만수, 영희와 순희가 서로 친구 관계라면 이를 표현하는 친구 관계 그래프는 다음과 같다. 

![이미지](https://upload.acmicpc.net/c0d162b4-20d6-46eb-be8f-d06ae8bf1e9c/-/preview/)

친구 관계 그래프를 이용하면 사회망 서비스에서 어떤 새로운 아이디어가 전파되는 과정을 이해하는데 도움을 줄 수 있다. 어떤 새로운 아이디어를 먼저 받아들인 사람을 얼리 아답터(early adaptor)라고 하는데, 사회망 서비스에 속한 사람들은 얼리 아답터이거나 얼리 아답터가 아니다. 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다. 

어떤 아이디어를 사회망 서비스에서 퍼뜨리고자 할 때, 가능한 한 최소의 수의 얼리 아답터를 확보하여 모든 사람이 이 아이디어를 받아들이게 하는  문제는 매우 중요하다. 

일반적인 그래프에서 이 문제를 푸는 것이 매우 어렵다는 것이 알려져 있기 때문에, 친구 관계 그래프가 트리인 경우, 즉 모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우만 고려한다. 

예를 들어, 8명의 사람으로 이루어진 다음 친구 관계 트리를 생각해보자. 2, 3, 4번 노드가 표현하는 사람들이 얼리 아답터라면, 얼리 아답터가 아닌 사람들은 자신의 모든 친구가 얼리 아답터이기 때문에 새로운 아이디어를 받아들인다.

![이미지](https://upload.acmicpc.net/ac2e6a89-2e66-4cab-8f07-951372ef7fcc/-/preview/)

친구 관계 트리가 주어졌을 때, 모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에는 친구 관계 트리의 정점 개수 N이 주어진다. 단, 2 ≤ N ≤ 1,000,000이며, 각 정점은 1부터 N까지 일련번호로 표현된다. 두 번째 줄부터 N-1개의 줄에는 각 줄마다 친구 관계 트리의 에지 (u, v)를 나타내는 두 정수 u와 v가 하나의 빈칸을 사이에 두고 주어진다. 
### **출력**
주어진 친구 관계 그래프에서 아이디어를 전파하는데 필요한 얼리 아답터의 최소 수를 하나의 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
```

**예제 출력1**

```
3
```

**예제 입력2**

```
9
1 2
1 3
2 4
3 5
3 6
4 7
4 8
4 9
```

**예제 출력2**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    edges[u].append(v)
    edges[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1

    for child in edges[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|317400|5588|Python3|606
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
from sys import stdin
from array import array
def main():
    input = stdin.readline
    n = int(input())
    edges = [array('i') for _ in range(n+1)]
    req = array('i', (0,))*(n+1)
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        req[u], req[v] = req[u]+1, req[v]+1
    stack = array('i')
    for i in range(n+1):
        if req[i] == 1:
            stack.append(i)
    early = array('i', (0,))*(n+1)
    while stack:
        u = stack.pop()
        if early[u]:
            for v in edges[u]:
                req[v] -= 1
                if req[v] == 1:
                    stack.append(v)
        else:
            for v in edges[u]:
                req[v] -= 1
                if req[v] == 1:
                    stack.append(v)
                early[v] = 1
    print(sum(early))
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
peter5264|201440|1388|PyPy3|870
#### **📝해설**

```python
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N+1)]

# 간선 정보 저장
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    edges[u].append(v)
    edges[v].append(u)

# DP 테이블 설정. dp[node][bool] : node가 얼리어답터일 때 그 노드의 서브트리의 얼리어답터 최소 갯수
dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N + 1)

# DFS로 루트노드부터 탐색
def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1

    # 자식 노드들을 검사하면서
    for child in edges[node]:
        if not visited[child]:
            dfs(child)

            # 자식 노드의 얼리어답터의 개수를 더함
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
```