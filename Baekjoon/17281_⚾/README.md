# [17281] ⚾

### **난이도**
골드 4
## **📝문제**
⚾는 9명으로 이루어진 두 팀이 공격과 수비를 번갈아 하는 게임이다. 하나의 이닝은 공격과 수비로 이루어져 있고, 총 N이닝 동안 게임을 진행해야 한다. 한 이닝에 3아웃이 발생하면 이닝이 종료되고, 두 팀이 공격과 수비를 서로 바꾼다.

두 팀은 경기가 시작하기 전까지 타순(타자가 타석에 서는 순서)을 정해야 하고, 경기 중에는 타순을 변경할 수 없다. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않은 상태면 이닝은 끝나지 않고, 1번 타자가 다시 타석에 선다. 타순은 이닝이 변경되어도 순서를 유지해야 한다. 예를 들어, 2이닝에 6번 타자가 마지막 타자였다면, 3이닝은 7번 타자부터 타석에 선다.

공격은 투수가 던진 공을 타석에 있는 타자가 치는 것이다. 공격 팀의 선수가 1루, 2루, 3루를 거쳐서 홈에 도착하면 1점을 득점한다. 타자가 홈에 도착하지 못하고 1루, 2루, 3루 중 하나에 머물러있을 수 있다. 루에 있는 선수를 주자라고 한다. 이닝이 시작될 때는 주자는 없다.

타자가 공을 쳐서 얻을 수 있는 결과는 안타, 2루타, 3루타, 홈런, 아웃 중 하나이다. 각각이 발생했을 때, 벌어지는 일은 다음과 같다.

