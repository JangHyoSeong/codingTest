# [17070] 파이프 옮기기 1

### **난이도**
골드 5
## **📝문제**
유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.

![이미지](https://upload.acmicpc.net/3ceac594-87df-487d-9152-c532f7136e1e/-/preview/)

파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.

![이미지](https://upload.acmicpc.net/b29efafa-dbae-4522-809c-76d5c184a231/-/preview/)

파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.

![이미지](https://upload.acmicpc.net/0f445b26-4e5b-4169-8a1a-89c9e115907e/-/preview/)

가로

![이미지](https://upload.acmicpc.net/045d071f-0ea2-4ab5-a8db-61c215e7e7b7/-/preview/)

세로

![이미지](https://upload.acmicpc.net/ace5e982-6a52-4982-b51d-6c33c6b742bf/-/preview/)

대각선

가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.
### **입력**
첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.
### **출력**
첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.
### **예제입출력**

**예제 입력1**

```
3
0 0 0
0 0 0
0 0 0
```

**예제 출력1**

```
1
```

**예제 입력2**

```
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

**예제 출력2**

```
3
```

**예제 입력3**

```
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for y in range(N):
    for x in range(2, N):
        if table[y][x] == 1:
            continue

        if table[y][x-1] == 0:
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]

        if y-1 >= 0 and table[y-1][x] == 0:
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
        
        if y-1 >= 0 and x-1 >= 0:
            if table[y-1][x] == 0 and table[y][x-1] == 0 and table[y-1][x-1] == 0:
                dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[N-1][N-1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|665
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
N = int(input())
new_house = tuple(tuple(map(int, input().split())) for _ in range(N))
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if new_house[r][c]:
            continue
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
        dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
        if not new_house[r - 1][c] and not new_house[r][c - 1]:
            dp[r][c][2] = sum(dp[r - 1][c - 1])
print(sum(dp[N - 1][N - 1]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kanadachocolate|31120|32|Python3|544
#### **📝해설**

```python
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# dp테이블 정의. dp[y][x][dir]: 파이프의 끝이 (y, x)에 위치하며, dir방향의 경우의 수(0: 가로, 1: 세로, 2: 대각선)
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 초기상태
dp[0][1][0] = 1

# 모든 지점을 확인
for y in range(N):

    # 가로상태로 시작하고, (0,2)부터 시작
    for x in range(2, N):

        # 벽인 경우 넘어감
        if table[y][x] == 1:
            continue
        
        # 가로일 때
        if table[y][x-1] == 0:

            # 이전칸이 가로인 경우와 대각선인 경우를 더함
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]

        # 세로일 때
        if y-1 >= 0 and table[y-1][x] == 0:

            # 이전칸이 세로거나 대각선인 경우 더함
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
        
        # 대각선일 때
        if y-1 >= 0 and x-1 >= 0:

            # 이전칸이 가로, 대각선, 세로의 경우의 수를 더함
            if table[y-1][x] == 0 and table[y][x-1] == 0 and table[y-1][x-1] == 0:
                dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[N-1][N-1]))
```