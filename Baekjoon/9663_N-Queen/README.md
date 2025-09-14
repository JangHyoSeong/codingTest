# [9663] N-Queen

### **난이도**
골드 4
## **📝문제**
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N이 주어진다. (1 ≤ N < 15)
### **출력**
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
8
```

**예제 출력1**

```
92
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

table = [-1] * N
result = 0

def check_valid(x, y):
    for i in range(x):
        if table[i] == y or abs(x - i) == abs(y - table[i]):
            return False
    
    return True

def backtracking(depth, N):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        if check_valid(depth, i):
            table[depth] = i
            backtracking(depth + 1, N)

backtracking(0, N)
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|212864|29868|PyPy3|461
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

#### **📝해설**

```python
N = int(input())

# 퀸이 각 열에서 몇번째에 위치하는지 저장
table = [-1] * N
result = 0

# 퀸을 놓을 수 있는 위치인지 검사하는 함수
def check_valid(x, y):

    # 이전에 놓은 퀸들을 확인하면서
    for i in range(x):

        # 같은 줄에 있거나, 대각선에 존재한다면 False
        if table[i] == y or abs(x - i) == abs(y - table[i]):
            return False
    # 아니라면 True
    return True

# 백트래킹을 하면서 퀸을 위치함
def backtracking(depth, N):
    global result

    # 보드를 모두 채웠다면 결과 ++
    if depth == N:
        result += 1
        return

    # 이번 줄의 모든 위치를 검사하면서
    for i in range(N):

        # 퀸을 놓을 수 있다면 놓음
        if check_valid(depth, i):
            table[depth] = i

            # 다음으로 이동
            backtracking(depth + 1, N)

backtracking(0, N)
print(result)
```