- 안타: 타자와 모든 주자가 한 루씩 진루한다.
- 2루타: 타자와 모든 주자가 두 루씩 진루한다.
- 3루타: 타자와 모든 주자가 세 루씩 진루한다.
- 홈런: 타자와 모든 주자가 홈까지 진루한다.
- 아웃: 모든 주자는 진루하지 못하고, 공격 팀에 아웃이 하나 증가한다.  
한 야구팀의 감독 아인타는 타순을 정하려고 한다. 아인타 팀의 선수는 총 9명이 있고, 1번부터 9번까지 번호가 매겨져 있다. 아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다. 이제 다른 선수의 타순을 모두 결정해야 한다. 아인타는 각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있다. 가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.
### **입력**
첫째 줄에 이닝 수 N(2 ≤ N ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에는 각 선수가 각 이닝에서 얻는 결과가 1번 이닝부터 N번 이닝까지 순서대로 주어진다. 이닝에서 얻는 결과는 9개의 정수가 공백으로 구분되어져 있다. 각 결과가 의미하는 정수는 다음과 같다.

- 안타: 1
- 2루타: 2
- 3루타: 3
- 홈런: 4
- 아웃: 0  
각 이닝에는 아웃을 기록하는 타자가 적어도 한 명 존재한다.
### **출력**
아인타팀이 얻을 수 있는 최대 점수를 출력한다.
### **예제입출력**

**예제 입력1**

```
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0
```

**예제 출력1**

```
1
```

**예제 입력2**

```
2
4 0 0 0 1 1 1 0 0
0 0 0 0 0 0 0 0 0
```

**예제 출력2**

```
4
```

**예제 입력3**

```
2
0 4 4 4 4 4 4 4 4
0 4 4 4 4 4 4 4 4
```

**예제 출력3**

```
43
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import permutations

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

others = [i for i in range(1, 9)]

for order in permutations(others):
    batting_order = list(order[:3]) + [0] + list(order[3:])
    score = 0
    batter_idx = 0

    for inning in innings:
        out_count = 0
        base = [0, 0, 0]

        while out_count < 3:
            player = batting_order[batter_idx]
            result = inning[player]

            if result == 0:
                out_count += 1
            elif result == 1:
                score += base[2]
                base = [1] + base[:2]
            elif result == 2:
                score += base[2] + base[1]
                base = [0, 1, base[0]]
            elif result == 3:
                score += base[2] + base[1] + base[0]
                base = [0, 0, 1]
            elif result == 4:
                score += base[0] + base[1] + base[2] + 1
                base = [0, 0, 0]

            batter_idx = (batter_idx + 1) % 9

    max_score = max(max_score, score)

print(max_score)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110964|956|PyPy3|1094
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
#ref: https://www.acmicpc.net/source/57009296 -> 속도 빨라지는지 확인

from itertools import permutations
num = int(input())
rounds = []
for _ in range(num):
    rounds.append(list(map(int, input().split())))

max_inning_score = [0]*num
for inning, h in enumerate(rounds):
    h_sorted = list(sorted(h))

    zeros = 0
    while zeros < 9 and h_sorted[0] == 0:
        h_sorted.append(h_sorted.pop(0))
        zeros += 1

    score = 0
    hitter = 0
    first, second, third = 0, 0, 0
    out = 0
    while out < 3:
        step = h_sorted[hitter]
        if step == 0:
            out += 1
        elif step == 1:
            score += first
            first, second, third = second, third, 1
        elif step == 2:
            score += first + second
            first, second, third = third, 1, 0
        elif step == 3:
            score += first + second + third
            first, second, third = 1, 0, 0
        else:
            score += first + second + third + 1
            first, second, third = 0, 0, 0
        hitter = (hitter + 1) % 9
    max_inning_score[inning] = score

#get max score possible for the remaining innings
max_score_possible = [0]*num
max_score_accumulated = 0
for i in range(num-1, -1, -1):
    max_score_accumulated += max_inning_score[i]
    max_score_possible[i] = max_score_accumulated


max = 0
for p in permutations(range(1, 9)):
    p = list(p)
    global order
    order = p[:3] + [0] + p[3:]
    score = 0
    hitter = 0
    for inning, round in enumerate(rounds):
        if score + max_score_possible[inning] <= max:
            break
        first, second, third = 0, 0, 0
        out = 0
        while out < 3:
            step = round[order[hitter]]
            if step == 0:
                out += 1
            elif step == 1:
                score += first
                first, second, third = second, third, 1
            elif step == 2:
                score += first + second
                first, second, third = third, 1, 0
            elif step == 3:
                score += first + second + third
                first, second, third = 1, 0, 0
            else:
                score += first + second + third + 1
                first, second, third = 0, 0, 0
            hitter = (hitter + 1) % 9
    if score > max:
        max = score
print(max)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
heoragi53|115356|552|PyPy3|2321
#### **📝해설**

```python
from itertools import permutations

# 입력받기
N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

# 최대점수
max_score = 0

# 1번 타자(0번 인덱스)는 4번 타석 고정이고, 나머지의 인덱스
others = [i for i in range(1, 9)]

# 가능한 모든 경우를 순열로 생성
for order in permutations(others):

    # 1번 타자를 4번 타석에 포함
    batting_order = list(order[:3]) + [0] + list(order[3:])

    # 이번 조합에서의 점수
    score = 0

    # 타석에 설 타자의 인덱스
    batter_idx = 0

    # 이닝들을 모두 검사
    for inning in innings:

        # 아웃 갯수
        out_count = 0

        # 베이스 상태
        base = [0, 0, 0]

        # 아웃이 3번 되기 전까지 현재 이닝을 수행
        while out_count < 3:

            # 현재 타자의 인덱스
            player = batting_order[batter_idx]

            # 타자가 이번 이닝에서 칠 결과
            result = inning[player]

            # 아웃
            if result == 0:
                out_count += 1

            # 1루타
            elif result == 1:
                score += base[2]
                base = [1] + base[:2]
            
            # 2루타
            elif result == 2:
                score += base[2] + base[1]
                base = [0, 1, base[0]]

            # 3루타
            elif result == 3:
                score += base[2] + base[1] + base[0]
                base = [0, 0, 1]
            
            # 4루타
            elif result == 4:
                score += base[0] + base[1] + base[2] + 1
                base = [0, 0, 0]

            # 다음 타자로 넘어감
            batter_idx = (batter_idx + 1) % 9
    # 최대 점수 갱신
    max_score = max(max_score, score)

print(max_score)
```