# [문제번호] 문제제목

### **난이도**
플래티넘 5
## **📝문제**
오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.

이 역사적인 순간을 맞이하기 위해 줄에서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해졌다.

두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.

줄에 서 있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)

둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 231 나노미터 보다 작다.

사람들이 서 있는 순서대로 입력이 주어진다.
### **출력**
서로 볼 수 있는 쌍의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
7
2
4
1
2
2
5
1
```

**예제 출력1**

```
10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from sys import stdin

N = int(stdin.readline().rstrip())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]


stack = []
count = 0

for i in range(N):

    same_height = 1

    while stack and stack[-1][0] <= arr[i]:
        count += stack[-1][1]

        if stack[-1][0] == arr[i]:
            same_height += stack[-1][1]

        stack.pop()

    if stack:
        count += 1
    
    stack.append([arr[i], same_height])

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|168372|252|PyPy3|443
#### **📝해설**

**알고리즘**
```
1. 스택
```

### **다른 풀이**

```python
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

int1 = lambda: int(input())
ints = lambda: map(int,input().split())
intl = lambda: list(map(int,input().split()))

N = int1()
arr = [int1() for _ in range(N)]

stack = [0]*500000
top = -1
prevs = [-1]

stack[0] = arr[0]
top = 0

ans = 0

for h in arr[1:]:
    if h < stack[top]:
        prevs.append(top)
        top += 1
        stack[top] = h
        ans += 1
    elif h >= stack[top]:
        # 같아질때까지 먹어버리기
        top_new = top
        while top_new >= 0 and h > stack[top_new]:
            top_new -= 1
        # 큰거 찾을때까지 이동하기
        if stack[prevs[-1]] <= h:
            while prevs[-1] >= 0 and stack[prevs[-1]] <= h:
                prevs.pop()
        prev = prevs[-1]
        if prev < 0:
            ans += top - prev
        else:
            ans += top - prev + 1   # prev위치의 것도 보임
        top = top_new + 1
        stack[top] = h

print(ans)   
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
books1234|165184|164|PyPy3|1006
#### **📝해설**

```python
from sys import stdin

N = int(stdin.readline().rstrip())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]


# 스택을 사용하여 계산
stack = []
count = 0

# 처음부터 순회하면서
for i in range(N):

    # 현재와 동일한 숫자의 개수를 셀 변수
    same_height = 1

    # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막값보다 크거나 같다면
    while stack and stack[-1][0] <= arr[i]:

        # 스택의 마지막 값과 같은 숫자들의 개수를 더함
        count += stack[-1][1]

        # 스택의 top과 현재 숫자가 같다면, same_height의 개수를 더해줌
        if stack[-1][0] == arr[i]:
            same_height += stack[-1][1]

        # pop
        stack.pop()

    # 스택이 비어있지 않다면 count++
    if stack:
        count += 1
    
    # 현재 값을 스택에 삽입
    stack.append([arr[i], same_height])

print(count)
```

### **🔖정리**

1. 중복 처리를 잘하자