# [15661] 링크와 스타트

### **난이도**
골드 5
## **📝문제**
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이다. 이제 스타트 팀과 링크 팀으로 사람들을 나눠야 한다. 두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
### **입력**
첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
### **출력**
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
```

**예제 출력1**

```
0
```

**예제 입력2**

```
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
```

**예제 출력2**

```
2
```

**예제 입력3**

```
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

def team_sum(team):
    ability = 0
    for i in team:
        for j in team:
            if i != j:
                ability += table[i][j]
    
    return ability

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

min_diff = int(21e8)
people = list(range(N))

for r in range(1, N // 2 + 1):
    for team in combinations(people, r):
        another_team = [p for p in people if p not in team]

        a_team = team_sum(team)
        b_team = team_sum(another_team)
        diff = abs(a_team - b_team)

        min_diff = min(min_diff, diff)
        if min_diff == 0:
            break

print(min_diff)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111600|1108|PyPy3|666
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```
### **다른 풀이**

```python
#   https://boj.kr/15661
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]
row, col = [sum(i) for i in S], [sum(i) for i in zip(*S)]
stat = [i + j for i, j in zip(row, col)]
sumStat = sum(row)

ans = float('inf')
for r in range(N//2, 0, -1):
    for combi in combinations(stat, r):
        ans = min(ans, abs(sumStat - sum(combi)))
        if ans == 0:
            break
    if ans == 0:
        break

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dohyahn|31120|152|Python3|512
#### **📝해설**

```python
from itertools import combinations

# 팀 멤버가 주어졌을때 능력치의 합을 구하는 함수
def team_sum(team):
    ability = 0
    for i in team:
        for j in team:
            if i != j:
                ability += table[i][j]
    
    return ability

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 능력치 차이의 최소값
min_diff = int(21e8)

# combinations 사용을 위해 각 사람의 인덱스를 저장할 리스트
people = list(range(N))


# 1 ~ N//2명을 포함하는 조합을 생성하기 위해 반복
for r in range(1, N // 2 + 1):

    # r명을 포함하는 조합을 생성
    for team in combinations(people, r):

        # 나머지 팀
        another_team = [p for p in people if p not in team]

        # 각 팀의 능력치를 구함
        a_team = team_sum(team)
        b_team = team_sum(another_team)
        diff = abs(a_team - b_team)

        # 최소값 갱신
        min_diff = min(min_diff, diff)
        if min_diff == 0:
            break

print(min_diff)
```