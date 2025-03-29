# [1956] 운동

### **난이도**
골드 4
## **📝문제**
V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.
### **입력**
첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a → b임에 주의) 거리는 10,000 이하의 자연수이다. (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.
### **출력**
첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
1 2 1
3 2 1
1 3 5
2 3 2
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
INF = int(21e8)

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(E)]

dist = [[INF] * (V+1) for _ in range(V+1)]
for a, b, c in edges:
    dist[a][b] = c

for i in range(1, V+1):
    dist[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_cycle = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            min_cycle = min(min_cycle, dist[i][j] + dist[j][i])

print(min_cycle if min_cycle != INF else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|128900|780|PyPy3|683
#### **📝해설**

**알고리즘**
```
1. 플로이드 워셜
```

#### **📝해설**

```python
import sys
INF = int(21e8)

# 간선 정보 입력
V, E = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(E)]

# 각 노드까지의 거리를 2차원 리스트로 표현
dist = [[INF] * (V+1) for _ in range(V+1)]

# 거리 정보를 입력
for a, b, c in edges:
    dist[a][b] = c

# 본인 노드까지의 거리는 0
for i in range(1, V+1):
    dist[i][i] = 0

# 플로이드 워셜 알고리즘
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 최소 사이클 길이
min_cycle = INF

# 모든 노드를 검사하면서
for i in range(1, V+1):
    for j in range(1, V+1):

        # 최소 사이클의 길이를 찾음
        if i != j:
            min_cycle = min(min_cycle, dist[i][j] + dist[j][i])

# 출력
print(min_cycle if min_cycle != INF else -1)
```