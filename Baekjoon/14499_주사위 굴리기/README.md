# [14499] 주사위 굴리기

### **난이도**
골드 4
## **📝문제**
크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

```
  2
4 1 3
  5
  6
```
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
### **입력**
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
### **출력**
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
### **예제입출력**

**예제 입력1**

```
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
```

**예제 출력1**

```
0
0
3
0
0
8
6
3
```

**예제 입력2**

```
3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3
```

**예제 출력2**

```
0
0
0
3
0
1
0
6
0
```

**예제 입력3**

```
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
```

**예제 출력3**

```
0
0
0
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, x, y, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for cmd in moves:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    x, y = nx, ny
    t = dice[:]
    if cmd == 1: # 동
        dice[1], dice[3], dice[6], dice[4] = t[4], t[1], t[3], t[6]

    elif cmd == 2: # 서
        dice[1], dice[4], dice[6], dice[3] = t[3], t[1], t[4], t[6]

    elif cmd == 3: # 북
        dice[1], dice[2], dice[6], dice[5] = t[5], t[1], t[2], t[6]

    else: # 남
        dice[1], dice[5], dice[6], dice[2] = t[2], t[1], t[5], t[6]
    
    if table[x][y] == 0:
        table[x][y] = dice[6]
    
    else:
        dice[6] = table[x][y]
        table[x][y] = 0

    print(dice[1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|870
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
n, m, x, y, k = map(int, input().split())

map_gird = []
for _ in range(n):
    map_gird.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0] * 6

def roll_dice(direc):
    if direc == 1:
        temp = dice[0]
        
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp

    elif direc == 2:
        temp = dice[0]

        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp

    elif direc == 3:
        temp = dice[0]

        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    
    elif direc == 4:
        temp = dice[0]

        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

for i in range(k):
    direc = command[i]

    nx = x + dx[direc]
    ny = y + dy[direc]

    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny

        roll_dice(direc)

        if map_gird[x][y] == 0:
            map_gird[x][y] = dice[5]
        
        else:
            dice[5] = map_gird[x][y]
            map_gird[x][y] = 0

        print(dice[0])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
nagihiko0704|31120|32|Python3|1220
#### **📝해설**

```python
N, M, x, y, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

# 주사위 각 칸을 리스트로 저장, 0번 인덱스는 더미
dice = [0] * 7

# 동서북남 이동(0번은 더미)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 이동을 구현
for cmd in moves:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    # 인덱스를 벗어나는 경우 무시
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    
    # 이동 후 인덱스
    x, y = nx, ny

    # 이동 이전 주사위 상태
    t = dice[:]

    # 각 움직임에 맞게 주사위를 갱신
    if cmd == 1: # 동
        dice[1], dice[3], dice[6], dice[4] = t[4], t[1], t[3], t[6]

    elif cmd == 2: # 서
        dice[1], dice[4], dice[6], dice[3] = t[3], t[1], t[4], t[6]

    elif cmd == 3: # 북
        dice[1], dice[2], dice[6], dice[5] = t[5], t[1], t[2], t[6]

    else: # 남
        dice[1], dice[5], dice[6], dice[2] = t[2], t[1], t[5], t[6]

    # 이동 후 0인 위치였다면 지도를 갱신    
    if table[x][y] == 0:
        table[x][y] = dice[6]
    
    # 0이 아닌 위치라면 주사위를 갱신
    else:
        dice[6] = table[x][y]
        table[x][y] = 0

    # 출력
    print(dice[1])
```