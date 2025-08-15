# [1063] 킹

### **난이도**
실버 3
## **📝문제**
8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

킹은 다음과 같이 움직일 수 있다.

- R : 한 칸 오른쪽으로
- L : 한 칸 왼쪽으로
- B : 한 칸 아래로
- T : 한 칸 위로
- RT : 오른쪽 위 대각선으로
- LT : 왼쪽 위 대각선으로
- RB : 오른쪽 아래 대각선으로
- LB : 왼쪽 아래 대각선으로

체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.

![이미지](https://upload.acmicpc.net/259549ad-b275-48a1-91f7-197a7ce72a23/-/preview/)

입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.
### **출력**
첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.
### **예제입출력**

**예제 입력1**

```
A1 A2 5
B
L
LB
RB
LT
```

**예제 출력1**

```
A1
A2
```

**예제 입력2**

```
A1 H8 1
T
```

**예제 출력2**

```
A2
H8
```

**예제 입력3**

```
A1 A2 1
T
```

**예제 출력3**

```
A2
A3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
king_pos, stone_pos, N = input().split()
N = int(N)

directions = {
    "R":  (0, 1),
    "L":  (0, -1),
    "B":  (-1, 0),
    "T":  (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

def pos_to_coord(pos):
    col = ord(pos[0]) - ord('A')  # 0~7
    row = int(pos[1]) - 1         # 0~7
    return (row, col)

def coord_to_pos(coord):
    row, col = coord
    return chr(col + ord('A')) + str(row + 1)

king = pos_to_coord(king_pos)
stone = pos_to_coord(stone_pos)

for _ in range(N):
    move = input().strip()
    dr, dc = directions[move]

    new_king = (king[0] + dr, king[1] + dc)

    if not (0 <= new_king[0] < 8 and 0 <= new_king[1] < 8):
        continue

    if new_king == stone:
        new_stone = (stone[0] + dr, stone[1] + dc)
        if not (0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8):
            continue
        stone = new_stone

    king = new_king

print(coord_to_pos(king))
print(coord_to_pos(stone))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|966
#### **📝해설**

**알고리즘**
```
1. 구현
```

#### **📝해설**

```python
# 킹 위치, 돌 위치, 명령 개수 입력
king_pos, stone_pos, N = input().split()
N = int(N)

# 방향 정의
directions = {
    "R":  (0, 1),
    "L":  (0, -1),
    "B":  (-1, 0),
    "T":  (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

# 체스 좌표 → 숫자 변환
def pos_to_coord(pos):
    col = ord(pos[0]) - ord('A')  # 0~7
    row = int(pos[1]) - 1         # 0~7
    return (row, col)

# 숫자 → 체스 좌표 변환
def coord_to_pos(coord):
    row, col = coord
    return chr(col + ord('A')) + str(row + 1)

# 현재 좌표로 변환
king = pos_to_coord(king_pos)
stone = pos_to_coord(stone_pos)

for _ in range(N):
    move = input().strip()
    dr, dc = directions[move]

    # 킹의 다음 위치
    new_king = (king[0] + dr, king[1] + dc)

    # 킹이 보드 안에 있는지 확인
    if not (0 <= new_king[0] < 8 and 0 <= new_king[1] < 8):
        continue

    # 돌과 부딪히면 돌도 이동
    if new_king == stone:
        new_stone = (stone[0] + dr, stone[1] + dc)
        # 돌이 보드 밖이면 이동 불가
        if not (0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8):
            continue
        stone = new_stone

    king = new_king

# 결과 출력
print(coord_to_pos(king))
print(coord_to_pos(stone))
```