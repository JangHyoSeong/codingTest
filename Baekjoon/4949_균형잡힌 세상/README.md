# [4949] 균형잡힌 세상

### **난이도**
실버 4
## **📝문제**
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.  
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
### **입력**
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.

### **출력**
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
### **예제입출력**

**예제 입력1**

```
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
```

**예제 출력1**

```
yes
yes
no
no
no
yes
yes
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
while True:
    string = input()
    if string == ".":
        break

    flag = True
    stack = []
    for c in string:
        if c in ["[", "("]:
            stack.append(c)

        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break

        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    if stack:
        flag = False
    
    print("yes" if flag else "no")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|228|Python3|583
#### **📝해설**

**알고리즘**
```
1. 스택
```

### **다른 풀이**

```python
import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s==".":break
    if s.count("(")!=s.count(")") or s.count("[")!=s.count("]"):print("no");continue
    b=""
    for i in s:
        if i in "()[]":
            b+=i
    while "()" in b or "[]" in b:
        if "()" in b:b=b.replace("()","")
        if "[]" in b:b=b.replace("[]","")
    if b=="":print("yes")
    else:print("no")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sakura0319|31120|48|Python3|396
#### **📝해설**

```python
while True:

    # 온점만 입력받았다면 종료
    string = input()
    if string == ".":
        break

    # 균형잡혀있는지 여부를 저장
    flag = True
    stack = []

    # 문자들을 탐색하면서
    for c in string:

        # 열린괄호라면
        if c in ["[", "("]:

            # 스택에 삽입
            stack.append(c)

        # 닫힌괄호를 만났을 때
        if c == ")":

            # 스택에 괄호가 존재하고, 직전 괄호가 여는 괄호였다면
            if stack and stack[-1] == "(":

                # 괄호를 pop
                stack.pop()

            # 아닌 경우 균형잡힌 문자열이 아님
            else:
                flag = False
                break
        
        # 대괄호도 동일
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    # 문자를 모두 탐색했는데 괄호가 남아있다면 균형잡히지 않음
    if stack:
        flag = False
    
    print("yes" if flag else "no")
```