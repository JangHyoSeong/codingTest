# [11724] 연결 요소의 개수

### **난이도**
실버2
## **📝문제**
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
### **출력**
첫째 줄에 연결 요소의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
6 5
1 2
2 5
5 1
3 4
4 6
```

**예제 출력1**

```
2
```

**예제 입력2**

```
6 5
1 2
2 5
5 1
3 4
4 6
```

**예제 출력2**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        visited[i] = True

        stack = [i]
        while stack:
            now = stack.pop()

            for next in edges[now]:
                if not visited[next]:
                    stack.append(next)
                    visited[next] = True

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|173416|396|PyPy3|539
#### **📝해설**

**알고리즘**
```
1.DFS
```
#### **📝해설**

```python

# 입력받기
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# 방문 여부 저장 리스트
visited = [False] * (N+1)

# 연결 요소의 개수
count = 0

# 노드를 검사하면서
for i in range(1, N+1):

    # 이전에 방문하지 않았던 노드라면
    if not visited[i]:
        # 새로운 연결 요소
        count += 1
        visited[i] = True

        # 현재 위치를 기준으로 DFS
        stack = [i]
        while stack:
            now = stack.pop()

            for next in edges[now]:
                if not visited[next]:
                    stack.append(next)
                    visited[next] = True

print(count)
```

### **🔖정리**

1. 배운점