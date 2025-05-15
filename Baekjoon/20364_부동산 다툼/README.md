# [20364] 부동산 다툼

### **난이도**
실버 1
## **📝문제**
이진 트리 모양의 땅으로 이루어진 꽉꽉마을에는 오리들이 살고 있다. 땅 번호는 다음과 같이 매겨진다.

루트 땅의 번호는 1이다.
어떤 땅의 번호가 K라면, 왼쪽 자식 땅의 번호는 2 × K, 오른쪽 자식 땅의 번호는 2 × K + 1이다.
어느날 오리들끼리 부동산 다툼이 일어나서 꽉꽉마을 촌장 경완이가 해결책을 가져왔고, 그 내용은 다음과 같다.

1. 오리들을 한 줄로 대기시킨다. 맨 처음 오리들은 1번 땅에 위치해 있다.
2. 오리들이 서있는 순서대로 원하는 땅을 가지도록 한다.

[이미지](https://upload.acmicpc.net/1916169a-8540-4a0d-a7c9-889d6afe2842/-/preview/)

만약, 한 오리가 원하는 땅까지 가는 길에 이미 다른 오리가 점유한 땅이 있다면 막대한 세금을 내야 하는 이유로 해당 땅을 지나가지 못해 그 오리는 땅을 가지지 못한다. 오리가 원하는 땅까지 가는 길에는 오리가 원하는 땅도 포함된다.

경완이의 해결책대로 땅 분배를 했을 때 각 오리별로 원하는 땅을 가질 수 있는지, 가질 수 없다면 처음 마주치는 점유된 땅의 번호를 구해보자.
### **입력**
첫 번째 줄에 땅 개수 N과 꽉꽉나라에 사는 오리 수 Q가 공백으로 구분되어 주어진다. (2 ≤ N < 220, 1 ≤ Q ≤ 200,000)

두 번째 줄부터 차례로 Q개의 줄에 걸쳐 i+1번째 줄에는 i번째 오리가 원하는 땅 번호 xi가 주어진다. (2 ≤ xi ≤ N)
### **출력**
Q개의 줄에 원하는 땅에 갈 수 있다면 0을, 갈 수 없다면 처음 마주치는 점유된 땅의 번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
6 4
3
5
6
2
```

**예제 출력1**

```
0
0
3
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())
ducks = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

tree = set()
result = []

for duck in ducks:
    path = []
    now = duck

    while now >= 1:
        path.append(now)
        now //= 2
    
    blocked = 0
    for land in reversed(path):
        if land in tree:
            blocked = land
            break
    
    print(blocked)
    if blocked == 0:
        tree.add(duck)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|135260|264|PyPy3|459
#### **📝해설**

**알고리즘**
```
1. 트리
```

### **다른 풀이**

```python
import sys
from math import log2
input = sys.stdin.readline

def btot(n): # bottom to top
    leaf = n
    ret = 0
    while True:
        if leaf == 0: break
        else: 
            if Tree[leaf]: ret = leaf
            leaf //= 2
    return ret
    
N, Q = map(int, input().split())
order = []
for _ in range(Q): order.append(int(input()))

H = int(log2(N)) + 1 if 2 ** int(log2(N)) != N else int(log2(N))
Tree = [0 for _ in range(2**H+1)]

for ele in order:
    print(btot(ele))
    Tree[ele] = 1
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iioo233|127292|220|PyPy3|502
#### **📝해설**

```python
import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())
ducks = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

# 오리가 점유중인 땅을 set로 저장
tree = set()
# 결과 출력을 위한 리스트
result = []

# 모든 오리들을 검사하면서
for duck in ducks:

    # 오리가 트리를 따라 내려오는 경로를 저장
    path = []
    # 오리가 내려올 경로를 역순으로 검사
    now = duck

    # 트리의 root까지 경로를 추가함
    while now >= 1:
        path.append(now)
        now //= 2
    
    # 오리가 이동하다 막히는 구간을 저장할 변수
    blocked = 0

    # 트리의 root부터 검사
    for land in reversed(path):
        # 이미 점유된 땅을 지난다면
        if land in tree:
            # 그때 인덱스를 저장
            blocked = land
            break
    
    print(blocked)
    # 자신의 땅에 잘도착했다면, 점유중인 땅을 추가
    if blocked == 0:
        tree.add(duck)
```