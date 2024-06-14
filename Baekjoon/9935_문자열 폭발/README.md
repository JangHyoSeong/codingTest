# [9935] 문자열 폭발

### **난이도**
골드 4
## **📝문제**
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

- 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.  
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
### **입력**
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.
### **출력**
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
### **예제입출력**

**예제 입력1**

```
mirkovC4nizCC44
C4
```

**예제 출력1**

```
mirkovniz
```

**예제 입력2**

```
12ab112ab2ab
12ab
```

**예제 출력2**

```
FRULA
```

### **출처**
Contest > Croatian Open Competition in Informatics > COCI 2013/2014 > Contest #5 3번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
string = input()

boom = input()
boom_len = len(boom)

stack = []

for c in string:
    stack.append(c)
    if len(stack) >= boom_len and ''.join(stack[-boom_len:]) == boom:
        for i in range(boom_len):
            stack.pop()
    
if stack:
    print(''.join(stack))
else:
    print("FRULA")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42300|776|Python3|297
#### **📝해설**

**알고리즘**
```
1. 스택
```
#### **📝해설**

```python
# 입력받고, 폭발 문자열의 길이를 저장해둠
string = input()
boom = input()
boom_len = len(boom)

# 스택을 활용하여 문제 풀이
stack = []

# 문자열을 순회하면서
for c in string:
    # 일단 스택에 삽입
    stack.append(c)

    # 스택의 길이가 폭발 문자열의 길이보다 길다면,
    # 그리고 폭발 문자열의 길이만큼 슬라이싱 했을 때, 그 문자열이 폭발 문자열과 같다면
    if len(stack) >= boom_len and ''.join(stack[-boom_len:]) == boom:
        # 폭발 문자열의 길이만큼 스택에서 pop
        for i in range(boom_len):
            stack.pop()

# 스택이 비어있지 않다면
if stack:
    # 그 문자열을 출력
    print(''.join(stack))
# 스택이 비어있다면
else:
    print("FRULA")
```