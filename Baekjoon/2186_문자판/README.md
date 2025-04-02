# [2186] 문자판

### **난이도**
골드 3
## **📝문제**
알파벳 대문자가 한 칸에 한 개씩 적혀있는 N×M 크기의 문자판이 있다. 편의상 모든 문자는 대문자라 생각하자. 예를 들어 아래와 같은 문자판을 보자.

```
K	A	K	T
X	E	A	S
Y	R	W	U
Z	B	Q	P
```

이 문자판의 한 칸(아무 칸이나 상관없음)에서 시작하여 움직이면서, 그 칸에 적혀 있는 문자들을 차례대로 모으면 하나의 단어를 만들 수 있다. 움직일 때는 상하좌우로 K개의 칸까지만 이동할 수 있다. 예를 들어 K=2일 때 아래의 그림의 가운데에서는 'X' 표시된 곳으로 이동할 수 있다.

```
 	 	X	 	 
 	 	X	 	 
X	X	 	X	X
 	 	X	 	 
 	 	X	 	 
```

반드시 한 칸 이상 이동을 해야 하고, 같은 자리에 머물러 있을 수 없다. 또, 같은 칸을 여러 번 방문할 수 있다.

이와 같은 문자판과 K, 그리고 하나의 영단어가 주어졌을 때, 이와 같은 영단어를 만들 수 있는 경로가 총 몇 개 존재하는지 알아내는 프로그램을 작성하시오.

위의 예에서 영단어가 BREAK인 경우에는 다음과 같이 3개의 경로가 존재한다. 앞의 수는 행 번호, 뒤의 수는 열 번호를 나타낸다.

- (4, 2) (3, 2) (2, 2) (1, 2) (1, 1)
- (4, 2) (3, 2) (2, 2) (1, 2) (1, 3)
- (4, 2) (3, 2) (2, 2) (2, 3) (1, 3)
### **입력**
첫째 줄에 N(1 ≤ N ≤ 100), M(1 ≤ M ≤ 100), K(1 ≤ K ≤ 5)가 주어진다. 다음 N개의 줄에는 M개의 알파벳 대문자가 주어지는데, 이는 N×M 크기의 문자판을 나타낸다. 다음 줄에는 1자 이상 80자 이하의 영단어가 주어진다. 모든 문자들은 알파벳 대문자이며, 공백 없이 주어진다.
### **출력**
첫째 줄에 경로의 개수를 출력한다. 이 값은 $2^{31}-1$보다 작거나 같다.
### **예제입출력**

**예제 입력1**

```
4 4 1
KAKT
XEAS
YRWU
ZBQP
BREAK
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, K = map(int, input().split())
table = [list(input()) for _ in range(N)]
target = input()
target_len = len(target)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dp = [[[-1] * target_len for _ in range(M)] for _ in range(N)]

def dfs(x, y, idx):
    if idx == len(target):
        return 1
    
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]
    
    count = 0
    for i in range(4):
        for step in range(1, K+1):
            nx, ny = x + dx[i] * step, y + dy[i] * step
            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == target[idx]:
                count += dfs(nx, ny, idx + 1)

    dp[x][y][idx] = count
    return count

result = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == target[0]:
            result += dfs(i, j, 1)

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121588|1008|PyPy3|790
#### **📝해설**

**알고리즘**
```
1. DP
2. DFS
```

### **다른 풀이**

```python
import sys; input = sys.stdin.readline

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(lv, i, j):
    if lv == 0:
        return 1
    if ~dp[lv][i][j]:
        return dp[lv][i][j]
    dp[lv][i][j] = 0
    for di, dj in dir:
        ii = i; jj = j
        for _ in range(K):
            ii += di; jj += dj
            if not (0 <= ii < N and 0 <= jj < M):
                break
            if matrix[ii][jj] == word[lv - 1]:
                dp[lv][i][j] += dfs(lv - 1, ii, jj)
    return dp[lv][i][j]

N, M, K = map(int, input().split())
matrix = [input().strip() for _ in range(N)]
word = input().strip()
L = len(word)

dp = [[[-1] * M for _ in range(N)] for _ in range(L)]
result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == word[L - 1]:
            result += dfs(L - 1, i, j)
print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
vkdldjvkdnj|36944|92|Python3|823
#### **📝해설**

```python
# 입력받기
N, M, K = map(int, input().split())
table = [list(input()) for _ in range(N)]
target = input()
target_len = len(target)

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# DP배열을 통해 메모리제이션, DP[i][j][k] : (i, j)위치에서 k번째 문자열까지 만들었을 때 경우의 수를 미리 계산
dp = [[[-1] * target_len for _ in range(M)] for _ in range(N)]

# DFS 함수
def dfs(x, y, idx):

    # 문자열을 완성헀다면 1을 리턴하고 종료
    if idx == len(target):
        return 1
    
    # 이미 계산한 위치라면 그 값을 그대로 반환
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]
    
    # 현재 위치에서 문자열을 완성할 수 있는 경우의 수
    count = 0

    # 상하좌우 주어진 범위까지 탐색
    for i in range(4):
        for step in range(1, K+1):
            nx, ny = x + dx[i] * step, y + dy[i] * step
            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == target[idx]:

                # 재귀적으로 함수를 호출하면서 경우의 수를 찾음
                count += dfs(nx, ny, idx + 1)

    # 해당 위치의 경우의 수를 저장
    dp[x][y][idx] = count

    # 최종적으로 해당 위치에서 만들 수 있는 총 경우의 수를 반환
    return count

# 주어진 배열을 순회하면서 시작 위치를 찾음
result = 0
for i in range(N):
    for j in range(M):
        # 모든 시작위치에서 DFS
        if table[i][j] == target[0]:
            result += dfs(i, j, 1)

# 총 경우의 수
print(result)
```