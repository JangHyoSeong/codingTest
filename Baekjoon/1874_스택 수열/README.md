# [1874] 스택 수열

### **난이도**
실버 2
## **📝문제**
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
### **입력**
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.
### **출력**
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
### **예제입출력**

**예제 입력1**

```
8
4
3
6
8
7
5
2
1
```

**예제 출력1**

```
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
```

**예제 입력2**

```
5
1
2
5
3
4
```

**예제 출력2**

```
NO
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N  = int(input())
arr = [int(input()) for _ in range(N)]

idx = 1
stack = []
result = []

for num in arr:
    while idx <= num:
        stack.append(idx)
        result.append('+')
        idx += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result = False
        break

if result:
    for c in result:
        print(c)
else:
    print('NO')
```

결과| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36560|5404|Python3|393
#### **📝해설**

**알고리즘**
```
1. 스택
```

### **다른 풀이**

```python
import sys


def solution():
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append('-')
    return '\n'.join(answer)


print(solution())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yankeecanmoa|41012|72|Python3|387
#### **📝해설**

```python
N  = int(input())
arr = [int(input()) for _ in range(N)]

# 현재 스택에 삽입할 숫자
idx = 1
# 스택, 결과값
stack = []
result = []

# 만들어야 할 리스트를 순회하면서
for num in arr:
    # 현재 스택에 넣어야 할 값이 만들어야 할 숫자보다 작다면
    # 스택에 삽입
    while idx <= num:
        stack.append(idx)
        result.append('+')
        idx += 1
    
    # 스택의 top이 만들어야 할 숫자와 같다면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 아니라면 만들지 못하는 스택
    else:
        result = False
        break

if result:
    for c in result:
        print(c)
else:
    print('NO')
```