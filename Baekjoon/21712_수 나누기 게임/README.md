# [21712] 수 나누기 게임

### **난이도**
골드 4
## **📝문제**
《보드게임컵》을 준비하다 지친 은하는 보드게임컵 참가자들을 경기장에 몰아넣고 결투를 시키는 게임 《수 나누기 게임》을 만들었습니다.

《수 나누기 게임》의 규칙은 다음과 같습니다.

게임을 시작하기 전 각 플레이어는 
$1$부터 
$1\,000\,000$ 사이의 수가 적힌 서로 다른 카드를 잘 섞은 뒤 한 장씩 나눠 가집니다.
매 턴마다 플레이어는 다른 플레이어와 한 번씩 결투를 합니다.
결투는 서로의 카드를 보여주는 방식으로 진행되며, 플레이어의 카드에 적힌 수로 다른 플레이어의 카드에 적힌 수를 나눴을 때, 나머지가 
$0$이면 승리합니다. 플레이어의 카드에 적힌 수가 다른 플레이어의 카드에 적힌 수로 나누어 떨어지면 패배합니다. 둘 다 아니라면 무승부입니다.
승리한 플레이어는 
$1$점을 획득하고, 패배한 플레이어는 
$1$점을 잃습니다. 무승부인 경우 점수의 변화가 없습니다.
본인을 제외한 다른 모든 플레이어와 정확히 한 번씩 결투를 하고 나면 게임이 종료됩니다.
《수 나누기 게임》의 결과를 가지고 한별이와 내기를 하던 은하는 게임이 종료되기 전에 모든 플레이어의 점수를 미리 알 수 있을지 궁금해졌습니다. 은하를 위해 각 플레이어가 가지고 있는 카드에 적힌 수가 주어졌을 때, 게임이 종료된 후의 모든 플레이어의 점수를 구해주세요.
### **입력**
첫 번째 줄에 플레이어의 수 
$N$이 주어집니다.

두 번째 줄에 첫 번째 플레이어부터 
$N$번째 플레이어까지 각 플레이어가 가지고 있는 카드에 적힌 정수 
$x_{1}$, 
$\cdots$, 
$x_{N}$이 공백으로 구분되어 주어집니다.
### **출력**
첫 번째 플레이어부터 
$N$번째 플레이어까지 게임이 종료됐을 때의 각 플레이어의 점수를 공백으로 구분하여 출력해주세요.
### **예제입출력**

**예제 입력1**

```
3
3 4 12
```

**예제 출력1**

```
1 1 -2
```

**예제 입력2**

```
4
7 23 8 6
```

**예제 출력2**

```
0 0 0 0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

MAX = 1000000

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

score = [0] * N
value_to_index = {x: i for i, x in enumerate(arr)}

for i in range(N):
    x = arr[i]
    mul = x * 2

    while mul <= MAX:
        if mul in value_to_index:
            j = value_to_index[mul]
            score[i] += 1
            score[j] -= 1
        mul += x

print(" ".join(map(str, score)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|139452|352|PyPy3|440
#### **📝해설**

**알고리즘**
```
1. 정수론
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

mx = max(P)
A = [0]*1000001
B = [0]*1000001

for v in P:
    A[v] = 1

for v in P:
    t = v*2
    while t <= mx:
        if A[t]:
            B[t] -= 1
            B[v] += 1
        t += v

print(" ".join([str(B[x]) for x in P]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rich1055|139020|188|PyPy3|323
#### **📝해설**

```python
import sys

MAX = 1000000

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

score = [0] * N
# 어떤 숫자가 어느 인덱스에 존재하는지 딕셔너리로 저장
value_to_index = {x: i for i, x in enumerate(arr)}

# 모든 숫자를 확인
for i in range(N):
    x = arr[i]

    # 그 숫자의 배수가 존재한다면, 그 점수를 낮추고 본인의 점수를 올림
    mul = x * 2

    # 최대값을 넘어가기 전까지 확인
    while mul <= MAX:

        # 배수가 딕셔너리에 존재한다면, 승부를 봄
        if mul in value_to_index:
            j = value_to_index[mul]
            score[i] += 1
            score[j] -= 1
        mul += x

print(" ".join(map(str, score)))
```