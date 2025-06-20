# [10157] 자리배정

### **난이도**
실버 3
## **📝문제**
어떤 공연장에는 가로로 C개, 세로로 R개의 좌석이 C×R격자형으로 배치되어 있다. 각 좌석의 번호는 해당 격자의 좌표 (x,y)로 표시된다. 

예를 들어보자. 아래 그림은 가로 7개, 세로 6개 좌석으로 구성된 7×6격자형 좌석배치를 보여주고 있다. 그림에서 각 단위 사각형은 개별 좌석을 나타내며, 그 안에 표시된 값 (x,y)는 해당 좌석의 번호를 나타낸다. 가장 왼쪽 아래의 좌석번호는 (1,1)이며, 가장 오른쪽 위 좌석의 번호는 (7,6)이다. 

이 공연장에 입장하기 위하여 많은 사람이 대기줄에 서있다. 기다리고 있는 사람들은 제일 앞에서부터 1, 2, 3, 4, . 순으로 대기번호표를 받았다. 우리는 대기번호를 가진 사람들에 대하여 (1,1)위치 좌석부터 시작하여 시계방향으로 돌아가면서 비어있는 좌석에 관객을 순서대로 배정한다. 이것을 좀 더 구체적으로 설명하면 다음과 같다.

먼저 첫 번째 사람, 즉 대기번호 1인 사람은 자리 (1,1)에 배정한다. 그 다음에는 위쪽 방향의 좌석으로 올라가면서 다음 사람들을 배정한다. 만일 더 이상 위쪽 방향으로 빈 좌석이 없으면 오른쪽으로 가면서 배정한다. 오른쪽에 더 이상 빈자리가 없으면 아래쪽으로 내려간다. 그리고 아래쪽에 더 이상 자리가 없으면 왼쪽으로 가면서 남은 빈 좌석을 배정한다. 이 후 왼쪽으로 더 이상의 빈 좌석이 없으면 다시 위쪽으로 배정하고, 이 과정을 모든 좌석이 배정될 때까지 반복한다. 

아래 그림은 7×6공연장에서 대기번호 1번부터 42번까지의 관객이 좌석에 배정된 결과를 보여주고 있다.

여러분은 공연장의 크기를 나타내는 자연수 C와 R이 주어져 있을 때, 대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)를 찾는 프로그램을 작성해야 한다. 
### **입력**
첫 줄에는 공연장의 격자 크기를 나타내는 정수 C와 R이 하나의 공백을 사이에 두고 차례대로 주어진다. 두 값의 범위는 5 ≤ C, R ≤ 1,000이다. 그 다음 줄에는 어떤 관객의 대기번호 K가 주어진다. 단 1 ≤ K ≤ 100,000,000이다.
### **출력**
입력으로 제시된 대기번호 K인 관객에게 배정될 좌석번호 (x,y)를 구해서 두 값, x와 y를 하나의 공백을 사이에 두고 출력해야 한다. 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력해야 한다. 
### **예제입출력**

**예제 입력1**

```
7 6
11
```

**예제 출력1**

```
6 6
```

**예제 입력2**

```
7 6
87
```

**예제 출력2**

```
0
```

**예제 입력3**

```
100 100
3000
```

**예제 출력3**

```
9 64
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    exit()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

seats = [[0] * C for _ in range(R)]

x, y = 0, 0
direction = 0

for num in range(1, K + 1):
    seats[y][x] = num
    if num == K:
        print(x + 1, y + 1)
        break

    ny = y + dy[direction]
    nx = x + dx[direction]

    if ny < 0 or ny >= R or nx < 0 or nx >= C or seats[ny][nx] != 0:
        direction = (direction + 1) % 4
        ny = y + dy[direction]
        nx = x + dx[direction]

    y, x = ny, nx
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|56428|588|Python3|547
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input().rstrip())



def sol():
    if K > C * R:
        print(0)
        return
    
    i = 0
    offset = 0
    prev = 0
    while offset < K:
        i += 1
        prev = offset
        offset += ((C - (2 * i)) + (R - (2 * (i - 1)))) * 2
    
    
    check = K - prev
    y = i - 1
    x = i

    if check - (R - (2 * (i - 1))) > 0:
        check -= (R - (2 * (i - 1)))
        y += (R - (2 * (i - 1)))
    else:
        print(x, y + check)
        return

    if check - (C - (2 * i)) > 0:
        check -= (C - (2 * i))
        x += (C - (2 * i)) + 1
    else: 
        print(x + check, y)
        return
    
    if check - (R - (2 * (i - 1))) > 0:
        check -= (R - (2 * (i - 1)))
        y -= ((R - (2 * (i - 1))) - 1)
    else:
        print(x, y - check + 1)
        return
    
    print(x - check, y)
        
sol()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
xowns97|30616|36|Python3|917
#### **📝해설**

```python
C, R = map(int, input().split())
K = int(input())

# K가 불가능한 숫자라면 0을 출력하고 종료
if K > C * R:
    print(0)
    exit()

# 상하좌우 이동을 위한 리스트
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 2차원 배열로 자리를 저장
seats = [[0] * C for _ in range(R)]

# 현재 위치
x, y = 0, 0
# 현재 이동방향
direction = 0

# K번 반복
for num in range(1, K + 1):
    seats[y][x] = num
    
    # K번 반복이 끝났다면 출력 후 종료
    if num == K:
        print(x + 1, y + 1)
        break
    
    # 다음 이동할 좌표
    ny = y + dy[direction]
    nx = x + dx[direction]

    # 인덱스를 벗어나거나 이미 있는 자리를 만난다면 방향을 바꿈
    if ny < 0 or ny >= R or nx < 0 or nx >= C or seats[ny][nx] != 0:
        direction = (direction + 1) % 4
        ny = y + dy[direction]
        nx = x + dx[direction]

    y, x = ny, nx
```