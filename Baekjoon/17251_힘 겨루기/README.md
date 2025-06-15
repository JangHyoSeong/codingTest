# [17251] 힘 겨루기

### **난이도**
실버 1
## **📝문제**
과거 격투가로 명성을 떨치던 힘스트롱씨는 "힘 겨루기"라는 대회를 주최하여 전국에 홍보를 하였다. 모집 공고를 보고 전국 각지에서 많은 사람들이 모였는 데, 모집 공고에 '힘'이란 것에 대해 정의하지 않아 혼란이 생긴 것이다.

헬스장에서 3대 500치는 근육질 아저씨부터, 유명 RPG 게임의 힘(STR) 스탯이 높은 사람까지 여러 종류의 힘을 두고 모인 것이다.
힘스트롱씨는 문득 "아는 것이 힘이다"라는 유명 격언이 떠올랐다. 예선전에서 상식 퀴즈를 통해 참가자들의 힘을 수치화하였고, 이 수치를 통해 본선 참가자를 선정하기로 하였다.

그렇게 총 N명의 참가자가 본선에 진출하였다. 하지만 예상과 달리, 본선은 홍팀과 청팀 두 팀으로 나누어 승부를 겨루는 팀전으로 진행되었다.

N명의 참가자들이 일렬로 나란히 서 있다. 힘스트롱씨는 1부터 N−1까지의 수가 적힌 공이 들어있는 추첨 상자에서 무작위로 하나를 뽑아 기준선을 선정할 예정이다. 예를 들어, 3번이 적힌 공을 뽑으면 3번과 4번 참가자 사이가 기준선이 된다. 기준선보다 왼쪽은 홍팀, 기준선보다 오른쪽은 청팀이다.

경기는 단판으로 진행된다. 각 팀에서 가장 센 사람이 나온 후, 두 사람이 힘을 겨룬다. 힘이 더 센 사람이 이기고 게임은 종료된다. 힘의 세기가 같으면 이기는 사람은 없다.

도박사 김씨(이하 김도박사)는 경기가 시작되기 전에 참가자 명단을 입수했다! 기준선의 위치에 따라 어느 팀이 이길 지 미리 알 수 있게 된 김도박사는 이길 확률이 더 높은 쪽에 전재산을 걸 예정이다. 김도박사는 어느 팀에 전재산을 걸어야할까?

기준선은 선수와 선수 사이에만 위치할 수 있으며, 팀에는 반드시 1명 이상 있어야 한다.
### **입력**
첫째 줄에 사람의 수 N이 주어진다. N은 1,000,000보다 작거나 같은 짝수이다.

둘째 줄에 1번 사람부터 N번 사람까지의 힘을 나타내는 정수가 주어진다. 각 사람의 힘은 10,000보다 작거나 같은 자연수이다.
### **출력**
김도박사가 홍팀에 걸어야 하는 경우에는 R, 청팀에 걸어야 하는 경우에는 B를 출력한다. 두 팀의 이길 확률이 같은 경우에는 X를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
9 15 18 7 13 11
```

**예제 출력1**

```
R
```

**예제 입력2**

```
10
26 25 9 27 7 30 15 20 8 16
```

**예제 출력2**

```
B
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_max = [0] * N
prefix_max[N-1] = arr[N-1]

for i in range(N-2, -1, -1):
    prefix_max[i] = max(prefix_max[i+1], arr[i])

left_max, right_max = 0, prefix_max[0]
left_win, right_win = 0, 0

for i in range(N-1):
    left_max = max(left_max, arr[i])
    right_max = prefix_max[i+1]    

    if left_max > right_max:
        left_win += 1
    
    elif left_max < right_max:
        right_win += 1


if left_win > right_win:
    print("R")

elif left_win < right_win:
    print("B")

else:
    print("X")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|221428|324|PyPy3|618
#### **📝해설**

**알고리즘**
```
1. 에드 혹
```

### **다른 풀이**

```python
from sys import *
n = int(stdin.readline().rstrip())
p  = list(map(int,stdin.readline().rstrip().split()))
k = 0
mx = 0
l, r = 0,0
for i in range(n):
    if(p[i]>mx):
        mx = p[i]
        l,r = i,i
    else:
        if(p[i]==mx):
            r = i
flag = (n-1-r)-(l)
if(flag>0):
    print('R')
elif(flag==0):
    print('X')
else:
    print('B')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
blackkarn|216576|276|PyPy3|349
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 오른쪽에서부터 시작해서, 그 인덱스까지의 최대값을 저장하는 리스트
prefix_max = [0] * N

# 시작지점 초기화
prefix_max[N-1] = arr[N-1]

# 거꾸로 순회하면서, 그 인덱스까지의 최대값을 저장해둠
for i in range(N-2, -1, -1):
    prefix_max[i] = max(prefix_max[i+1], arr[i])

# 각 지점을 기준으로 할 때, 그때까지의 최대값
left_max, right_max = 0, prefix_max[0]

# 왼쪽, 오른쪽의 승리 횟수
left_win, right_win = 0, 0

# 1 : 2~N ----- 1~N-1 : N 까지 승부를 보기 위해 반복
for i in range(N-1):

    # 레드팀의 최대값
    left_max = max(left_max, arr[i])

    # 블루팀의 최대값
    right_max = prefix_max[i+1]    

    # 비교 후 승리 횟수를 더함
    if left_max > right_max:
        left_win += 1
    
    elif left_max < right_max:
        right_win += 1

# 출력
if left_win > right_win:
    print("R")

elif left_win < right_win:
    print("B")

else:
    print("X")
```