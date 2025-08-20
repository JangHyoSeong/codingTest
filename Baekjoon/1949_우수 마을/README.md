# [1949] 우수 마을

### **난이도**
골드 2
## **📝문제**
N개의 마을로 이루어진 나라가 있다. 편의상 마을에는 1부터 N까지 번호가 붙어 있다고 하자. 이 나라는 트리(Tree) 구조로 이루어져 있다. 즉 마을과 마을 사이를 직접 잇는 N-1개의 길이 있으며, 각 길은 방향성이 없어서 A번 마을에서 B번 마을로 갈 수 있다면 B번 마을에서 A번 마을로 갈 수 있다. 또, 모든 마을은 연결되어 있다. 두 마을 사이에 직접 잇는 길이 있을 때, 두 마을이 인접해 있다고 한다.

이 나라의 주민들에게 성취감을 높여 주기 위해, 다음 세 가지 조건을 만족하면서 N개의 마을 중 몇 개의 마을을 '우수 마을'로 선정하려고 한다.

1. '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
2. 마을 사이의 충돌을 방지하기 위해서, 만일 두 마을이 인접해 있으면 두 마을을 모두 '우수 마을'로 선정할 수는 없다. 즉 '우수 마을'끼리는 서로 인접해 있을 수 없다.
3. 선정되지 못한 마을에 경각심을 불러일으키기 위해서, '우수 마을'로 선정되지 못한 마을은 적어도 하나의 '우수 마을'과는 인접해 있어야 한다.

각 마을 주민 수와 마을 사이의 길에 대한 정보가 주어졌을 때, 주어진 조건을 만족하도록 '우수 마을'을 선정하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 10,000) 둘째 줄에는 마을 주민 수를 나타내는 N개의 자연수가 빈칸을 사이에 두고 주어진다. 1번 마을부터 N번 마을까지 순서대로 주어지며, 주민 수는 10,000 이하이다. 셋째 줄부터 N-1개 줄에 걸쳐서 인접한 두 마을의 번호가 빈칸을 사이에 두고 주어진다.
### **출력**
첫째 줄에 '우수 마을'의 주민 수의 총 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1000 3000 4000 1000 2000 2000 7000
1 2
2 3
4 3
4 5
6 2
6 7
```

**예제 출력1**

```
14000
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(int(1e9))

N = int(sys.stdin.readline().rstrip())
towns = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = towns[u]

    for v in edges[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|37048|64|Python3|637
#### **📝해설**

**알고리즘**
```
1. 트리
2. DP
```

### **다른 풀이**

```python
import sys



sys.setrecursionlimit(10**5)


def sol(weights, edges):
    def dfs(parent, cur):
        c1, c2 = 0, weights[cur]

        for chi in edges[cur]:
            if chi == parent: continue

            c3, c4 = dfs(cur, chi)

            c1 += c3 if c3 > c4 else c4
            c2 += c3 
        
        return c1, c2

    return max(dfs(0, 1))


readline = sys.stdin.readline
N = int(readline())

weights = (0,) + tuple(map(int, readline().split()))

edges = [[] for _ in range(N+1)]
for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

print(sol(weights, edges))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
power16one5|35036|48|Python3|635
#### **📝해설**

```python
import sys
sys.setrecursionlimit(int(1e9))

# 입력받기
N = int(sys.stdin.readline().rstrip())
towns = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

# dp배열 선언. dp[i][j] : i번째 마을까지 확인했을 때 최대값(j: 우수마을 선정 여부(1이면 선정))
dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

# DFS 재귀함수
def dfs(u):

    # 현재 마을 방문처리
    visited[u] = True

    # 우수마을로 선택하지 않은 경우
    dp[u][0] = 0

    # 우수 마을로 선택한 경우
    dp[u][1] = towns[u]

    # 방문 가능한 노드들을 확인하면서
    for v in edges[u]:

        # 방문하지 않았을 때
        if not visited[v]:

            # 다음 노드 방문(서브트리)
            dfs(v)

            # 현재 노드를 우수마을로 선정하지 않았으니, 다음 노드중 큰 값을 고름(우수마을이거나 아닌 경우)
            dp[u][0] += max(dp[v][0], dp[v][1])

            # 현재 노드를 우수마을로 정했으니, 다음 노드는 무조건 우수마을이 아니어야함
            dp[u][1] += dp[v][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))
```