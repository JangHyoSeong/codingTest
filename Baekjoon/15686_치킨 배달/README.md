# [15686] 치킨 배달

### **난이도**
골드 5
## **📝문제**
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.
```
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2
```
0은 빈 칸, 1은 집, 2는 치킨집이다.

(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
### **출력**
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
```

**예제 출력1**

```
5
```

**예제 입력2**

```
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
```

**예제 출력2**

```
10
```

**예제 입력3**

```
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
```

**예제 출력3**

```
11
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, M))

min_chicken_range = 21e8

for case in comb_chicken:
    temp_chicken_range = 0

    for one_house in house:
        h_x, h_y = one_house
        
        one_range = 100
        for one_chicken in case:
            c_x, c_y = one_chicken
            one_range = min(one_range, abs((h_x-c_x)) + abs((h_y - c_y)))
        
        temp_chicken_range += one_range
        if temp_chicken_range > min_chicken_range:
            break
    
    min_chicken_range = min(min_chicken_range, temp_chicken_range)

print(min_chicken_range)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111332|160|PyPy3|898
#### **📝해설**

**알고리즘**
```
1. 완전 탐색
2. 백트래킹
```

#### **😅개선점**

1. BFS를 사용해서도 풀어보자

### **다른 풀이**

```python
ans = 1e9
def solve():
    global ans
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    chickens = []
    chicken_dists = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                houses.append((i, j))
            elif board[i][j] == 2:
                chickens.append((i, j))


    for r1, c1 in houses:
        chicken_dists.append([])
        for idx, (r2, c2) in enumerate(chickens):
            chicken_dists[-1].append((abs(r1 - r2) + abs(c1 - c2), idx))
        chicken_dists[-1].sort(key=lambda x:x[0])

    ans = 1e9
    visited = [False for _ in range(len(chickens))]
    def dfs(depth, start):
        global ans
        if depth == M:
            tmp = 0
            for D in chicken_dists:
                for distance, idx in D:
                    if visited[idx]:
                        tmp += distance
                        break
            ans = min(ans, tmp)
            return

        for i in range(start, len(chickens)):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False

    dfs(0, 0)
    print(ans)

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
greg1028|31120|72|Python3|1240
#### **📝해설**

```python
from itertools import combinations

# 입력 받음
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 좌표를 튜플의 형태로 리스트에 저장해둠
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 모든 치킨집 중 M개로 치킨집을 구성하는 조합을 생성
comb_chicken = list(combinations(chicken, M))

# 치킨거리의 최소값이 될 변수
min_chicken_range = 21e8

# M개의 치킨집을 고른 조합을 case로 두고 순회
for case in comb_chicken:
    # 이 경우에서의 치킨 거리
    temp_chicken_range = 0

    # 모든 집마다 가장 가까운 치킨거리를 구할 것
    for one_house in house:
        # 현재 집의 좌표
        h_x, h_y = one_house
        
        # 현재 집의 최소 치킨거리를 저장할 변수
        one_range = 100

        # M개 고른 치킨집 중 모든 치킨집을 순회하며 최소값을 찾음
        for one_chicken in case:

            # 치킨집의 좌표
            c_x, c_y = one_chicken

            # 모든 치킨집의 거리를 구하고, 최소값과 비교하여 최소값을 찾음
            one_range = min(one_range, abs((h_x-c_x)) + abs((h_y - c_y)))
        
        # 한 집에서 최소 치킨거리를 총 마을의 최소치킨거리에 더해줌
        temp_chicken_range += one_range
        
        # 이미 최소값을 넘었다면 이 케이스는 더이상 수행하지 않고 넘어감
        if temp_chicken_range > min_chicken_range:
            break
    
    # 최소 치킨거리를 갱신시켜줌
    min_chicken_range = min(min_chicken_range, temp_chicken_range)

print(min_chicken_range)
```