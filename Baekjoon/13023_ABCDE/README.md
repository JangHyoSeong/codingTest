# [13023] ABCDE

### **난이도**
골드 5
## **📝문제**
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

- A는 B와 친구다.
- B는 C와 친구다.
- C는 D와 친구다.
- D는 E와 친구다.  
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.
### **출력**
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 4
0 1
1 2
2 3
3 4
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6 5
0 1
0 2
0 3
0 4
0 5
```

**예제 출력2**

```
0
```

**예제 입력3**

```
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def dfs(node, depth):
    if depth == 4:
        print(1)
        exit()

    visited[node] = True
    for next_node in edges[node]:
        if not visited[next_node]:
            dfs(next_node, depth+1)
    
    visited[node] = False

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * N

for i in range(N):
    dfs(i, 0)    

print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|640|Python3|473
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

#### **📝해설**

```python
def dfs(node, depth):
    # 재귀함수를 통한 DFS

    # 친구의 깊이가 4가 된다면 1을 출력하고 종료
    if depth == 4:
        print(1)
        exit()

    # 현재 노드 방문처리
    visited[node] = True

    # 다음 노드를 탐색
    for next_node in edges[node]:
        # 방문하지 않았다면 방문
        if not visited[next_node]:
            dfs(next_node, depth+1)

    # 이번 케이스가 깊이가 4가 아니라면 백트래킹
    visited[node] = False

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * N

for i in range(N):
    dfs(i, 0)    

print(0)
```

### **🔖정리**

1. 배운점