# [2504] 괄호의 값

### **난이도**
골드 5
## **📝문제**
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

1. ‘()’ 인 괄호열의 값은 2이다.
2. ‘[]’ 인 괄호열의 값은 3이다.
3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.  
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.
### **입력**
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
### **출력**
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
### **예제입출력**

**예제 입력1**

```
(()[[]])([])
```

**예제 출력1**

```
28
```

**예제 입력2**

```
[][]((])
```

**예제 출력2**

```
0
```

### **출처**
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2008 > 초등부 4번

Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2008 > 중등부 2번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
arr = list(input())
stack = []
is_valid = True

for bracket in arr:
    if bracket == '(' or bracket == '[':
        stack.append(bracket)
    else:
        if not stack:
            is_valid = False
            break
        
        top = stack.pop()
        
        if (bracket == ')' and top == '(') or (bracket == ']' and top == '['):
            value = 2 if bracket == ')' else 3
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        elif isinstance(top, int):
            if not stack:
                is_valid = False
                break
            opening_bracket = stack.pop()
            if (bracket == ')' and opening_bracket != '(') or (bracket == ']' and opening_bracket != '['):
                is_valid = False
                break
            multiplier = 2 if bracket == ')' else 3
            value = top * multiplier
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        else:
            is_valid = False
            break

# 최종 값 계산
total_value = 0
for item in stack:
    if isinstance(item, int):
        total_value += item
    else:
        is_valid = False

if is_valid:
    print(total_value)
else:
    print(0)

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|36|Python3|1459
#### **📝해설**

**알고리즘**
```
1. 스택
```

#### **📝해설**

```python
arr = list(input())
stack = []
is_valid = True

for bracket in arr:
    # 여는 괄호는 스택에 삽입
    if bracket == '(' or bracket == '[':
        stack.append(bracket)
    
    # 닫는 괄호라면
    else:
        # 스택이 비어있다면 올바르지 않은 괄호입력
        if not stack:
            is_valid = False
            break
        
        # 스택의 맨 위 값을 pop
        top = stack.pop()
        
        # 만약 여는괄호, 닫는괄호가 제대로 쌍이 맞다면
        if (bracket == ')' and top == '(') or (bracket == ']' and top == '['):
            # ()인 경우 값은 2, []인 경우 값은 3
            value = 2 if bracket == ')' else 3
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        elif isinstance(top, int):
            if not stack:
                is_valid = False
                break
            opening_bracket = stack.pop()
            if (bracket == ')' and opening_bracket != '(') or (bracket == ']' and opening_bracket != '['):
                is_valid = False
                break
            multiplier = 2 if bracket == ')' else 3
            value = top * multiplier
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        else:
            is_valid = False
            break

# 최종 값 계산
total_value = 0
for item in stack:
    if isinstance(item, int):
        total_value += item
    else:
        is_valid = False

if is_valid:
    print(total_value)
else:
    print(0)

```