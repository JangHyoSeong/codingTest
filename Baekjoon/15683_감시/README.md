# [15683] 감시

### **난이도**
골드 4
## **📝문제**

### **입력**
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.
### **출력**
첫째 줄에 사각 지대의 최소 크기를 출력한다.
### **예제입출력**

**예제 입력1**

```
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
```

**예제 출력1**

```
20
```

**예제 입력2**

```
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
```

**예제 출력2**

```
15
```

**예제 입력3**

```
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
```

**예제 출력3**

```
6
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from copy import deepcopy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctvs = []

for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append([i, j, office[i][j]])

cctv_count = len(cctvs)
min_count = N * M

def check_down(x, y, office):
    while x < N:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x += 1
    
    return office

def check_up(x, y, office):
    while x >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x -= 1
    
    return office

def check_left(x, y, office):
    while y >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y -= 1

    return office

def check_right(x, y, office):
    while y < M:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y += 1

    return office

def check_blind(idx, office):
    global min_count

    if idx == cctv_count:
        count = 0

        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    count += 1

        if min_count > count:
            min_count = count
        
        return

    x, y, cctv = cctvs[idx]
    
    if cctv == 1:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        nx = x
        temp_office = deepcopy(office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)
        
    if cctv == 2:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 3:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 4:
        nx, ny = x, y

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 5:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

check_blind(0, office)
print(min_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124828|1048|PyPy3|4606
#### **📝해설**

**알고리즘**
```
1. 완전탐색
```

#### **😅개선점**

1. 조금만 실행시간을 줄여보자

### **다른 풀이**

```python
# 벽은 감시할 수 없고, 통과도 못 한다. CCTV는 회전시킬 수 있다. 5가지 타입의 CCTV가 있다. CCTV가 못 비추는 사각지대가 최소가 되게 하는 사각지대갯수를 구해라.

blind = 0
cctv = []
dx = [0,0,-1,1] # 오,왼,위,아래
dy = [1,-1,0,0] 
# cctv로 비출 수 있는 구역들 다 비추기 
def watch(x,y,check_list):
    s=set() # visited 대신 set 사용. 갔던 데 또 가도 되는 대신 합쳐지기때문
    for d in check_list: # d=0 check_list = [0,1]
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d] # visited 했어도 또 비춰도 되므로 set 사용. 중복
            if nx<0 or ny<0 or nx>=N or ny>=M or graph[nx][ny]==6:
                break
            elif graph[nx][ny]==0:
                s.add((nx,ny))
    return s
type = {
    1:[[0],[1],[2],[3]],
    2:[[0,1],[2,3]],
    3:[[0,2],[0,3],[1,2],[1,3]],
    4:[[0,1,2],[0,1,3],[2,3,0],[2,3,1]],
    5:[[0,1,2,3]]
}
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
# cctv별로 비출 수 있는 경우의 수 set조합들 만들어 cctv에 저장.
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            blind+=1 # 안보이는 지역 수
        elif graph[i][j]!=0 and graph[i][j]!=6:
            cctv.append([watch(i,j,check_list) for check_list in type[graph[i][j]]]) # check_list = [0,1] 한 경우마다 비춰지는 좌표들 set


# 가장 넓은 범위로 비추는 watched_set 만들기
watched_set = [set()]
def dfs(depth,prev_set):
    if depth==len(cctv):
        if len(prev_set)>len(watched_set[0]): # 더 많이 비추면 갱신
            watched_set[0] = prev_set
        return
    for cur_set in cctv[depth]: # 조합1, 조합2..
        dfs(depth+1,prev_set|cur_set) # prev_set | 조합1

dfs(0,set())
print(blind - len(watched_set[0]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
aassdd38|31256|100|Python3|1903
#### **📝해설**

```python
from copy import deepcopy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# 현재 cctv의 위치, 종류를 담을 리스트
cctvs = []

# cctv의 정보를 리스트에 담아줌
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append([i, j, office[i][j]])

# cctv의 총 개수
cctv_count = len(cctvs)

# 사각지대의 최소값을 선언
min_count = N * M

# 각각 현재 cctv기준 아래, 위, 왼쪽, 오른쪽의 사각지대를 없애는 함수들
def check_down(x, y, office):
    while x < N:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x += 1
    
    return office

def check_up(x, y, office):
    while x >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x -= 1
    
    return office

def check_left(x, y, office):
    while y >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y -= 1

    return office

def check_right(x, y, office):
    while y < M:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y += 1

    return office

# 재귀적으로 호출되며 완전탐색을 실행할 함수
# 인덱스를 늘려가며, 모든 경우의수를 탐색함
def check_blind(idx, office):
    global min_count

    # 모든 cctv의 방향을 정했다면
    if idx == cctv_count:
        count = 0

        # 사각지대의 개수를 셈
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    count += 1

        # 최소값 갱신이 가능하다면 갱신
        if min_count > count:
            min_count = count
        
        return

    # 현재 인덱스의 cctv 정보
    x, y, cctv = cctvs[idx]
    
    # 모든 방향을 고려하여 완전탐색
    if cctv == 1:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        nx = x
        temp_office = deepcopy(office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)
        
    if cctv == 2:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 3:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 4:
        nx, ny = x, y

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 5:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

check_blind(0, office)
print(min_count)
```