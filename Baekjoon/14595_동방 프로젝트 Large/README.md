# [14595] 동방 프로젝트 (Large)

### **난이도**
골드 4
## **📝문제**
동아리방이 가지고 싶었던 병찬이는 LINK 사업단에 문의하여 N개의 방 중의 하나를 얻을 기회를 얻었다. 일자로 되어있는 건물에 N개의 방은 일직선상에 존재하며, 각 방에는 번호가 매겨져 있다. 맨 왼쪽 방의 번호는 1번이며, 순서대로 증가하여 맨 오른쪽 방의 번호가 N번이다. 각 방 사이에는 방을 구분하는 벽이 존재한다.

물론 병찬이 외에도 많은 사람이 동아리방을 원한다. 다행히 방은 충분했기에 병찬이는 안심하고 있었지만…

그때였다.

빅-종빈빌런이 나타나 건물 벽을 허물기 시작한 것이다! 빅-종빈빌런은 다음과 같은 규칙으로 벽을 무너뜨린다.

- x < y 를 만족하는 두 방에 대해서 x번 방부터 y번 방 사이에 있는 모든 벽을 허문다.
- 두 방 사이의 벽이 허물어지면 두 방은 하나의 방으로 합쳐진다.
- 이미 허물어진 벽이 존재한다면 무시하고 다음 벽을 허문다.
- 빅-종빈빌런은 건물이 무너지는 걸 원치 않기 때문에, 1번 방의 왼쪽 벽과 N번 방의 오른쪽 벽(즉, 바깥과 연결된 벽)은 허물지 않는다.  
동아리 방의 개수가 점점 줄어들자 병찬이는 초조해졌다. 이에 병찬이는 동아리방을 얻을 수 있는지에 대한 확률을 계산하기 위해 남는 동아리방의 수를 구하고 싶어 한다. 병찬이를 위해 빅-종빈빌런의 행동 횟수 M과 동방의 개수 N이 주어졌을 때, 남은 동아리방의 수를 구해주자.
### **입력**
첫 번째 줄에는 동아리방의 개수를 나타내는 양의 정수 N(2 ≤ N ≤ 1,000,000) 이 주어진다. 두 번째 줄에는 빅-종빈빌런의 행동 횟수를 나타내는 음이 아닌 정수 M(0 ≤ M ≤ 5,000) 이 주어진다. 세 번째 줄부터 M개의 줄에 걸쳐 빅-종빈빌런의 행동이 양의 정수 x, y(1 ≤ x < y ≤ N) 로 주어진다. 여기서 행동이란 x번 방부터 y번 방 사이의 벽을 무너뜨리는 것을 의미한다.

빅-종빈빌런은 매우 허당이기 때문에 동일한 행동을 여러 번 할 수 있음에 유의하라.
### **출력**
빅-종빈빌런의 모든 행동이 끝난 후 남아있는 동방의 개수를 한 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
5
2
1 2
2 4
```

**예제 출력1**

```
2
```

**예제 입력2**

```
5
1
1 5
```

**예제 출력2**

```
1
```

**예제 입력3**

```
10
3
1 3
2 4
5 8
```

**예제 출력3**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

N = int(input())
M = int(input())

if M == 0:
    print(N)
    exit()

parent = list(range(N + 1))
check = [0] * (N + 1)
sections = [tuple(map(int, input().split())) for _ in range(M)]
sections.sort()

right = 0
for a, b in sections:
    if a < right:
        a = right

    num = find(parent, a)
    for j in range(a, b + 1):
        parent[j] = num
    right = b

cnt = 0
for i in range(1, N + 1):
    root = find(parent, i)
    if check[root] == 0:
        cnt += 1
        check[root] = 1

print(cnt)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|127212|760|PyPy3|614
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

### **다른 풀이**

```python
def cnt_room():
    from sys import stdin
    
    new_input = stdin.readline
    N = int(new_input())
    M = int(new_input())
    
    if M == 0:
        return N
    
    orders = [tuple(map(int, new_input().split())) for _ in range(M)]
    orders.sort()
    start, end = orders[0]
    cnt = start
    for i in range(1, M):
        x, y = orders[i]
        if x > end:
            cnt += x - end
            start, end = x, y
        elif y > end:
            end = y

    return cnt + N - end
        
print(cnt_room())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pubhan35|31120|36|Python3|523
#### **📝해설**

```python
# 부모 노드 검색
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 입력
N = int(input())
M = int(input())

if M == 0:
    print(N)
    exit()

# 부모 노드의 정보를 저장할 리스트
parent = list(range(N + 1))

# 이미 벽을 허물었는지 검사
check = [0] * (N + 1)

# 입력받기
sections = [tuple(map(int, input().split())) for _ in range(M)]
sections.sort()

# 이미 검사한 방은 고려하지 않기 위해 변수 선언
right = 0
for a, b in sections:

    # 검사한 방 저장해둠
    if a < right:
        a = right

    # 부모를 찾고 합침
    num = find(parent, a)
    for j in range(a, b + 1):
        parent[j] = num
    right = b

# 방 개수 세기
cnt = 0
for i in range(1, N + 1):
    root = find(parent, i)
    if check[root] == 0:
        cnt += 1
        check[root] = 1

print(cnt)
```