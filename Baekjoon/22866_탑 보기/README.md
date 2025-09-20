# [22866] 탑 보기

### **난이도**
골드 3
## **📝문제**
일직선으로 다양한 높이의 건물이 총 
$N$개가 존재한다. 각 건물 옥상에서 양 옆에 존재하는 건물의 옆을 몇 개 볼 수 있는지 궁금해졌다.

 
$i$번째 건물 기준으로 
$i - 1$, 
$i - 2$, ..., 
$1$번째 건물은 왼쪽에, 
$i + 1$, 
$i + 2$, ..., 
$N$번째 건물은 오른쪽에 있다. 각 건물 사이의 거리는 다 동일하다.

현재 있는 건물의 높이가 
$L$이라고 가정하면 높이가 
$L$보다 큰 곳의 건물만 볼 수 있다.

바라보는 방향으로 높이가 
$L$인 건물 뒤에 높이가 
$L$이하인 건물이 있다면 가려져서 보이지 않는다.

번호 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
---|---|---|---|---|---|---|---|--
높이 | 3 | 7 | 1 | 6 | 3 | 5 | 1 | 7
보이는 건물 번호 | 2 | x | 2, 4, 8 | 2, 8 | 2,4,6,8 | 2,4,8 | 2,4,6,8 | x
각 건물에서 볼 수 있는 건물들이 어떤것이 있는지 구해보자.
### **입력**
첫번째 줄에 건물의 개수 
$N$이 주어진다.

두번째 줄에는 
$N$개의 건물 높이가 공백으로 구분되어 주어진다.
### **출력**
 
$i(1 \le i \le N)$번째 건물에서 볼 수 있는 건물의 개수를 출력한다.

만약 볼 수 있는 건물의 개수가 1개 이상이라면 
$i$번째 건물에서 거리가 가장 가까운 건물의 번호 중 작은 번호로 출력한다.
### **예제입출력**

**예제 입력1**

```
8
3 7 1 6 3 5 1 7
```

**예제 출력1**

```
1 2
0
3 2
2 2
4 4
3 4
4 6
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = [0] * N
nearest = [0] * N

stack = []
for i in range(N):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        nearest[i] = stack[-1] + 1
    stack.append(i)

stack = []
for i in range(N - 1, -1, -1):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        
        if nearest[i] == 0:
            nearest[i] = stack[-1] + 1
        else:
            left_dist = abs((nearest[i] - 1) - i)
            right_dist = abs((stack[-1]) - i)
            if right_dist < left_dist or (right_dist == left_dist and stack[-1] + 1 < nearest[i]):
                nearest[i] = stack[-1] + 1
    stack.append(i)

for i in range(N):
    if count[i] == 0:
        print(0)
    else:
        print(count[i], nearest[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|130408|176|PyPy3|949
#### **📝해설**

**알고리즘**
```
1. 스택
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def check(tar):
    res = []
    for i in tar:
        while res and arr[res[-1]] <= arr[i]: res.pop()
        view[i] += len(res)
        if res:
            d = abs(i - res[-1])
            if abs(i - dist[i]) > d: dist[i] = res[-1]
        res.append(i)

n = int(input())
arr = list(map(int, input().split()))
view = [0] * n
dist = [float('inf')] * n
check(range(n))
check(range(n - 1, -1, -1))
for i in range(n): sys.stdout.write(f"{view[i]} {dist[i] + 1 if view[i] else ''}\n")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|130520|156|PyPy3|521
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 보이는 건물의 개수
count = [0] * N

# 가장 가까운 건물
nearest = [0] * N

# 스택을 사용해 보이는 건물을 확인
stack = []

# 왼쪽에서 오른쪽으로 확인
for i in range(N):

    # 다른 건물이 스택에 들어있고, 현재 건물보다 낮은 경우 pop
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()

    # 현재 건물보다 높은 건물을 만났다면
    if stack:
        # count++, 가장 가까운 건물에 갱신
        count[i] += len(stack)
        nearest[i] = stack[-1] + 1
    stack.append(i)

# 오른쪽에서 왼쪽으로 확인
stack = []
for i in range(N - 1, -1, -1):

    # 왼쪽과 동일
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()

    if stack:
        count[i] += len(stack)

        # 아직 가까운 건물이 없었다면 그대로 삽입
        if nearest[i] == 0:
            nearest[i] = stack[-1] + 1
        
        # 있었다면
        else:

            # 왼쪽 거리와 오른쪽 거리를 비교해서, 작은 것을 삽입
            left_dist = abs((nearest[i] - 1) - i)
            right_dist = abs((stack[-1]) - i)
            if right_dist < left_dist or (right_dist == left_dist and stack[-1] + 1 < nearest[i]):
                nearest[i] = stack[-1] + 1
    stack.append(i)

for i in range(N):
    if count[i] == 0:
        print(0)
    else:
        print(count[i], nearest[i])
```

### **🔖정리**

1. 배운점