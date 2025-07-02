# [7692] 틱택토

### **난이도**
골드 5
## **📝문제**
틱택토 게임은 두 명의 사람이 번갈아가며 말을 놓는 게임이다. 게임판은 3×3 격자판이며, 처음에는 비어 있다. 두 사람은 각각 X 또는 O 말을 번갈아가며 놓는데, 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 게임판이 가득 차도 게임은 끝난다.

게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하시오.
### **입력**
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다. '.'은 빈칸을 의미하며, 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 입력의 마지막에는 문자열 "end"가 주어진다.
### **출력**
각 테스트 케이스마다 한 줄에 정답을 출력한다. 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다.
### **예제입출력**

**예제 입력1**

```
XXXOO.XXX
XOXOXOXOX
OXOXOXOXO
XXOOOXXOX
XO.OX...X
.XXX.XOOO
X.OO..X..
OOXXXOOXO
end
```

**예제 출력1**

```
invalid
valid
invalid
valid
valid
invalid
invalid
invalid
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def is_win(board, player):

    win_lines = [
        [0,1,2], [3,4,5], [6,7,8],  # 가로
        [0,3,6], [1,4,7], [2,5,8],  # 세로
        [0,4,8], [2,4,6]            # 대각선
    ]
    for line in win_lines:
        if all(board[i] == player for i in line):
            return True
    return False

while True:
    line = input()
    if line == "end":
        break

    board = list(line)
    x_count = board.count('X')
    o_count = board.count('O')

    x_win = is_win(board, 'X')
    o_win = is_win(board, 'O')

    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
        continue

    valid = False
    if x_win and not o_win and x_count == o_count + 1:
        valid = True
    elif o_win and not x_win and x_count == o_count:
        valid = True
    elif not x_win and not o_win and x_count + o_count == 9:
        valid = True

    print("valid" if valid else "invalid")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|922
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
import sys
def game(tc, p):
    cases = [
        [tc[0], tc[4], tc[-1]],
        [tc[3], tc[4], tc[5]],
        [tc[1], tc[4], tc[7]],
        [tc[2], tc[4], tc[6]],
        [tc[0], tc[1], tc[2]],
        [tc[0], tc[3], tc[6]],
        [tc[6], tc[7], tc[-1]],
        [tc[2], tc[5], tc[-1]]
    ]
    return cases.count([p]*3)
while 1:
    tc = sys.stdin.readline().strip()
    if tc == 'end': break
    xl = game(tc, 'X')
    ol = game(tc, 'O')
    ans = 0
    if (xl > 0 and ol > 0) or xl > 2 or ol > 2:
        print('invalid')
        continue
    x = tc.count('X')
    o = tc.count('O')
    if xl or ol:
        if xl and x - 1 == o: ans = 1
        elif ol and x == o: ans = 1
    else:
        if '.' not in tc and x - 1 == o: ans = 1
    print('valid' if ans else 'invalid')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|31120|32|Python3|783
#### **📝해설**

```python

# 누가 이기는지 확인하는 함수
def is_win(board, player):

    # 승리할 때 줄 경우의 수
    win_lines = [
        [0,1,2], [3,4,5], [6,7,8],  # 가로
        [0,3,6], [1,4,7], [2,5,8],  # 세로
        [0,4,8], [2,4,6]            # 대각선
    ]

    # 입력받은 player가 이기는지 여부를 리턴
    for line in win_lines:
        if all(board[i] == player for i in line):
            return True
    return False

while True:
    line = input()
    if line == "end":
        break
    
    board = list(line)
    # x와 o의 개수를 세기
    x_count = board.count('X')
    o_count = board.count('O')

    # x, o가 이기는지 여부를 검사
    x_win = is_win(board, 'X')
    o_win = is_win(board, 'O')

    # x가 항상 선공이니 x와 o 개수가 같거나 x가 하나만 많아야함
    if not (x_count == o_count or x_count == o_count + 1):

        # 일단 이를 만족하지 못한다면 무조건 불가능한 케이스
        print("invalid")
        continue
    
    # 불가능한 케이스로 시작해서
    valid = False

    # x만 이기고, x가 o보다 하나많은경우 valid
    if x_win and not o_win and x_count == o_count + 1:
        valid = True
    
    # o만 이기고, x와 o가 같은 경우 valid
    elif o_win and not x_win and x_count == o_count:
        valid = True

    # 둘다 이기지 못했고 보드가 가득 찼다면 valid
    elif not x_win and not o_win and x_count + o_count == 9:
        valid = True

    print("valid" if valid else "invalid")

```