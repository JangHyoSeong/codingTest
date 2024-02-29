# 문제 제목
N-Queen
## **📝문제 설명**
체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때, n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.
### **⚠제한사항**
- 퀸(Queen)은 가로, 세로, 대각선으로 이동할 수 있습니다.
- n은 12이하의 자연수 입니다.
### **입출력 예**
|n|	result|
|:---:|:---:|
|4|	2|
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**

### **🧾나의 풀이**

```python
count = 0

def queen(line, n, board):
    global count
    
    if line == n:
        count += 1
        return
        
    for i in range(n):
        if is_safe(line, i, n, board):
            board[line][i] = 1
            queen(line + 1, n, board)
            board[line][i] = 0
            
def is_safe(x, y, n, board):
    
    for i in range(x):
        if board[i][y] == 1:
            return False
    
    
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
   
    i = x - 1
    j = y + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solution(n):
    board = [[0] * n for _ in range(n)]
    queen(0, n, board)
    return count
```

#### **📝해설**
백트래킹을 사용하여 조건을 만족하지 못한다면 더이상 진행하지 않고 종료하여 실행횟수를 줄인다

```python
count = 0

def queen(line, n, board):
    global count
    
    # 마지막까지 문제없이 도달했다면 count증가
    if line == n:
        count += 1
        return
    
    # 이번 줄에서 n번 반복하여 각 위치에 queen을 놓을 수 있다면 놓고 다음 줄로 이동
    for i in range(n):
        if is_safe(line, i, n, board):
            board[line][i] = 1
            queen(line + 1, n, board)
            # 백트래킹을 위하여 위치 초기화
            board[line][i] = 0
            
def is_safe(x, y, n, board):
    # 가로세로대각선에 퀸이 있는지 파악하는 함수
    for i in range(x):
        # 현재 줄에 퀸이 있다면 종료
        if board[i][y] == 1:
            return False
    
    # 왼쪽 위 대각선에 퀸이 있다면 종료
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # 오른쪽 위 대각선에 퀸이 있다면 종료
    i = x - 1
    j = y + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    #아래는 아직 퀸을 안놓았으므로 검사하지 않아도 무방

    return True

def solution(n):
    board = [[0] * n for _ in range(n)]
    queen(0, n, board)
    return count
```

#### **😅개선점**

1. 다른 방식으로도 풀어보자

### **다른 풀이**

```python
ans = 0
num = 0
chkX = [False for i in range(32)]
chkCross1 = [False for i in range(32)]
chkCross2 = [False for i in range(32)]

def nq(y, n):
    global ans
    x = 0
    if y > n:
        ans+=1
    for x in range(1, n+1):
        if chkX[x] or chkCross1[y + x] or chkCross2[(y - x) + n]:
            continue
        chkX[x] = True
        chkCross1[y + x] = True
        chkCross2[(y - x) + n] = True

        nq(y + 1, n)
        chkX[x] = False
        chkCross1[y + x] = False
        chkCross2[(y - x) + n] = False

def solution(n):
    nq(1, n)
    return ans
```

### **🔖정리**

1. 백트래킹 활용시 조건을 잘 생각하자

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12952)**<br/>
