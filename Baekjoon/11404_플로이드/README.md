# [11404] 플로이드

### **난이도**
골드 4
## **📝문제**
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
### **출력**
n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
```

**예제 출력1**

```
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    dist[i][i] = 0

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    dist[a][b] = min(dist[a][b], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

for i in range(1, N+1):
    print(" ".join(map(str, dist[i][1:])))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111432|164|PyPy3|652
#### **📝해설**

**알고리즘**
```
1. 플로이드 워셜
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# MAXC = 100000000

n = int(input())
d = [[100000000]*(n+1) for _ in range(n+1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if c < d[a][b]: d[a][b] = c

for i in range(1, n+1): d[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(d[i][j] if d[i][j] != 100000000 else 0, end=' ')
    print()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|112848|132|PyPy3|593
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

# 각 노드까지의 거리를 이차원 리스트로 저장
dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

# 자기 자신까지 거리는 0
for i in range(1, N+1):
    dist[i][i] = 0

# 간선 정보를 입력받음
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())

    # 최소값이 되는 간선만 저장
    dist[a][b] = min(dist[a][b], cost)

# 플로이드 워셜 알고리즘으로 각 노드간의 거리 최소값을 모두 구함
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 도달하지 못하는 경우 0으로 바꿈
for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

# 출력
for i in range(1, N+1):
    print(" ".join(map(str, dist[i][1:])))
```