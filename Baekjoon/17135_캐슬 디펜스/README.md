# [17135] 캐슬 디펜스

### **난이도**
골드 3
## **📝문제**
캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.

성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. 

게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.

격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
### **입력**
첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
### **출력**
첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
```

**예제 출력1**

```
3
```

**예제 입력2**

```
5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
```

**예제 출력2**

```
3
```

**예제 입력3**

```
5 5 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
```

**예제 출력3**

```
5
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31692|476|Python3|1461
#### **📝해설**

**알고리즘**
```
1. 조합
2. 그래프 탐색
```

#### **📝해설**

```python
from itertools import combinations
import copy

def attack(archers, board, D):
    # 적의 위치 이동 후 공격하는 함수
    n, m = len(board), len(board[0])
    attacked = set()

    for archer in archers:
        targets = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    distance = abs(n - i) + abs(archer - j)
                    if distance <= D:
                        targets.append((distance, j, i))
        
        if targets:
            targets.sort()
            attacked.add((targets[0][2], targets[0][1]))

    return attacked

def move_enemies(board):
    # 적을 이동하는 함수
    n, m = len(board), len(board[0])
    new_board = [[0]*m for _ in range(n)]
    
    for i in range(n-1):
        new_board[i+1] = board[i]
    
    return new_board

def simulate(archers, original_board, D):
    # 전체 담당 함수
    board = copy.deepcopy(original_board)
    total_attacked = 0

    while any(1 in row for row in board):
        attacked = attack(archers, board, D)
        total_attacked += len(attacked)
        
        for i, j in attacked:
            board[i][j] = 0

        board = move_enemies(board)

    return total_attacked

def main():
    # 입력
    n, m, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    max_kills = 0
    for archers in combinations(range(m), 3):
        kills = simulate(archers, board, D)
        max_kills = max(max_kills, kills)

    print(max_kills)

if __name__ == "__main__":
    main()

```