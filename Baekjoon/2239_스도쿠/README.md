# [2239] 스도쿠

### **난이도**
골드 4
## **📝문제**
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.

[이미지](https://www.acmicpc.net/JudgeOnline/upload/201008/sdk.png)

위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.

하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.
### **입력**
9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.
### **출력**
9개의 줄에 9개의 숫자로 답을 출력한다. 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다. 즉, 81자리의 수가 제일 작은 경우를 출력한다.
### **예제입출력**

**예제 입력1**

```
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
```

**예제 출력1**

```
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
table = [list(map(int, input())) for _ in range(9)]

empty = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]

def is_valid(x, y, num):
    for i in range(9):
        if table[x][i] == num or table[i][y] == num:
            return False
    
    box_x = (x // 3) * 3
    box_y = (y //3 ) * 3

    for i in range(3):
        for j in range(3):
            if table[box_x + i][box_y + j] == num:
                return False
    
    return True

def solve(index):
    if index == len(empty):
        for row in table:
            print("".join(map(str, row)))

        exit()
    
    x, y = empty[index]
    for num in range(1, 10):
        if is_valid(x, y, num):
            table[x][y] = num
            solve(index + 1)
            table[x][y] = 0
    
solve(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|140436|3652|PyPy3|781
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
input = open(0).readline

def square(i, j):
    return (i // 3) * 3 + j // 3

def fill_bit(i, j, n, bit_board):
    bit_board[i * 9 + j] = 0b1111111110
    bit = 1 << n
    for ii in range(9):
        bit_board[ii * 9 + j] |= bit
    for jj in range(9):
        bit_board[i * 9 + jj] |= bit
    i = i // 3 * 3
    j = j // 3 * 3
    for ii in range(3):
        for jj in range(3):
            bit_board[(i + ii) * 9 + j + jj] |= bit
    return bit_board

def check(i, j, n, check_rcs):
    if check_rcs[i] & (1 << n) or check_rcs[9 + j] & (1 << n) or check_rcs[18 + square(i, j)] & (1 << n):
        return False, check_rcs
    check_rcs[i] |= 1 << n
    check_rcs[9 + j] |= 1 << n
    check_rcs[18 + square(i, j)] |= 1 << n
    return True, check_rcs

def fill(i, j, n, board, bit_board, check_rcs):
    board[i * 9 + j] = n
    bit_board = fill_bit(i, j, n, bit_board)
    ok, check_rcs = check(i, j, n, check_rcs)
    return ok, board, bit_board, check_rcs

def fill_one_blank(board, bit_board, check_rcs):
    fill_count = 0
    for n in range(1, 10):
        for i in range(9):
            count = 0
            for j in range(9):
                if bit_board[i * 9 + j] & (1 << n):
                    count += 1
                else:
                    fj = j
            if count == 8:
                fill_count += 1
                ok, board, bit_board, check_rcs = fill(i, fj, n, board, bit_board, check_rcs)
                if not ok:
                    return False, board, bit_board, check_rcs
        for j in range(9):
            count = 0
            for i in range(9):
                if bit_board[i * 9 + j] & (1 << n):
                    count += 1
                else:
                    fi = i
            if count == 8:
                fill_count += 1
                ok, board, bit_board, check_rcs = fill(fi, j, n, board, bit_board, check_rcs)
                if not ok:
                    return False, board, bit_board, check_rcs
        for i in range(3):
            for j in range(3):
                count = 0
                for ii in range(3):
                    for jj in range(3):
                        ni = i * 3 + ii
                        nj = j * 3 + jj
                        if bit_board[ni * 9 + nj] & (1 << n):
                            count += 1
                        else:
                            fi, fj = ni, nj
                if count == 8:
                    fill_count += 1
                    ok, board, bit_board, check_rcs = fill(fi, fj, n, board, bit_board, check_rcs)
                    if not ok:
                        return False, board, bit_board, check_rcs
    if fill_count:
        ok, board, bit_board, check_rcs = fill_one_blank(board, bit_board, check_rcs)
        if not ok:
            return False, board, bit_board, check_rcs
    return True, board, bit_board, check_rcs

def solve(z, board, bit_board, check_rcs):
    if z == 81:
        for i in range(9):
            print(*board[i * 9 : i * 9 + 9], sep='')
        return True, board, bit_board, check_rcs
    if board[z] != 0:
        return solve(z + 1, board, bit_board, check_rcs)
    i = z // 9
    j = z % 9
    for n in range(1, 10):
        if check_rcs[i] & (1 << n) == 0 and check_rcs[9 + j] & (1 << n) == 0 and check_rcs[18 + square(i, j)] & (1 << n) == 0:
            _, nboard, nbit_board, ncheck_rcs = fill(i, j, n, [*board], [*bit_board], [*check_rcs])
            ok, nboard, nbit_board, ncheck_rcs = solve(z + 1, nboard, nbit_board, ncheck_rcs)
            if ok:
                return True, nboard, nbit_board, ncheck_rcs
    return False, board, bit_board, check_rcs

def main():
    board = [0] * 81
    bit_board = [0] * 81
    check_rcs = [0] * 27
    for i in range(9):
        for j, num in enumerate(map(int, input().rstrip())):
            if num != 0:
                ok, board, bit_board, check_rcs = fill(i, j, num, board, bit_board, check_rcs)
    ok, board, bit_board, check_rcs = fill_one_blank(board, bit_board, check_rcs)
    solve(0, board, bit_board, check_rcs)

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
minskai|31132|68|Python3|4054
#### **📝해설**

```python
table = [list(map(int, input())) for _ in range(9)]

# 비어있는 칸들의 인덱스를 저장하는 리스트
empty = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]

# 해당 위치에 num이 들어갈 수 있는지 검사하는 함수
def is_valid(x, y, num):

    # 가로, 세로 줄을 검사
    for i in range(9):
        if table[x][i] == num or table[i][y] == num:
            return False
    
    box_x = (x // 3) * 3
    box_y = (y //3 ) * 3

    # 박스를 검사
    for i in range(3):
        for j in range(3):
            if table[box_x + i][box_y + j] == num:
                return False
    
    return True

# 백트래킹을 사용해 스도쿠의 빈칸을 채우는 함수
def solve(index):
    # 끝까지 채웠다면 출력 후 종료
    if index == len(empty):
        for row in table:
            print("".join(map(str, row)))

        exit()
    
    # 현재 채울 빈칸
    x, y = empty[index]

    # 1~9까지 모든 숫자를 대입해봄
    for num in range(1, 10):
        # 넣을 수 있는 숫자라면
        if is_valid(x, y, num):
            # 숫자를 넣고
            table[x][y] = num
            # 다음 빈칸으로 이동
            solve(index + 1)
            # 이후에 백트래킹을 위해 원래대로 되돌림
            table[x][y] = 0
    
solve(0)
```