# [14889] 스타트와 링크

### **난이도**
실버 1
## **📝문제**
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

```
i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
```
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S12 + S21 = 1 + 4 = 5
- 링크 팀: S34 + S43 = 2 + 5 = 7

1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
### **입력**
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
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

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

team = list(combinations(range(N), N//2))

team_len = len(team)

min_gap = 200 * N

for i in range(team_len // 2):
    temp_gap = 0
    team1_sum = 0
    team2_sum = 0
    for member1 in team[i]:
        for member2 in team[i]:
            team1_sum += table[member1][member2]

    for member1 in team[team_len -1 -i]:
        for member2 in team[team_len -1 -i]:
            team2_sum += table[member1][member2]

    temp_gap = abs(team2_sum - team1_sum)
    min_gap = min(min_gap, temp_gap)

print(min_gap)

    
    
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|137228|392|PyPy3|633
#### **📝해설**

**알고리즘**
```
1. 브루트포스
```

### **다른 풀이**

```python
import sys
def d_find(remain,start,total):
    global member_arr, N
    if remain == 0:
        if total > 0:
            total = -total
        global d_max
        if d_max < total:
            d_max = total
        return
    for i in range(start,N-remain):
        d_find(remain-1,i+1,total+member_arr[i])
input = sys.stdin.readline
N = int(input())
member_arr = list(map(int,input().split()))
member_arr[0] = sum(member_arr)
for i in range(1,N):
    line_arr = tuple(map(int,input().split()))
    for j in range(N):
        member_arr[j] = member_arr[j] + line_arr[j]
    member_arr[i] = member_arr[i] + sum(line_arr)
member_arr = tuple(sorted(member_arr,reverse = True))
total = -sum(member_arr)//2
d_max = total
d_find(N//2,0,total)
print(-d_max)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
cherish|31120|84|Python3|753
#### **📝해설**

```python
from itertools import combinations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 가능한 모든 조합을 리스트로 생성
team = list(combinations(range(N), N//2))

# 가능한 모든 조합 경우의 수의 개수를 저장
team_len = len(team)

# 최소값으로 사용할 변수
min_gap = 200 * N

# 조합은 절반을 기준으로 대칭. 따라서 절반까지 순회
for i in range(team_len // 2):
    
    # 이번 경우의수에서의 두 팀의 차이, 각 팀의 점수 합계
    temp_gap = 0
    team1_sum = 0
    team2_sum = 0

    # 팀의 점수를 구함
    for member1 in team[i]:
        for member2 in team[i]:
            team1_sum += table[member1][member2]

    # 상대팀의 점수를 구함
    for member1 in team[team_len -1 -i]:
        for member2 in team[team_len -1 -i]:
            team2_sum += table[member1][member2]

    # 최저 차이를 갱신
    temp_gap = abs(team2_sum - team1_sum)
    min_gap = min(min_gap, temp_gap)

print(min_gap)
```