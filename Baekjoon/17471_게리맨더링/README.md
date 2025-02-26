# [17471] 게리멘더링

### **난이도**
골드 3
## **📝문제**
백준시의 시장 최백준은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 최백준은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 백준시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.

백준시는 N개의 구역으로 나누어져 있고, 구역은 1번부터 N번까지 번호가 매겨져 있다. 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

아래 그림은 6개의 구역이 있는 것이고, 인접한 구역은 선으로 연결되어 있다.

[이미지](https://upload.acmicpc.net/08218f4c-2653-4861-a4c1-e7ce808f3a85/-/preview/)

공평하게 선거구를 나누기 위해 두 선거구에 포함된 인구의 차이를 최소로 하려고 한다. 백준시의 정보가 주어졌을 때, 인구 차이의 최솟값을 구해보자.
### **입력**
첫째 줄에 구역의 개수 N이 주어진다. 둘째 줄에 구역의 인구가 1번 구역부터 N번 구역까지 순서대로 주어진다. 인구는 공백으로 구분되어져 있다.

셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보가 주어진다. 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다. 모든 값은 정수로 구분되어져 있다.

구역 A가 구역 B와 인접하면 구역 B도 구역 A와 인접하다. 인접한 구역이 없을 수도 있다.
### **출력**
첫째 줄에 백준시를 두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값을 출력한다. 두 선거구로 나눌 수 없는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6
1 1 1 1 1 1
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
```

**예제 출력2**

```
0
```

**예제 입력3**

```
6
10 20 10 20 30 40
0
0
0
0
0
0
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations
from collections import deque

N = int(input())
populations = [0] + list(map(int, input().split()))

edges = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    edges[i] = data[1:]

min_population = int(21e8)

for i in range(1, N//2 + 1):
    for subset in combinations(range(1, N+1), i):
        area1 = set(subset)
        area2 = set(range(1, N+1)) - area1

        queue = deque([next(iter(area1))])
        visited = set(queue)

        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        if visited != area1:
            continue

        queue = deque([next(iter(area2))])
        visited = set(queue)
        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area2 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        if visited != area2:
            continue

        pop1 = sum(populations[i] for i in area1)
        pop2 = sum(populations[i] for i in area2)
        min_population = min(min_population, abs(pop1 - pop2))

print(min_population if min_population != int(21e8) else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36040|64|Python3|1417
#### **📝해설**

**알고리즘**
```
1. 브루탈포스
2. 조합
```

### **다른 풀이**

```python
from itertools import combinations

def bfs(comb):
    Q = [comb[0]]
    visited = [0] * (N+1)
    visited[comb[0]] = 1
    cnt = 1
    people = population[comb[0]]

    while Q:
        temp = Q.pop(0)
        for w in adj_lst[temp]:
            if visited[w] == 0 and w in comb:
                Q.append(w)
                visited[w] = 1
                cnt += 1
                people += population[w]

    return people, cnt


N = int(input())
population = [0] + list(map(int,input().split()))
adj_lst = [[] for _ in range(N+1)]
result = 1001
for i in range(1,N+1):
    temp = list(map(int,input().split()))
    adj_lst[i] = temp[1:]

for i in range(1,N//2+1):
    comb_lst = list(combinations(range(1,N+1),i))
    for comb in comb_lst:
        people1, cnt1 = bfs(comb)

        comb_2 = []
        for x in range(1,N+1):
            if x not in comb:
                comb_2.append(x)
        people2, cnt2 = bfs(comb_2)

        if cnt1 + cnt2 == N:
            result = min(result, abs(people2 - people1))

if result != 1001:
    print(result)
else:
    print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
taktak33|31120|36|Python3|1070
#### **📝해설**

```python
from itertools import combinations
from collections import deque

# 입력받음
N = int(input())
populations = [0] + list(map(int, input().split()))

# 간선 정보 저장
edges = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    edges[i] = data[1:]

# 최소 인구차이를 저장할 변수
min_population = int(21e8)

# 모든 지역구를 두 집합으로 나누기 위한 반복
for i in range(1, N//2 + 1):
    # 원소가 i개인 조합을 생성
    for subset in combinations(range(1, N+1), i):
        # 구역 1
        area1 = set(subset)
        # 구역 2
        area2 = set(range(1, N+1)) - area1

        # 구역 1에서 임의의 한 지역을 선택
        queue = deque([next(iter(area1))])

        # BFS
        visited = set(queue)

        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # 구역을 모두 방문할 수 없는 경우 고려하지 않음
        if visited != area1:
            continue

        # 구역 2도 똑같이 BFS
        queue = deque([next(iter(area2))])
        visited = set(queue)
        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if neighbor in area2 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        if visited != area2:
            continue
        
        # 두 구역의 인구차를 구한 뒤 갱신
        pop1 = sum(populations[i] for i in area1)
        pop2 = sum(populations[i] for i in area2)
        min_population = min(min_population, abs(pop1 - pop2))

# 출력
print(min_population if min_population != int(21e8) else -1)
```