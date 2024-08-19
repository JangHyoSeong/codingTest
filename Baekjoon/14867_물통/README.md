# [14867] 물통

### **난이도**
골드 2
## **📝문제**
용량이 다른 두 개의 빈 물통 A, B가 있다. 이 물통들에 물을 채우고 비우는 일을 반복하여 두 물통을 원하는 상태(목표하는 양의 물을 담은 상태)가 되도록 만들고자 한다. 물통 이외에는 물의 양을 정확히 잴 수 있는 방법이 없으며, 가능한 작업은 다음과 같은 세 종류가 전부이다.

- [F(x): Fill x]: 물통 x에 물을 가득 채운다. (물을 채우기 전에 물통 x가 비어있는지 여부는 관계없음. 다른 물통은 그대로 둠)
- [E(x): Empty x]: 물통 x의 물을 모두 버린다. (다른 물통은 그대로 둠)
- [M(x,y): Move water from x to y)]: 물통 x의 물을 물통 y에 붓는다. 이때 만약 물통 x에 남아 있는 물의 양이 물통 y에 남아 있는 빈 공간보다 적거나 같다면 물통 x의 물을 물통 y에 모두 붓는다. 만약 물통 x에 남아 있는 물의 양이 물통 y에 남아 있는 빈 공간보다 많다면 부을 수 있는 만큼 최대로 부어 물통 y를 꽉 채우고 나머지는 물통 x에 남긴다.  
예를 들어, 물통 A와 B의 용량이 각각 2리터와 5리터라고 하자. 두 물통 모두 빈 상태에서 시작하여 최종적으로 물통 A에는 2리터, 물통 B에는 4리터 물을 남기길 원할 경우, 다음과 같은 순서로 작업을 수행하면 총 8회의 작업으로 원하는 상태에 도달할 수 있다.

(0,0)→[F(B)]→(0,5)→[M(B,A)]→(2,3)→[E(A)]→(0,3)→[M(B,A)]→(2,1)→[E(A)]→(0,1)→[M(B,A)]→(1,0)→[F(B)]→(1,5)→[M(B,A)]→(2,4)

하지만, 작업 순서를 아래와 같이 한다면 필요한 작업 총 수가 5회가 된다.

(0,0)→[F(A)]→(2,0)→[M(A,B)]→(0,2)→[F(A)]→(2,2)→[M(A,B)]→(0,4)→[F(A)]→(2,4)

두 물통의 용량과 원하는 최종 상태를 입력으로 받은 후, 두 물통이 비어 있는 상태에서 시작하여 최종 상태에 도달하기 위한 최소 작업 수를 구하는 프로그램을 작성하시오.
### **입력**
표준 입력으로 물통 A의 용량을 나타내는 정수 a(1 ≤ a < 100,000), 물통 B의 용량을 나타내는 정수 b(a < b ≤ 100,000), 최종 상태에서 물통 A에 남겨야 하는 물의 용량을 나타내는 정수 c(0 ≤ c ≤ a), 최종 상태에서 물통 B에 남겨야 하는 물의 용량을 나타내는 정수 d(0 ≤ d ≤ b)가 공백으로 분리되어 한 줄에 주어진다.
### **출력**
목표 상태에 도달하는 최소 작업 수를 나타내는 정수를 표준 출력으로 출력한다. 만약 목표 상태에 도달하는 방법이 없다면 –1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 7 3 2
```

**예제 출력1**

```
9
```

**예제 입력2**

```
2 5 0 1
```

**예제 출력2**

```
5
```

**예제 입력3**

```
3 5 2 4
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

a, b, c, d = map(int, input().split())

q = deque()
q.append([0, 0, 0])

visited = {}
visited[(0, 0)] = True

while q:
    now_a, now_b, count = q.popleft()

    if now_a == c and now_b == d:
        print(count)
        break

    if now_a > 0 and now_b != b:
        temp_a = now_a
        temp_b = now_b

        if b - now_b <= now_a:
            temp_a -= (b-temp_b)
            temp_b = b
        else:
            temp_b += temp_a
            temp_a = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True

    if now_b > 0 and now_a != a:
        temp_a = now_a
        temp_b = now_b

        if a - now_a <= now_b:
            temp_b -= (a-temp_a)
            temp_a = a
        else:
            temp_a += temp_b
            temp_b = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True


    if now_a > 0:
        if visited.get((0, now_b)) is None:
            q.append([0, now_b, count+1])
            visited[(0, now_b)] = True
    
    if now_b > 0:
        if visited.get((now_a, 0)) is None:
            q.append([now_a, 0, count+1])
            visited[(now_a, 0)] = True

    if now_a < a:
        if visited.get((a, now_b)) is None:
            q.append([a, now_b, count+1])
            visited[(a, now_b)] = True

    if now_b < b:
        if visited.get((now_a, b)) is None:
            q.append([now_a, b, count+1])
            visited[(now_a, b)] = True
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|184868|404|PyPy3|1614
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **😅개선점**

