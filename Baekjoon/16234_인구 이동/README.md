# [16234] 인구 이동

### **난이도**
골드 4
## **📝문제**
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

- 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
- 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
- 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
- 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
- 연합을 해체하고, 모든 국경선을 닫는다.  
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.
### **출력**
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
2 20 50
50 30
20 40
```

**예제 출력1**

```
1
```

**예제 입력2**

```
2 40 50
50 30
20 40
```

**예제 출력2**

```
0
```

**예제 입력3**

```
2 20 50
50 30
30 40
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
while True:
    opened = [[False] * N for _ in range(N)]
    open_flag = False

    for i in range(N):
        for j in range(N):
            if opened[i][j]:
                continue

            q = deque([(i, j)])
            union = [(i, j)]
            temp_sum = table[i][j]
            opened[i][j] = True

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not opened[nx][ny]:
                        if L <= abs(table[nx][ny] - table[x][y]) <= R:
                            q.append((nx, ny))
                            union.append((nx, ny))
                            temp_sum += table[nx][ny]
                            opened[nx][ny] = True
                            open_flag = True

            if len(union) > 1:
                new_population = temp_sum // len(union)
                for x, y in union:
                    table[x][y] = new_population

    if not open_flag:
        break

    count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124376|1056|PyPy3|1264
#### **📝해설**

**알고리즘**
```
1. 구현
```

#### **📝해설**

```python
from collections import deque

N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 검사를 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 몇 번 인구 이동이 일어났는지 검사할 변수
count = 0

# break하기 전까지 무한으로 반복
while True:

    # 국경선이 열렸는지 여부를 검사할 리스트
    opened = [[False] * N for _ in range(N)]

    # 국경선이 열린적이 있는지 검사할 리스트
    open_flag = False

    # 모든 나라를 순회하면서
    for i in range(N):
        for j in range(N):

            # 이미 국경선이 열린 지역이면 넘어감
            if opened[i][j]:
                continue
            
            # 이번 나라를 기준으로 BFS를 시작
            q = deque([(i, j)])

            # 연합 국가를 저장할 리스트
            union = [(i, j)]

            # 연합 국가의 시민 수를 전부 더할 변수
            temp_sum = table[i][j]

            # 이번 나라의 국경을 일단 열어둠
            opened[i][j] = True

            # BFS 시작
            while q:
                x, y = q.popleft()

                # 상하좌우 인접한 칸을 검사하면서
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    # 주어진 조건에 맞는다면
                    if 0 <= nx < N and 0 <= ny < N and not opened[nx][ny]:
                        if L <= abs(table[nx][ny] - table[x][y]) <= R:

                            # 연합 국가에 더함
                            q.append((nx, ny))
                            union.append((nx, ny))
                            temp_sum += table[nx][ny]
                            opened[nx][ny] = True
                            open_flag = True

            # 연합 국가가 2개 이상 존재한다면
            if len(union) > 1:

                # 인구수를 균등하게 나눔
                new_population = temp_sum // len(union)
                for x, y in union:
                    table[x][y] = new_population

    # 국경이 열린적이 없다면 루프 종료
    if not open_flag:
        break

    # 마지막으로 횟수를 더함
    count += 1

print(count)
```