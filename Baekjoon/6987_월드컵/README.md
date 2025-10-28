# [6987] 월드컵

### **난이도**
골드 4
## **📝문제**
월드컵 조별 최종 예선에서는 6개국으로 구성된 각 조별로 동일한 조에 소속된 국가들과 한 번씩, 각 국가별로 총 5번의 경기를 치른다. 조별리그가 끝난 후, 기자가 보내온 각 나라의 승, 무승부, 패의 수가 가능한 결과인지를 판별하려고 한다. 다음은 가능한 결과와 가능하지 않은 결과의 예이다.

나라	승	무	패
A	5	0	0
B	3	0	2
C	2	0	3
D	0	0	5
E	4	0	1
F	1	0	4
나라	승	무	패
A	4	1	0
B	3	0	2
C	4	1	0
D	1	1	3
E	0	0	5
F	1	1	3
나라	승	무	패
A	5	0	0
B	4	0	1
C	2	2	1
D	2	0	3
E	1	0	4
F	0	0	5
나라	승	무	패
A	5	0	0
B	3	1	1
C	2	1	1
D	2	0	3
E	0	0	5
F	1	0	4
예제 1 가능한 결과	예제 2 가능한 결과	예제 3 불가능한 결과	예제 4 불가능한 결과
네 가지의 결과가 주어질 때 각각의 결과에 대하여 가능하면 1, 불가능하면 0을 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄부터 넷째 줄까지 각 줄마다 6개국의 결과가 나라별로 승, 무승부, 패의 순서로 빈칸을 하나 사이에 두고 18개의 숫자로 주어진다. 승, 무, 패의 수는 6보다 작거나 같은 자연수 또는 0이다.
### **출력**
입력에서 주어진 네 가지 결과에 대하여 가능한 결과는 1, 불가능한 결과는 0을 빈칸을 하나 사이에 두고 출력한다.
### **예제입출력**

**예제 입력1**

```
5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
```

**예제 출력1**

```
1 1 0 0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
answer = []
matches = []
for i in range(6):
    for j in range(i+1, 6):
        matches.append((i, j))

def dfs(idx):
    global possible

    if possible:
        return
    
    if idx == 15:
        for team in result:
            if any(x != 0 for x in team):
                return
        
        possible = True
        return
    
    a, b = matches[idx]

    # a 승, b 패
    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        dfs(idx + 1)
        result[a][0] += 1
        result[b][2] += 1

    # a 무, b 무
    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        dfs(idx + 1)
        result[a][1] += 1
        result[b][1] += 1

    # a 패, b 승
    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        dfs(idx + 1)
        result[a][2] += 1
        result[b][0] += 1

for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i*3 : (i+1)*3] for i in range(6)]

    possible = False

    if sum(sum(team) for team in result) != 30:
        answer.append(0)
    else:
        dfs(0)
        answer.append(1 if possible else 0)
    
print(*answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32544|32|Python3|1237
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
from sys import stdin
from itertools import combinations as cb


def solution(round):
    global ans
    if round == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3:
                ans = 0
                break
        return

    t1, t2 = game[round]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            solution(round + 1)
            res[t1][x] += 1
            res[t2][y] += 1


answer = []
game = list(cb(range(6), 2))
# 백트래킹
for _ in range(4):
    data = list(map(int, stdin.readline().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)]
    ans = 0
    solution(0)
    answer.append(ans)

print(*answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kikiru328|31120|32|Python3|760
#### **📝해설**

```python
# 정답 결과를 담을 리스트
answer = []

# 현재 어느 팀이 승부를 보는지 확인하기 위한 리스트
matches = []
for i in range(6):
    for j in range(i+1, 6):
        matches.append((i, j))

# DFS와 백트래킹을 통해 가능한 결과인지 확인
def dfs(idx):
    global possible

    # 가능하다면 종료
    if possible:
        return
    
    # 마지막까지 확인했을 때
    if idx == 15:
        # 모든 결과를 확인해서 불가능하다면 종료
        for team in result:
            if any(x != 0 for x in team):
                return
        
        # 가능한 경우 possible을 True로 설정 후 종료
        possible = True
        return
    
    # 현재 승부를 볼 팀 두개
    a, b = matches[idx]

    # a 승, b 패
    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        dfs(idx + 1)
        result[a][0] += 1
        result[b][2] += 1

    # a 무, b 무
    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        dfs(idx + 1)
        result[a][1] += 1
        result[b][1] += 1

    # a 패, b 승
    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        dfs(idx + 1)
        result[a][2] += 1
        result[b][0] += 1

# 4번 확인
for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i*3 : (i+1)*3] for i in range(6)]

    possible = False

    # 승패 합이 30이 안되는 경우 처음부터 불가능
    if sum(sum(team) for team in result) != 30:
        answer.append(0)
    
    # DFS를 통해 확인
    else:
        dfs(0)
        answer.append(1 if possible else 0)
    
print(*answer)
```