1. 물을 옮겨담거나 채우는 행위를 리스트로 만들고 반복문으로 관리하면 코드가 더 깔끔할 것 같다

### **다른 풀이**

```python
from collections import deque

def transfer_water(from_amt, to_amt, to_max):
    # 물을 옮기고 남은 물의 양을 계산
    transfer_amt = min(from_amt, to_max - to_amt)
    return from_amt - transfer_amt, to_amt + transfer_amt

def find_minimum_operations(a, b, c, d):
    # BFS 큐 초기화: 현재 상태 (a의 물 양, b의 물 양, 작업 횟수)
    queue = deque([(0, 0, 0)])
    visited = {(0, 0): True}

    while queue:
        cur_a, cur_b, operations = queue.popleft()

        # 목표 상태에 도달한 경우 작업 횟수 반환
        if cur_a == c and cur_b == d:
            return operations

        # 가능한 모든 작업 생성
        next_states = [
            (a, cur_b),         # A 물통 가득 채우기
            (cur_a, b),         # B 물통 가득 채우기
            (0, cur_b),         # A 물통 비우기
            (cur_a, 0),         # B 물통 비우기
            transfer_water(cur_a, cur_b, b),  # A -> B 물 옮기기
            transfer_water(cur_b, cur_a, a)[::-1]  # B -> A 물 옮기기
        ]

        for next_a, next_b in next_states:
            if (next_a, next_b) not in visited:
                visited[(next_a, next_b)] = True
                queue.append((next_a, next_b, operations + 1))

    return -1  # 목표 상태에 도달할 수 없는 경우

# 입력 처리 및 결과 출력
a, b, c, d = map(int, input().split())
result = find_minimum_operations(a, b, c, d)
print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wkdgytmd200|92912|736|Python3|1468
#### **📝해설**

```python
from collections import deque

a, b, c, d = map(int, input().split())

q = deque()
q.append([0, 0, 0])

# 방문 여부를 딕셔너리로 검사
# 리스트로 검사할 경우 쓰지 않는 부분이 많아서 메모리 낭비
visited = {}
visited[(0, 0)] = True


# BFS 시작
while q:
    now_a, now_b, count = q.popleft()

    # 찾는 값에 도달했다면 종료
    if now_a == c and now_b == d:
        print(count)
        break

    # 물 A에서 B로 옮겨담기
    if now_a > 0 and now_b != b:
        temp_a = now_a
        temp_b = now_b

        if b - now_b <= now_a:
            temp_a -= (b-temp_b)
            temp_b = b
        else:
            temp_b += temp_a
            temp_a = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True

    # B에서 A로 옮겨담기
    if now_b > 0 and now_a != a:
        temp_a = now_a
        temp_b = now_b

        if a - now_a <= now_b:
            temp_b -= (a-temp_a)
            temp_a = a
        else:
            temp_a += temp_b
            temp_b = 0

        if visited.get((temp_a, temp_b)) is None:
            q.append([temp_a, temp_b, count+1])
            visited[(temp_a, temp_b)] = True


    # A 물 비우기
    if now_a > 0:
        if visited.get((0, now_b)) is None:
            q.append([0, now_b, count+1])
            visited[(0, now_b)] = True
    
    # B 물 비우기
    if now_b > 0:
        if visited.get((now_a, 0)) is None:
            q.append([now_a, 0, count+1])
            visited[(now_a, 0)] = True

    # A 물 채우기
    if now_a < a:
        if visited.get((a, now_b)) is None:
            q.append([a, now_b, count+1])
            visited[(a, now_b)] = True

    # B 물 채우기
    if now_b < b:
        if visited.get((now_a, b)) is None:
            q.append([now_a, b, count+1])
            visited[(now_a, b)] = True
else:
    print(-1)
```