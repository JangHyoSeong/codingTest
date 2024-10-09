# [17136] 문제제목

### **난이도**
골드 2
## **📝문제**
<그림 1>과 같이 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.



<그림 1>

색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.

종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.
### **입력**
총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.

### **출력**
모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.

### **예제입출력**

**예제 입력1**

```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

**예제 출력1**

```
0
```

**예제 입력2**

```
0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

**예제 출력2**

```
4
```

**예제 입력3**

```
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

**예제 출력3**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def can_attach(x, y, size):
    # 주어진 위치 (x, y)에서 크기 size의 색종이를 붙일 수 있는지 확인
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if table[x + i][y + j] != 1 or visited[x + i][y + j]:
                return False
    return True

def attach(x, y, size, flag):
    # 주어진 위치 (x, y)에 크기 size의 색종이를 붙이거나 떼기 (flag: True 붙이기, False 떼기)
    for i in range(size):
        for j in range(size):
            visited[x + i][y + j] = flag

def dfs(cnt):
    global min_count
    if cnt >= min_count:
        return
    # 모든 1이 덮였는지 확인
    if all(all(visited[i][j] or table[i][j] == 0 for j in range(10)) for i in range(10)):
        min_count = min(min_count, cnt)
        return

    for i in range(10):
        for j in range(10):
            if table[i][j] == 1 and not visited[i][j]:
                for size in range(5, 0, -1):
                    if used[size] < 5 and can_attach(i, j, size):
                        attach(i, j, size, True)
                        used[size] += 1
                        dfs(cnt + 1)
                        attach(i, j, size, False)
                        used[size] -= 1
                return

table = [list(map(int, input().split())) for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
used = [0] * 6
min_count = float('inf')

dfs(0)
print(-1 if min_count == float('inf') else min_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|3528|Python3|1517
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```
### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def checkcheck(r, c, count):
    global paper_count, failed
    if count >= paper_count:
        return
    
    if r == 10:
        if count < paper_count:
            paper_count = count
        return
    if c == 0:
        col_check = 0
        for i in range(10):
            if board[r][i]:
                col_check |= 1<<i
        
        if str(papers) in dp[r][col_check]:
            if dp[r][col_check][str(papers)] > count:
                dp[r][col_check][str(papers)] = count
            else:
                return
        else:
            dp[r][col_check][str(papers)] = count
            
    elif c == 10:
        checkcheck(r+1, 0, count)
        return
    
    marked = is_marked(r,c)
    if marked:
        for i in range(1, marked+1):
            if papers[i-1]>0:
                mark(r,c,i,0)
                papers[i-1]-=1
                checkcheck(r,c+i,count+1)
                mark(r,c,i,1)
                papers[i-1]+=1
            else:
                failed = True
    else:
        checkcheck(r,c+1,count)
    return


def is_marked(r,c):
    if board[r][c]:
        if r < 6 and c < 6:
            if sum([sum(board[r+i][c:c+5]) for i in range(5)]) == 25:
                return 5
        if r < 7 and c < 7:
            if sum([sum(board[r+i][c:c+4]) for i in range(4)]) == 16:
                return 4
        if r < 8 and c < 8:
            if sum([sum(board[r+i][c:c+3]) for i in range(3)]) == 9:
                return 3
        if r < 9 and c < 9:
            if sum([sum(board[r+i][c:c+2]) for i in range(2)]) == 4:
                return 2
        return 1
    else:
        return 0

def mark(r,c,size, flag):
    for dr in range(size):
        for dc in range(size):
            board[r+dr][c+dc] = flag
   

board = [list(map(int,input().split())) for _ in range(10)]
papers = [5,5,5,5,5]
dp = [[{} for _ in range(1024)] for _ in range(10)]
paper_count = 30
failed = False
checkcheck(0,0,0)
if paper_count == 30:
    paper_count = 0
if not paper_count and failed:
    print(-1)
else:
    print(paper_count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
toto9091|30476|236|Python3|2097
#### **📝해설**

```python
def can_attach(x, y, size):
    # 주어진 위치 (x, y)에서 크기 size의 색종이를 붙일 수 있는지 확인
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if table[x + i][y + j] != 1 or visited[x + i][y + j]:
                return False
    return True

def attach(x, y, size, flag):
    # 주어진 위치 (x, y)에 크기 size의 색종이를 붙이거나 떼기 (flag: True 붙이기, False 떼기)
    for i in range(size):
        for j in range(size):
            visited[x + i][y + j] = flag

def dfs(cnt):
    global min_count
    if cnt >= min_count:
        return
    # 모든 1이 덮였는지 확인
    if all(all(visited[i][j] or table[i][j] == 0 for j in range(10)) for i in range(10)):
        min_count = min(min_count, cnt)
        return

    for i in range(10):
        for j in range(10):
            if table[i][j] == 1 and not visited[i][j]:
                for size in range(5, 0, -1):
                    if used[size] < 5 and can_attach(i, j, size):
                        attach(i, j, size, True)
                        used[size] += 1
                        dfs(cnt + 1)
                        attach(i, j, size, False)
                        used[size] -= 1
                return

table = [list(map(int, input().split())) for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
used = [0] * 6
min_count = float('inf')

dfs(0)
print(-1 if min_count == float('inf') else min_count)
```