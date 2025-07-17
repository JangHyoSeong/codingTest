# [2157] 여행

### **난이도**
골드 4
## **📝문제**
N개의 도시가 동쪽에서 서쪽으로 순서대로 위치해 있다. 제일 동쪽에 있는 도시는 1번 도시이며, 제일 서쪽에 있는 도시는 N번 도시이다.

당신은 이와 같은 도시 중에서 M개 이하의 도시를 지나는 여행을 계획하려 한다. 여행 경로는 반드시 1번 도시에서 시작해서 N번 도시에서 끝나야 한다. 물론 이 두 도시도 M개의 도시에 포함된다. 당신은 시차에 매우 민감하기 때문에, 한 번 서쪽으로 이동했다가 다시 동쪽으로 이동하면 몸이 대단히 아프다. 그래서 당신은 계속 서쪽으로만, 즉 도시 번호가 증가하는 순서대로만 이동하기로 하였다.

한편, 모든 도시에서 다른 모든 도시로 이동할 수 있는 건 아니다. 각각의 도시에서 다른 도시로 이동할 때에는 비행기를 타고 이동해야 하는데, 때로는 비행 항로가 개설되지 않았을 수도 있다. 또한 당신은 비행기를 아무렇게나 타려는 것이 아니라, 최대한 맛있는 기내식만 먹으면서 이동하려 한다(사실 이게 여행의 목적이다).

항로 개설 여부와 해당 항로에서 제공되는 기내식의 점수가 주어졌을 때, 먹게 되는 기내식의 점수의 총 합이 최대가 되도록 하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 300), M(2 ≤ M ≤ N), K(1 ≤ K ≤ 100,000)가 주어진다. K는 개설된 항공로의 개수이다. 다음 K개의 줄에는 각 항공로에 대한 정보를 나타내는 세 정수 a, b, c(1 ≤ a, b ≤ N, 1 ≤ c ≤ 10,000)가 주어진다. 이는 a번 도시에서 b번 도시로 이동하는 항로가 있고, 서비스되는 기내식의 점수가 c점이라는 의미이다. 서쪽에서 동쪽으로 이동하는 항로가 입력될 수도 있고, 같은 도시 쌍 사이에 항로가 여러 개 있을 수도 있지만, 날아다니다 다시 원래 도시로 돌아오는 a=b 와 같은 입력은 없다.
### **출력**
첫째 줄에 기내식 점수의 총 합의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3 5
1 3 10
1 2 5
2 3 3
1 3 4
3 1 100
```

**예제 출력1**

```
10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a < b:
        edges[a].append((b, c))

dp = [[-1] * (M+1) for _ in range(N+1)]
dp[1][1] = 0

for cnt in range(1, M):
    for curr in range(1, N+1):
        if dp[curr][cnt] == -1:
            continue

        for next_city, score in edges[curr]:
            dp[next_city][cnt + 1] = max(dp[next_city][cnt + 1], dp[curr][cnt] + score)
    
print(max(dp[N]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113480|220|PyPy3|549
#### **📝해설**

**알고리즘**
``` 
1. DP
```

### **다른 풀이**

```python
import sys

N, M, K = map(int, sys.stdin.readline().split())

graph = [[0] * (N+1) for i in range(N+1)]
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a <= b:
        graph[a][b] = max(graph[a][b], c)

dp = graph[1][:]
lst = []
for i in range(N, 1, -1):
    if graph[1][i] > 0:
        lst.append(i)
turn = 1
while turn < M-1:
    temp = set([])
    for i in lst:
        for j in range(N, i, -1):
            if graph[i][j] > 0 and dp[i] + graph[i][j] > dp[j]:
                dp[j] = dp[i] + graph[i][j]
                temp.add(j)
    if not temp:
        break
    lst = sorted(list(temp), reverse=True)
    turn+=1
print(dp[N])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
shhwangofficial|111416|168|PyPy3|665
#### **📝해설**

```python
import sys

# 입력받기
N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # 노드가 증가하는 경우에만 간선으로 추가
    if a < b:
        edges[a].append((b, c))

# DP배열 dp[i][j] : i번째 노드에 j번 이동해서 도달할때 최대 점수
dp = [[-1] * (M+1) for _ in range(N+1)]

# 시작점 초기화
dp[1][1] = 0


# M번 이동하는 동안
for cnt in range(1, M):

    # 모든 노드를 방문해서
    for curr in range(1, N+1):

        # 방문할 수 없는 곳은 넘어감
        if dp[curr][cnt] == -1:
            continue
        
        # 이동할 수 있는 도시들을 확인하면서
        for next_city, score in edges[curr]:

            # 최대값을 갱신
            dp[next_city][cnt + 1] = max(dp[next_city][cnt + 1], dp[curr][cnt] + score)

# 출력
print(max(dp[N]))
```