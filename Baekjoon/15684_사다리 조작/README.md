# [15684] 사다리 조작

### **난이도**
골드 3
## **📝문제**
사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져 있다. 인접한 세로선 사이에는 가로선을 놓을 수 있는데, 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고, 모든 세로선이 같은 위치를 갖는다. 아래 그림은 N = 5, H = 6 인 경우의 그림이고, 가로선은 없다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15684/1.png)

초록선은 세로선을 나타내고, 초록선과 점선이 교차하는 점은 가로선을 놓을 수 있는 점이다. 가로선은 인접한 두 세로선을 연결해야 한다. 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15684/2.png)

위의 그림에는 가로선이 총 5개 있다. 가로선은 위의 그림과 같이 인접한 두 세로선을 연결해야 하고, 가로선을 놓을 수 있는 위치를 연결해야 한다.

사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다. 이때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.

위의 그림에서 1번은 3번으로, 2번은 2번으로, 3번은 5번으로, 4번은 1번으로, 5번은 4번으로 도착하게 된다. 아래 두 그림은 1번과 2번이 어떻게 이동했는지 나타내는 그림이다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15684/3.png) | ![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15684/2.png)|
---------|----------
 1번 세로선 | 2번 세로선

사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 이때, i번 세로선의 결과가 i번이 나와야 한다. 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)

둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.

가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.

가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가한다. 세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.

입력으로 주어지는 가로선이 서로 연속하는 경우는 없다.
### **출력**
i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력한다. 만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
2 0 3
```

**예제 출력1**

```
0
```

**예제 입력2**

```
2 1 3
1 1
```

**예제 출력2**

```
1
```

**예제 입력3**

```
5 5 6
1 1
3 2
2 3
5 1
5 4
```

**예제 출력3**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M, H = map(int, sys.stdin.readline().rstrip().split())
ladder = [[False] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a][b] = True

def check():
    for i in range(1, N+1):
        pos = i

        for j in range(1, H+1):
            if ladder[j][pos]:
                pos += 1
            elif pos > 1 and ladder[j][pos - 1]:
                pos -= 1
        
        if pos != i:
            return False
    return True

result = 4

def dfs(count, x, y):
    global result

    if count >= result:
        return

    if check():
        if result > count:
            result = count
        return

    for i in range(x, H+1):
        k = y if i == x else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(count + 1, i, j)
                ladder[i][j] = False

dfs(0, 1, 1)
print(result if result <= 3 else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111928|3584|PyPy3|1019
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
N, M, H = map(int, input().split())     #  2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H

line = [[0]* (N) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    line[a-1][b-1] = 1
    line[a-1][b] = 2


def check():
    same = 0
    for s in range(N):
        now = s
        for j in range(H):
            if line[j][now] == 1: now += 1
            elif line[j][now] == 2: now -= 1
        if now == s: same += 1
    return same


def dfs(n):
    global answer

    if answer != -1:
        return
    
    temp = check()
    if temp+(cnt-n)*2 < N:
        return

    if n == cnt:
        if temp == N:
            answer = cnt
        return
    
    for i in range(H):
        for j in range(N-1):
            if line[i][j] or line[i][j+1]: continue
            line[i][j], line[i][j+1] = 1, 2
            dfs(n+1)
            line[i][j], line[i][j+1] = 0, 0


answer = -1
for cnt in range(4):
    dfs(0)
    if answer != -1: break

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ssbin407|31120|36|Python3|983
#### **📝해설**

```python
import sys

N, M, H = map(int, sys.stdin.readline().rstrip().split())
# 사다리의 상태를 나타내는 이차원 리스트
# ladder[a][b] : a번째 가로줄에 b와 b+1 사이 위치에 가로선이 있음
ladder = [[False] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a][b] = True

# 모든 사다리가 원래 세로선으로 돌아오는지 확인하는 함수
def check():
    for i in range(1, N+1):
        pos = i

        for j in range(1, H+1):
            if ladder[j][pos]:
                pos += 1
            elif pos > 1 and ladder[j][pos - 1]:
                pos -= 1
        
        if pos != i:
            return False
    return True

# 최대값은 3까지이니, 초기값을 3 이상으로 설정
result = 4

# DFS를 통해 최소값을 구함
def dfs(count, x, y):
    global result

    # 만약, 이미 최소값을 넘긴 케이스라면 고려하지 않음
    if count >= result:
        return

    # 이번 탐색에서 세로선이 모두 원래대로 돌아온다면
    if check():

        # 최소값이 갱신 가능하다면 갱신
        if result > count:
            result = count
        return

    # 가로선을 추가하는 로직
    for i in range(x, H+1):
        k = y if i == x else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(count + 1, i, j)
                ladder[i][j] = False

dfs(0, 1, 1)
print(result if result <= 3 else -1)
```