# [18428] 감시 피하기

### **난이도**
골드 5
## **📝문제**
NxN 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.

각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.

다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자. 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다. 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다. 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다. 



이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.

학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다. NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.

예를 들어 N=5일 때, 다음과 같이 선생님 및 학생의 위치 정보가 주어졌다고 가정하자.



이 때 다음과 같이 3개의 장애물을 설치하면, 모든 학생들을 선생님의 감시로부터 피하도록 만들 수 있다.


### **입력**
첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6) 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.

단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.
### **출력**
첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다. 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
```

**예제 출력1**

```
YES
```

**예제 입력2**

```
4
S S S T
X X X X
X X X X
T T T X
```

**예제 출력2**

```
NO
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

N = int(input())
table = [list(input().split()) for _ in range(N)]


obstacle = []
students = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 'X':
            obstacle.append([i, j])
        elif table[i][j] == 'S':
            students.append([i, j])
        
obs_comb = list(combinations(obstacle, 3))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def f(students):

    for student in students:
        x, y = student
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < N and 0 <= ny < N:
                
                if table[nx][ny] == 'O':
                    break
                elif table[nx][ny] == 'T':
                    return False
                
                nx += dx[i]
                ny += dy[i]
                

    return True

for case in obs_comb:
    
    for x, y in case:
        table[x][y] = 'O'
    
    flag = f(students)

    if flag:
        break
        
    for x, y in case:
        table[x][y] = 'X'


if flag:
    print('YES')
else:
    print('NO')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|56|Python3|1114
#### **📝해설**

**알고리즘**
```
1. 브루트포스 알고리즘
```

#### **😅개선점**

1. 백트래킹을 사용했다면 N이 더 큰 케이스에서도 적은 시간으로 풀릴 것이다.

### **다른 풀이**

```python
import sys
import itertools
input = sys.stdin.readline

def look_for(target: str, n: int):
    rtn = []
    for i in range(n):
        for j in range(n):
            if room[i][j] == target:
                rtn.append((i,j))
    return rtn

def eyesight(n: int):
    rtn = set()
    
    for teacher in teachers:
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            flag = 0
            lst = []
            ni = teacher[0] + d[0]
            nj = teacher[1] + d[1]
            while 0 <= ni < n and 0 <= nj < n:
                if room[ni][nj] == 'T':
                    break
                elif room[ni][nj] == 'S':
                    flag = 1
                else:
                    lst.append((ni, nj))
                ni += d[0]
                nj += d[1]
            
            if flag and lst:
                for v in lst:
                    rtn.add(v)
    return rtn


def teachers_bfs(n):
    
    for teacher in teachers:
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = teacher[0] + d[0]
            nj = teacher[1] + d[1]
            while 0 <= ni < n and 0 <= nj < n:
                if room[ni][nj] == 'S':
                    return 0
                elif room[ni][nj] == 'O' or room[ni][nj] == 'T' :
                    break
                ni += d[0]
                nj += d[1]
    return 1


def OX(val: str, arr: list):
    for x, y in arr:
        room[x][y] = val

if __name__ == "__main__":
    N = int(input())
    room = [list(input().split()) for _ in range(N)]
    teachers = look_for('T', N)
    eyes = eyesight(N)
    eyes_len = len(eyes)

    res = 'NO'
    if eyes_len == 0:
        res = 'YES'
    elif eyes_len == 1:
        for x,y in eyes:
            room[x][y] = 'O'
            if teachers_bfs(N):
                res = 'YES'
                break
            room[x][y] = 'X'
            
    elif eyes_len == 2:
        X_lst = itertools.combinations(eyes, 2)
        for X_val in X_lst:
            OX('O', X_val)
            if teachers_bfs(N):
                res = 'YES'
                break
            OX('X', X_val)

    else:
        X_lst = itertools.combinations(eyes, 3)
        for X_val in X_lst:
            OX('O', X_val)
            if teachers_bfs(N):
                res = 'YES'
                break
            OX('X', X_val)

    print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pc5401|31120|40|Python03|2331
#### **📝해설**

```python
from itertools import combinations

N = int(input())
table = [list(input().split()) for _ in range(N)]

# 빈공간의 위치를 담을 리스트
obstacle = []
# 학생의 위치를 담을 리스트
students = []

# 테이블을 순회하면서 학생, 빈공간의 위치를 리스트에 삽입
for i in range(N):
    for j in range(N):
        if table[i][j] == 'X':
            obstacle.append([i, j])
        elif table[i][j] == 'S':
            students.append([i, j])
        
# 모든 빈공간을 길이가 3인 조합으로 만들어줌
# 이 조합 하나하나가 장애물을 배치할 케이스
obs_comb = list(combinations(obstacle, 3))

# 상하좌우 이동을 위한 리스트 선언
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 종료 조건을 만나면 return하기 위해 함수로 선언
def f(students):

    # 모든 학생들의 위치를 확인하면서
    for student in students:
        x, y = student
        
        # 동서남북으로 인덱스의 범위 안까지 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < N and 0 <= ny < N:
                
                # 도중에 장애물을 만난다면 이쪽 방향으로의 탐색을 종료
                if table[nx][ny] == 'O':
                    break
                # 도중에 선생님을 만난다면 False를 return
                elif table[nx][ny] == 'T':
                    return False
                
                # 한쪽 방향으로 계속 이동(인덱스를 벗어날 때까지)
                nx += dx[i]
                ny += dy[i]
                
    # return False를 한번도 하지 않고 루프를 탈출했다면 True를 return
    return True

# 모든 생성된 조합에 대해서 확인
for case in obs_comb:
    
    # 현재 케이스의 장애물 배치
    for x, y in case:
        table[x][y] = 'O'
    
    # 현재 케이스에서 정답 여부 확인
    flag = f(students)

    # 만약 True라면 다른 케이스는 검사하지 않아도 됨
    # break
    if flag:
        break
    
    # 현재 케이스의 장애물을 원래대로 되돌림
    for x, y in case:
        table[x][y] = 'X'

# 정답 출력
if flag:
    print('YES')
else:
    print('NO')
```

### **🔖정리**

1. 배운점