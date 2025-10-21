# [24230] 트리 색칠하기

### **난이도**
골드 5
## **📝문제**
정점이 
$N$개인 트리가 있다. 정점에는 1부터 
$N$까지 번호가 붙어있다. 트리의 루트는 항상 1번 정점이며 맨 처음에는 모든 정점이 하얀색으로 칠해져 있는 상태이다.

하나의 정점에 색칠하면 해당 정점 아래 있는 모든 정점이 같은 색으로 칠해진다. 색은 섞이지 않고 색칠할 때마다 그 색으로 덮어진다. 단, 하얀색으로 색칠할 수는 없다.

아래 그림처럼 정점 10개로 구성된 트리가 있다고 가정을 해보자.

![이미지](https://upload.acmicpc.net/d60753e6-25d7-4baa-94c3-e99d84ed3d42/-/preview/)

[그림 1] 하얀색으로 칠해져 있는 트리

3번 정점을 노란색으로 칠하면 그 아래 있는 정점 5, 6, 8, 9, 10 모두 노란색으로 칠해진다.

![이미지](https://upload.acmicpc.net/6345e2aa-2c8a-4f59-a274-e9073c61e520/-/preview/)

[그림 2] 정점 3에 노란색을 칠한 후 트리의 상태

그리고 정점 5에 파란색을 칠한다면 그 아래 있는 정점 8, 9, 10 모두 파란색으로 칠해진다.

![이미지](https://upload.acmicpc.net/25b335ab-1493-4ca6-a4a0-87486da7e39d/-/preview/)

[그림 3] 정점 5에 파란색을 칠한 후 트리의 상태

입력으로 트리의 정보와 정점의 색 정보가 주어진다. 색 정보는 음이 아닌 정수로 주어지며 값이 0인 경우는 항상 하얀색을 의미한다.

하얀색을 제외한 색만 사용해서 모든 정점을 주어진 색으로 칠하고 싶을 때 최소 몇 번 색을 칠해야 모든 정점을 원하는 색으로 칠할 수 있는지 구해보자.

### **입력**
첫째 줄에 트리를 구성하는 정점의 개수 
$N(1 ≤ N ≤ 200,000)$이 주어진다.

둘째 줄에 1번 정점부터 
$N$번 정점까지 각 색 정보 
$C_i (0 ≤ C_i ≤ N)$가 공백으로 구분되어 주어진다.

셋째 줄부터 
$N - 1$개의 줄에 걸쳐 연결된 두 정점 
$a, b(1 ≤ a, b ≤ N$, 
$a ≠ b)$가 공백으로 구분되어 주어진다.  

모든 정점을 칠할 수 있는 입력만 주어진다.
### **출력**
하얀색을 제외한 색만 사용해서 모든 정점을 원하는 색으로 칠하기 위해 최소 몇 번 칠하면 되는지 출력한다.
### **예제입출력**

**예제 입력1**

```
7
0 0 2 0 1 2 2
1 2
1 3
1 4
2 5
3 6
3 7
```

**예제 출력1**

```
2
```

**예제 입력2**

```
10
0 0 1 0 2 1 0 2 2 2
3 1
1 4
9 5
10 5
1 2
3 6
3 5
5 8
4 7
```

**예제 출력2**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
colors = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)
visited[1] = True

count = 0

if colors[1] != 0:
    count += 1
stack = [1]

while stack:
    now_node = stack.pop()

    for next_node in edges[now_node]:
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
            if colors[next_node] != colors[now_node]:
                count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|154372|388|PyPy3|666
#### **📝해설**

**알고리즘**
```
1. 트리
```

### **다른 풀이**

```python
# 문제 URL : https://www.acmicpc.net/problem/24230
import sys
input = sys.stdin.readline

N = int(input())
C = [0] + list(map(int, input().split()))
ans = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    if C[a] != C[b]:
        ans += 1

if C[1] != 0:
    ans += 1

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pcy4196|146804|192|PyPy3|295
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
colors = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

# 각 노드의 자식노드 정보
edges = [[] for _ in range(N+1)]

# 간선 연결
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

# 방문 여부 저장
visited = [False] * (N+1)

# 루트 노드 방문
visited[1] = True

count = 0

# 루트 노드부터 색이 있다면 count ++
if colors[1] != 0:
    count += 1
stack = [1]

# DFS
while stack:
    now_node = stack.pop()

    # 자식 노드를 확인하면서
    for next_node in edges[now_node]:

        # 방문한 적 없다면 방문
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)

            # 자식노드와 색이 다르다면 무조건 칠해야함
            if colors[next_node] != colors[now_node]:
                count += 1

print(count)
```