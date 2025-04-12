# [28325] 호숫가의 개미굴

### **난이도**
골드 5
## **📝문제**
KOI 호숫가에 여러 개미가 모여 사는 개미굴이 있다. 개미굴은 둥근 호수의 둘레를 따라 
$1$부터 
$N$까지의 번호가 붙은 
$N$개의 방이 차례대로 원형으로 배치되어 있으며, 모든 
$i$ (
$1 \le i \le N-1$)에 대해 
$i$번째 방과 
$i+1$번째 방이, 그리고 
$N$번째 방과 
$1$번째 방이 통로로 직접 연결되어 있는 형태였다.

하지만 여러 이유로 인해 각 방에서 몇 개의 쪽방이 갈라지기 시작해서, 현재는 모든 
$i$ (
$1 \le i \le N$)에 대해, 개미굴의 
$i$번째 방에 
$C_i$개의 쪽방이 통로로 직접 연결되어 있다. 
$i$번째 방과 연결된 쪽방은 
$i$번째 방 이외에 다른 방과 통로로 연결되어 있지 않다.

예를 들어 
$N = 7$이고, 
$C = [3,0,0,1,0,2,0]$인 개미굴은 아래 그림과 같은 형태이다.

[이미지](https://upload.acmicpc.net/bf045d97-0759-4480-9d77-6f369b75d711/-/preview/)

개미굴의 각 방과 쪽방에는 최대 한 마리의 개미가 살 수 있다. 만약 통로로 직접 연결되어 있는 두 곳(방 또는 쪽방) 모두에 개미가 살고 있다면, 두 개미는 서로 불편해한다. 이러한 불편함을 방지하기 위해, 현재 개미굴의 각 통로가 직접 연결하는 두 곳 중 최대 한 곳에만 개미가 살고 있다.

개미들은 똑똑하기 때문에, 이 조건을 만족하는 하에 최대한 많은 수의 개미들이 현재 개미굴에 살고 있다고 한다. 현재 개미굴의 구조가 주어질 때, 개미굴에 살고 있는 개미의 수를 구하는 프로그램을 작성하라.
### **입력**
첫 번째 줄에 정수 
$N$이 주어진다.

두 번째 줄에 각 방과 연결된 쪽방의 개수를 의미하는 
$N$개의 정수 
$C_1, C_2, \cdots, C_N$이 공백으로 구분되어 주어진다.
### **출력**
첫 번째 줄에 개미굴에 살고 있는 개미의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 0 1 0
```

**예제 출력1**

```
4
```

**예제 입력2**

```
4
1 1 1 1
```

**예제 출력2**

```
4
```

**예제 입력3**

```
2
0 0
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

room = set()
count = 0
memo = [-1] * N

for i in range(N):
    if arr[i]:
        room.add(i)
        count += arr[i]
        memo[i] = 0

if len(room) == 0:
    print(N // 2)
    exit()

if N == 2:
    if len(room) == 1:
        count += 1
    print(count)
    exit()

start = 0
for i in range(N):
    if i in room:
        start = i
        break

for i in range(start, start + N):
    idx = i % N
    if memo[idx] == -1:
        left = (idx - 1) % N
        right = (idx + 1) % N
        if memo[left] != 1 and memo[right] != 1:
            memo[idx] = 1
            count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|189697|192|PyPy3|689
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. DP
```

### **다른 풀이**

```python
n = int(input())
li = list(map(int, input().split()))
st = [0]
for x in li:
    if x == 0:
        st[-1] += 1
    elif st[-1]:
        st.append(0)
if len(st) > 1 and li[0] == 0 and li[-1] == 0:
    st[0] += st.pop()
ans = sum(li)
sm = ans
for x in st:
    if ans:
        ans += (x+1)//2
    else:
        ans += x//2
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jwdoctor08|61634|136|Python3|330
#### **📝해설**

```python
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 쪽방이 있는 인덱스
room = set()

# 총 개미의 숫자
count = 0

# 개미가 살고 있는지 여부(-1: 개미가 없는 방, 0: 쪽방 있는 방, 1: 개미가 있는 방)
memo = [-1] * N

# 방을 검사하면서 쪽방의 여부를 검사
for i in range(N):
    if arr[i]:
        room.add(i)

        # 쪽방이 있다면 무조건 그 방을 비우고 쪽방을 채우는게 이득
        count += arr[i]
        memo[i] = 0

# 쪽방이 없다면, 개미의 총 숫자는 방의 // 2
if len(room) == 0:
    print(N // 2)
    exit()

# N == 2인 경우, 따로 계산
if N == 2:
    if len(room) == 1:
        count += 1
    print(count)
    exit()

# 원형 구조이기 때문에 쪽방이 있는 방부터 시작해야 계산이 편리함
start = 0
for i in range(N):
    if i in room:
        start = i
        break

# 모든 방을 검사
for i in range(start, start + N):
    idx = i % N

    # 아직 방문하지 않았거나 개미가 없는 방이라면
    if memo[idx] == -1:

        # 오른쪽, 왼쪽 방을 검사해서 개미가 없다면 개미를 추가
        left = (idx - 1) % N
        right = (idx + 1) % N
        if memo[left] != 1 and memo[right] != 1:
            memo[idx] = 1
            count += 1

# 출력
print(count)
```