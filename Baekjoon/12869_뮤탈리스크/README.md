# [12869] 뮤탈리스크

### **난이도**
골드 4
## **📝문제**
수빈이는 강호와 함께 스타크래프트 게임을 하고 있다. 수빈이는 뮤탈리스크 1개가 남아있고, 강호는 SCV N개가 남아있다.

각각의 SCV는 남아있는 체력이 주어져있으며, 뮤탈리스크를 공격할 수는 없다. 즉, 이 게임은 수빈이가 이겼다는 것이다.

뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.

1. 첫 번째로 공격받는 SCV는 체력 9를 잃는다.
2. 두 번째로 공격받는 SCV는 체력 3을 잃는다.
3. 세 번째로 공격받는 SCV는 체력 1을 잃는다.  
SCV의 체력이 0 또는 그 이하가 되어버리면, SCV는 그 즉시 파괴된다. 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.

남아있는 SCV의 체력이 주어졌을 때, 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 SCV의 수 N (1 ≤ N ≤ 3)이 주어진다. 둘째 줄에는 SCV N개의 체력이 주어진다. 체력은 60보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 모든 SCV를 파괴하기 위한 공격 횟수의 최솟값을 출력한다.

### **예제입출력**

**예제 입력1**

```
3
12 10 4
```

**예제 출력1**

```
2
```

**예제 입력2**

```
3
54 18 6
```

**예제 출력2**

```
6
```

**예제 입력3**

```
2
60 40
```

**예제 출력3**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

def min_attacks(hp):
    # 최대 체력 범위 설정
    MAX_HP = 60

    # 세 SCV의 초기 체력을 맞춰 0으로 확장
    while len(hp) < 3:
        hp.append(0)

    # dp 배열로 각 체력 상태에서의 최소 공격 횟수를 저장
    dp = [[[float('inf')] * (MAX_HP + 1) for _ in range(MAX_HP + 1)] for __ in range(MAX_HP + 1)]
    dp[hp[0]][hp[1]][hp[2]] = 0

    queue = deque([(hp[0], hp[1], hp[2])])

    while queue:
        a, b, c = queue.popleft()
        current_attacks = dp[a][b][c]

        # 가능한 공격 조합들
        attacks = [
            (9, 3, 1),
            (9, 1, 3),
            (3, 9, 1),
            (3, 1, 9),
            (1, 9, 3),
            (1, 3, 9)
        ]

        for da, db, dc in attacks:
            na, nb, nc = max(0, a - da), max(0, b - db), max(0, c - dc)
            if dp[na][nb][nc] > current_attacks + 1:
                dp[na][nb][nc] = current_attacks + 1
                queue.append((na, nb, nc))

    return dp[0][0][0]

# 입력
n = int(input())  # SCV의 수 (1 이상 3 이하)
hp = list(map(int, input().split()))  # 각 SCV의 초기 체력

# 결과 출력
print(min_attacks(hp))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116916|180|PyPy3|1197
#### **📝해설**

**알고리즘**
```
1. BFS
2. 다이나믹 프로그래밍
```

### **다른 풀이**

```python
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

scvs = list(map(int,input().split()))

scvs.sort()

attacks = [9,3,1]

ans = 21

visited = set()

def dfs(depth,lst):
    global ans
    if not lst:
        ans = min(ans,depth)
        return
    for attack in permutations(attacks[:len(lst)],len(lst)):
        temp = []
        for k in range(len(lst)):
            x = lst[k] - attack[k]
            if x>0:
                temp.append(x)
        temp.sort()
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            dfs(depth+1,temp)
            if not temp:
                visited.remove(tuple(temp))
        
dfs(0,scvs)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
howon1347|31120|44|Python3|711