# [1406] 에디터

### **난이도**
실버 2

## **📝문제**
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.

- L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
- D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
- B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
- P $	$라는 문자를 커서 왼쪽에 추가함

초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
### **입력**
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.
### **출력**
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
### **예제입출력**

**예제 입력1**

```
abcd
3
P x
L
P y
```

**예제 출력1**

```
abcdyx
```

**예제 입력2**

```
abc
9
L
L
L
L
L
P x
L
B
P y
```

**예제 출력2**

```
yxabc
```

**예제 입력3**

```
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z
```

**예제 출력3**

```
yxz
```

### **출처**
Olympiad > Croatian Highschool Competitions in Informatics > 2004 > National Competition #1 - Juniors 2번

## **🧐CODE REVIEW**

### **😫나의 오답 풀이**
### **🧾나의 풀이**

```python
left = list(input())
right = []

commands_num = int(input())


for i in range(commands_num):
    command = input().split()
    
    if command[0] == 'P':
        left.append(command[1])


    elif command[0] == 'L':
        if left != []:
            right.append(left.pop(len(left)-1))
               

    elif command[0] == 'D':
        if right != []:
            left.append(right.pop(len(right)-1))

    elif command[0] == 'B':
        if left != []:
            left.pop(len(left)-1)

left = ''.join(left)
right.reverse()
right = ''.join(right)

print(left + right)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|169576|368|PyPy3|572
#### **📝해설**

**알고리즘**
```
1. 스택 활용
```
그냥 리스트의 insert를 활용하면 시간복잡도가 O(n^2)이기 때문에 시간 초과에 걸린다.
따라서 양방향LinkedList, 혹은 스택을 사용하여 시간복잡도를 낮춰야 할 필요가 있다
#### **😅개선점**

1. Python3가 아닌 PyPy3를 통해 해결했다 -> 실행시간을 더 줄일 필요가 있다
2. LinkedList로도 한번 풀어보고 싶다


### **다른 풀이**

```python
import sys 
input = sys.stdin.readline

def cmd():
    sentence = input().rstrip()

    stack1 = list(sentence)
    stack2 = []
    for _ in range(int(input())):
        s_command = input()
        command = s_command[0]
        if command == 'L':
            if stack1:
                stack2.append(stack1.pop(-1))
        elif command == 'D':
            if stack2:
                stack1.append(stack2.pop(-1))
        elif command == 'B':
            if stack1: stack1.pop(-1)
        else:
            stack1.append(s_command[2])

    stack1.extend(reversed(stack2))

    print("".join(stack1))

cmd()
```

아이디 |	문제	| 문제 제목 |	결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:---------:|:-----:|:-----:|:-----:|:----:|:--------:
alex6856|1406|에디터|정답|37576|168|Python3|607
#### **📝해설**

```python
```

### **🔖정리**

1. 시간 제한이 빡빡한 문제의 경우 줄일 방법을 찾아야 한다.
2. 입력을 받을 경우 
```python
import sys  
input = sys.stdin.readline()
```
입력으로 발생하는 시간을 줄일 수 있다.

## 📚참고 사이트

> **[제목]**<br/>
사이트 주소