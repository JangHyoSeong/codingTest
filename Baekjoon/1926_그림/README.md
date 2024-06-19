# [1926] 그림

### **난이도**
실버 1
## **📝문제**
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
### **입력**
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
### **출력**
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
### **예제입출력**

**예제 입력1**

```
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
```

**예제 출력1**

```
4
9
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
H, W = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(H)]

count = 0
max_large = 0

visited = [[False] * W for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        
        if canvas[i][j] == 1:
            visited[i][j] = True
            temp_large = 1
            count += 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and canvas[nx][ny] == 1:
                        visited[nx][ny] = True
                        temp_large += 1
                        stack.append((nx, ny))
            
            max_large = max(max_large, temp_large)

print(count)
print(max_large)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|46784|544|Python3|939
#### **📝해설**

**알고리즘**
```
1. DFS
```

#### **📝해설**

```python
# 입력받음
H, W = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(H)]

# 결과값으로 사용할 변수
count = 0
max_large = 0

# 방문 여부를 처리할 리스트
visited = [[False] * W for _ in range(H)]

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 리스트를 전부 탐색하면서
for i in range(H):
    for j in range(W):

        # 이미 방문한 위치라면 건너뜀
        if visited[i][j]:
            continue
        
        # 방문하지 않고, 그림이 그려져 있다면
        if canvas[i][j] == 1:
            # 방문처리를 함
            visited[i][j] = True

            # 이번 그림의 크기를 구할 변수
            temp_large = 1

            # 그림이 있으니 ++
            count += 1
            
            # DFS를 위한 스택. BFS로 해도 상관없음
            stack = [(i, j)]

            # DFS 시작
            while stack:

                # 현재 위치를 스택에서 pop
                x, y = stack.pop()

                # 상하좌우 탐색
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    # 인덱스를 벗어나지 않고, 방문하지 않았으며, 그림이 그려져있다면
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and canvas[nx][ny] == 1:

                        # 방문처리를 하고, 그림의 크기를 + 1
                        visited[nx][ny] = True
                        temp_large += 1
                        stack.append((nx, ny))
            
            # 이번 그림의 크기가 최대값이라면 갱신
            max_large = max(max_large, temp_large)

print(count)
print(max_large)
```