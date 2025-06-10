# [14891] 톱니바퀴

### **난이도**
골드 5
## **📝문제**
총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/1.png)

이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/2.png)
![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/3.png)

톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 예를 들어, 아래와 같은 경우를 살펴보자.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/4.png)

두 톱니바퀴의 맞닿은 부분은 초록색 점선으로 묶여있는 부분이다. 여기서, 3번 톱니바퀴를 반시계 방향으로 회전했다면, 4번 톱니바퀴는 시계 방향으로 회전하게 된다. 2번 톱니바퀴는 맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되고, 1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다. 따라서, 아래 그림과 같은 모양을 만들게 된다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/5.png)

위와 같은 상태에서 1번 톱니바퀴를 시계 방향으로 회전시키면, 2번 톱니바퀴가 반시계 방향으로 회전하게 되고, 2번이 회전하기 때문에, 3번도 동시에 시계 방향으로 회전하게 된다. 4번은 3번이 회전하지만, 맞닿은 극이 같기 때문에 회전하지 않는다. 따라서, 아래와 같은 상태가 된다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/6.png)

톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
### **출력**
총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.

- 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
- 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
- 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
- 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
### **예제입출력**

**예제 입력1**

```
10101111
01111101
11001110
00000010
2
3 -1
1 1
```

**예제 출력1**

```
7
```

**예제 입력2**

```
11111111
11111111
11111111
11111111
3
1 1
2 1
3 1
```

**예제 출력2**

```
15
```

**예제 입력3**

```
10001011
10000011
01011011
00111101
5
1 1
2 1
3 1
4 1
1 -1
```

**예제 출력3**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

gears = [deque(map(int, input())) for _ in range(4)]
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

def rotate(gear: deque, direction):
    if direction == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())
    
for gear_num, direction in moves:
    gear_num -= 1
    rotate_dirs = [0] * 4
    rotate_dirs[gear_num] = direction

    for i in range(gear_num-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            rotate_dirs[i] = -rotate_dirs[i+1]
        else:
            break
    
    for i in range(gear_num + 1, 4):
        if gears[i-1][2] != gears[i][6]:
            rotate_dirs[i] = -rotate_dirs[i-1]
        else:
            break
    
    for i in range(4):
        if rotate_dirs[i] != 0:
            rotate(gears[i], rotate_dirs[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)
print(score)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34976|60|Python3|945
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline
# from collections import deque
# dij = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

def rolling(number, direction):
    visited.add(number)
    left = number - 1
    right = number + 1
    newDirection = -direction
    if left not in visited and 0 <= left and chains[left][2] != chains[number][6]:
        rolling(left, newDirection)
    if right not in visited and right < 4 and chains[right][6] != chains[number][2]:
        rolling(right, newDirection)
    if direction == 1:
        chains[number] = chains[number][-1] + chains[number][:-1]
    else:
        chains[number] = chains[number][1:] + chains[number][0]

chains = []
for t in range(4):
    chains.append(input().replace("\n", ""))

K = int(input())
for k in range(K):
    num, direct = map(int, input().split())
    visited = set()
    rolling(num-1, direct)

result = 0
for i in range(4):
    result += int(chains[i][0])*(2**i)
print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dltkdgns0303|31120|32|Python3|941
#### **📝해설**

```python
from collections import deque

# deque로 gear를 입력받음
gears = [deque(map(int, input())) for _ in range(4)]
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

# 톱니바퀴를 회전하는 함수
def rotate(gear: deque, direction):

    # 시계방향이라면
    if direction == 1:
        # 숫자를 하나씩 밀어냄
        gear.appendleft(gear.pop())

    # 반시계라면
    else:
        # 하나씩 당김
        gear.append(gear.popleft())

# 톱니바퀴 회전
for gear_num, direction in moves:
    # 인덱싱을 위해 -1
    gear_num -= 1

    # 이번 움직임에서 네 톱니바퀴의 이동 방향을 저장
    rotate_dirs = [0] * 4
    rotate_dirs[gear_num] = direction

    # 현재 톱니부터 시작해서 왼쪽으로 검사
    for i in range(gear_num-1, -1, -1):

        # 같은 극이 아니라면
        if gears[i][2] != gears[i+1][6]:
            # 회전 방향을 바꿈
            rotate_dirs[i] = -rotate_dirs[i+1]
        
        # 같은 극이라면 회전하지않고 종료
        else:
            break
    
    # 오른쪽으로 검사도 동일
    for i in range(gear_num + 1, 4):
        if gears[i-1][2] != gears[i][6]:
            rotate_dirs[i] = -rotate_dirs[i-1]
        else:
            break
    
    # 네 톱니바퀴를 검사하면서 회전시킴
    for i in range(4):
        if rotate_dirs[i] != 0:
            rotate(gears[i], rotate_dirs[i])

# 총 점수를 구함
score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)
print(score)
```