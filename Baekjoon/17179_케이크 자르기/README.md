# [17179] 케이크 자르기

### **난이도**
골드 4
## **📝문제**
생일을 맞이한 주성이가 생일 파티를 준비하려고 한다. 주성이는 일반 케이크 대신 평소 좋아하던 롤 케이크를 준비했다. 롤 케이크에는 장식이 존재해서 특정 위치에서만 자를 수 있다. 주성이는 롤 케이크 조각을 파티에 올 친구의 수 만큼 준비하고 싶어서, 가장 작은 조각의 크기를 미리 알아보기로 했다. 하지만 짓궂은 주성이의 친구들은 생일파티에 몇 명이 참석하는지 직접적으로 알려주지를 않는다. 그래서 몇 개의 수를 목록에 적어, 각 수만큼 조각을 만들었을 때 가장 작은 조각의 길이의 최댓값을 구하려고 한다.

예를 들어 70cm의 롤 케이크에 자를 수 있는 지점이 5군데(10cm, 20cm, 35cm, 55cm, 60cm)가 있다고 하자. 만약 목록에 적힌 수 중 하나가 3이라면 이때 가장 작은 조각의 길이는 최대 15cm이다. 예를 들어 20cm, 35cm, 55cm 지점을 자를 때 최대가 된다.
### **입력**
첫 번째 줄에 자르는 횟수가 담긴 목록의 길이 N과 자를 수 있는 지점의 개수 M, 그리고 롤 케이크의 길이인 정수 L이 주어진다. (1 ≤ N ≤ M ≤ 1,000, 1 < L ≤ 4,000,000)

다음 M줄에 걸쳐 자를 수 있는 지점을 나타내는 정수 Si가 주어진다. (1 ≤ Si < L)

다음 N줄에 걸쳐 자르는 횟수를 나타내는 정수 Qi가 주어진다. (1 ≤ Qi ≤ M)

Si는 오름차순으로 주어지고 중복되는 수는 없으며, Qi도 마찬가지이다.
### **출력**
N개 줄에 걸쳐 각 목록에 있는 횟수대로 롤 케이크를 잘랐을 때 가장 작은 조각의 길이의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
2 5 70
10
20
35
55
60
3
4
```

**예제 출력1**

```
15
10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def can_make(x, q):
    count = 0
    last = 0

    for c in cuts:
        if c - last >= x:
            count += 1
            last = c
            if count == q:
                break
    
    if count == q and L - last >= x:
        return True
    
    return False

N, M, L = map(int, sys.stdin.readline().rstrip().split())
cuts = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

for q in queries:
    left, right = 1, L
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_make(mid, q):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|960|Python3|730
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
l = []
left = 0
for _ in range(m):
    x = int(input())
    l.append(x - left)
    left = x

l.append(k - left)
save = dict()

for _ in range(n):
    target = int(input())
    if target in save:
        print(save[target])
        continue

    left, right = 1, k
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        q = 0
        current = 0
        possible = True

        for piece in l:
            current += piece
            if current >= mid:
                q += 1
                current = 0

        if q >= target + 1:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)
    save[target] = ans
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kyr778|110984|168|PyPy3|765
#### **📝해설**

```python
import sys

# 현재 최소길이를 x로 잡았을 때 만들 수 있는 케이스인지 확인
def can_make(x, q):

    # 자른 횟수
    count = 0

    # 이전에 자른 위치
    last = 0

    # 모두 잘랐을 때
    for c in cuts:

        # x보다 크다면
        if c - last >= x:

            # 이번에 자름
            count += 1
            last = c

            # 이미 q번 잘랐다면 종료
            if count == q:
                break
    
    # q번 잘랐고, 마지막 조각도 x 보다 크다면 가능한 케이스
    if count == q and L - last >= x:
        return True
    
    # 아니라면 불가능한 케이스
    return False

N, M, L = map(int, sys.stdin.readline().rstrip().split())
cuts = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 쿼리를 하나씩 확인
for q in queries:

    # 이분 탐색
    left, right = 1, L
    answer = 0

    # 가능한 최소 조각의 길이를 이분탐색으로 찾음
    while left <= right:
        mid = (left + right) // 2
        if can_make(mid, q):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    # 출력
    print(answer)
```