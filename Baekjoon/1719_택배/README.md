# [1719] 택배

### **난이도**
골드 3
## **📝문제**
명우기업은 2008년부터 택배 사업을 새로이 시작하기로 하였다. 우선 택배 화물을 모아서 처리하는 집하장을 몇 개 마련했지만, 택배 화물이 각 집하장들 사이를 오갈 때 어떤 경로를 거쳐야 하는지 결정하지 못했다. 어떤 경로를 거칠지 정해서, 이를 경로표로 정리하는 것이 여러분이 할 일이다.

예시된 그래프에서 굵게 표시된 1, 2, 3, 4, 5, 6은 집하장을 나타낸다. 정점간의 간선은 두 집하장간에 화물 이동이 가능함을 나타내며, 가중치는 이동에 걸리는 시간이다. 이로부터 얻어내야 하는 경로표는 다음과 같다.

경로표는 한 집하장에서 다른 집하장으로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것이다. 예를 들어 4행 5열의 6은 4번 집하장에서 5번 집하장으로 최단 경로를 통해 가기 위해서는 제일 먼저 6번 집하장으로 이동해야 한다는 의미이다.

이와 같은 경로표를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 두 수 n과 m이 빈 칸을 사이에 두고 순서대로 주어진다. n은 집하장의 개수로 200이하의 자연수, m은 집하장간 경로의 개수로 10000이하의 자연수이다. 이어서 한 줄에 하나씩 집하장간 경로가 주어지는데, 두 집하장의 번호와 그 사이를 오가는데 필요한 시간이 순서대로 주어진다. 집하장의 번호들과 경로의 소요시간은 모두 1000이하의 자연수이다.
### **출력**
예시된 것과 같은 형식의 경로표를 출력한다.
### **예제입출력**

**예제 입력1**

```
6 10
1 2 2
1 3 1
2 4 5
2 5 3
2 6 7
3 4 4
3 5 6
3 6 7
4 6 4
5 6 2
```

**예제 출력1**

```
- 2 3 3 2 2
1 - 1 4 5 5
1 1 - 4 5 6
3 2 3 - 6 6
2 2 3 6 - 6
5 5 3 4 5 -
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
INF = float('inf')

N, M = map(int, input().split())
dist = [[INF] * N for _ in range(N)]
path = [[0] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0
    path[i][i] = '-'

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
    path[a-1][b-1] = b
    path[b-1][a-1] = a

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]


for i in range(N):
    print(" ".join(map(str, path[i])))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112992|256|PyPy3|612
#### **📝해설**

**알고리즘**
```
1. 플로이드 워셜
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = [[200001] * n for _ in range(n)]
    ans = [['-'] * n for _ in range(n)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        arr[x - 1][y - 1] = arr[y - 1][x - 1] = c
        ans[x - 1][y - 1] = str(y)
        ans[y - 1][x - 1] = str(x)

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(i + 1, n):
                t = arr[i][k] + arr[k][j]
                if arr[i][j] > t:
                    arr[i][j] = arr[j][i] = t
                    ans[i][j] = ans[i][k]
                    ans[j][i] = ans[j][k]

    print('\n'.join(map(' '.join, ans)))


if __name__ == '__main__':
    solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
newprog|116004|180|PyPy3|791
#### **📝해설**

```python
INF = float('inf')

# 입력
N, M = map(int, input().split())

# dist[a][b] -> a에서 b노드까지의 거리
dist = [[INF] * N for _ in range(N)]

# 해당 노드에 도달 할 때, 직전 노드
path = [[0] * N for _ in range(N)]

# 초기값 세팅
for i in range(N):
    dist[i][i] = 0
    path[i][i] = '-'

# 입력받기. 초기값 세팅
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
    path[a-1][b-1] = b
    path[b-1][a-1] = a

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]


for i in range(N):
    print(" ".join(map(str, path[i])))
```