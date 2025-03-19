# [16943] 숫자 재배치

### **난이도**
실버 1
## **📝문제**
두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다. 

가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.
### **입력**
첫째 줄에 두 정수 A와 B가 주어진다.
### **출력**
B보다 작은 C중에서 가장 큰 값을 출력한다. 그러한 C가 없는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
1234 3456
```

**예제 출력1**

```
3421
```

**예제 입력2**

```
1000 5
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
789 123
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
A, B = map(int, input().split())

a_str = sorted(str(A), reverse=True)
used = [False] * len(a_str)
best = -1

def make_permutation(path):
    global best

    if len(path) == len(a_str):
        num = int("".join(path))
        if num < B:
            best = max(best, num)
        return
    
    for i in range(len(a_str)):
        if used[i]:
            continue

        if i > 0 and a_str[i] == a_str[i-1] and not used[i-1]:
            continue

        if len(path) == 0 and a_str[i] == "0":
            continue

        used[i] = True
        make_permutation(path + [a_str[i]])
        used[i] = False

make_permutation([])
print(best)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32544|496|Python3|647
#### **📝해설**

**알고리즘**
```
1. 백트래킹
2. 순열
```

### **다른 풀이**

```python
def dfs(depth, visit, now):
    global ans
    if depth == L:
        ans = now
        return True
    
    for i in range(L):
        if visit & (1 << i):
            continue
        new = now + A[i] * 10 ** (L-1-depth)
        if 0 < new < B:
            if dfs(depth+1, visit | (1 << i), new):
                return True
    return False

A, B = input().split()
A = sorted(map(int, A), reverse=True)
B = int(B)
L = len(A)

ans = -1
dfs(0, 0, 0)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wansang93|30616|36|Python3|462
#### **📝해설**

```python
A, B = map(int, input().split())

# A를 문자열(리스트)의 형식으로 저장, 내림차순으로 정렬
a_str = sorted(str(A), reverse=True)

# 순열을 만들면서 숫자를 사용했는지 여부를 저장
used = [False] * len(a_str)

# 최대값
best = -1

# 재귀적으로 호출하면서 순열을 생성할 함수
def make_permutation(path):

    # 전역변수 설정
    global best

    # 순열을 마지막까지 만들었을 때,
    if len(path) == len(a_str):
        num = int("".join(path))

        # B보다 작으면서 가장 큰 값을 저장
        if num < B:
            best = max(best, num)
        return
    
    # A의 모든 숫자를 확인하면서
    for i in range(len(a_str)):

        # 이미 사용한 숫자라면 고려하지 않음
        if used[i]:
            continue
        
        # 중복된 숫자라면 고려하지 않음
        if i > 0 and a_str[i] == a_str[i-1] and not used[i-1]:
            continue
        
        # 0으로 시작한다면 고려하지 않음
        if len(path) == 0 and a_str[i] == "0":
            continue
        
        # 사용 여부 저장
        used[i] = True

        # 다음 숫자로 넘어감
        make_permutation(path + [a_str[i]])

        # 백트래킹
        used[i] = False

# 함수 시작
make_permutation([])
print(best)
```