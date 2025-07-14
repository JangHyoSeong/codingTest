# [1743] 음식물 피하기

### **난이도**
실버 1
## **📝문제**
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 

이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 

통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.
### **입력**
첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.
### **출력**
첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.
### **예제입출력**

**예제 입력1**

```
3 4 5
3 2
2 2
3 1
2 3
1 1
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, K = map(int, input().split())

table = [[False] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    table[r-1][c-1] = True

visited = [[False] * M for _ in range(N)]
max_count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if visited[i][j] or not table[i][j]:
            continue

        count = 1
        stack = [(i, j)]
        visited[i][j] = True

        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
        
        max_count = max(max_count, count)

print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|168|Python3|844
#### **📝해설**

**알고리즘**
```
1. 그래프
```

#### **📝해설**

```python
N, M, K = map(int, input().split())

# 음식물의 위치를 저장할 이차원 리스트
table = [[False] * M for _ in range(N)]

# 위치 저장
for _ in range(K):
    r, c = map(int, input().split())
    table[r-1][c-1] = True

# 방문 여부를 저장할 리스트
visited = [[False] * M for _ in range(N)]

# 가장 큰 음식물의 크기
max_count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 모든 좌표를 검사하면서
for i in range(N):
    for j in range(M):

        # 방문했던 곳이거나 음식물이 없다면 건너뜀
        if visited[i][j] or not table[i][j]:
            continue
        
        # 현재위치부터 DFS 시작
        count = 1
        stack = [(i, j)]
        visited[i][j] = True

        while stack:
            x, y = stack.pop()

            # 상하좌우를 검사하면서 이동
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
        
        # DFS가 끝났다면 최대 크기 갱신
        max_count = max(max_count, count)

print(max_count)
```