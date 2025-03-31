# [2667] 단지번호붙이기

### **난이도**
실버 1
## **📝문제**
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

[이미지](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)
### **입력**
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
### **출력**
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
### **예제입출력**

**예제 입력1**

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

**예제 출력1**

```
3
7
8
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
table = [list(map(int, input())) for _ in range(N)]

count = 0
result = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if table[i][j] == 0:
            continue
        
        count += 1
        stack = [(i, j)]
        table[i][j] = 0

        area_count = 1
        while stack:
            x, y = stack.pop()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if 0 <= nx < N and 0 <= ny < N and table[nx][ny]:
                    stack.append((nx, ny))
                    table[nx][ny] = 0
                    area_count += 1
        
        result.append(area_count)

print(count)
print("\n".join(map(str, sorted(result))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|738
#### **📝해설**

**알고리즘**
```
1. DFS
```

#### **📝해설**

```python
N = int(input())
table = [list(map(int, input())) for _ in range(N)]

# 영역의 총 개수
count = 0

# 영역의 넓이를 저장할 리스트
result = []

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 주어진 범위의 모든 장소를 검사
for i in range(N):
    for j in range(N):
        # 0이라면 건너뜀 (단지가 없거나, 이미 방문한 곳이라면)
        if table[i][j] == 0:
            continue
        
        # 1이라면 그 곳에서부터 DFS로 탐색을 시작
        # 영역의 개수를 더함
        count += 1

        # DFS를 위한 스택
        stack = [(i, j)]

        # 방문 처리
        table[i][j] = 0

        # 이번 단지의 넓이를 셀 변수
        area_count = 1
        while stack:
            x, y = stack.pop()

            # 상하좌우를 탐색
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                # 인덱스를 벗어나지 않고 단지가 있다면
                if 0 <= nx < N and 0 <= ny < N and table[nx][ny]:

                    # 스택에 추가 후 방문처리
                    stack.append((nx, ny))
                    table[nx][ny] = 0
                    area_count += 1
        
        # DFS가 끝난 후 단지의 범위를 저장
        result.append(area_count)

# 출력
print(count)
print("\n".join(map(str, sorted(result))))
```