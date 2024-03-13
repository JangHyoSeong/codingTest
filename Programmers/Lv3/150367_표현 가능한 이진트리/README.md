# 문제 제목
표현 가능한 이진트리
## **📝문제 설명**
링크 참조
### **⚠제한사항**
- 1 ≤ numbers의 길이 ≤ 10,000
  - 1 ≤ numbers의 원소 ≤ 1015
### **입출력 예**
|numbers|result|
|:--:|:--:|
|[7, 42, 5]|[1, 1, 0]|
|[63, 111, 95]|[1, 1, 0]|
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**
트리 변환을 잘못하고있었다
### **🧾나의 풀이**

```python
from math import log2, ceil

def divide(bin_num):

    global flag
    if flag:
        return
    
    length = len(bin_num)
    if length == 0:
        return
    
    root = length//2
    left_tree = bin_num[:root]
    right_tree= bin_num[root+1:]

    if bin_num[root] == '0':

        if flag:
            return
        
        if '1' in bin_num:
            flag = True
            return
    else:
        divide(left_tree)
        divide(right_tree)


def solution(numbers):

    
    answer = []
    global flag

    for num in numbers:
        flag = False

        bin_num = bin(num)[2:]
        bin_len = len(bin_num)
        
        height = ceil(log2(bin_len+1))
        temp = 2**height

        bin_num = bin_num.zfill(temp-1)
        divide(bin_num)

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
```

#### **📝해설**

```python
from math import log2, ceil

def divide(bin_num):

    #flag를 전역변수로 사용
    global flag

    # 가지치기, True로 바뀌었다면 함수를 바로 끝냄
    if flag:
        return
    
    # 분할을 끝까지 해서 전부 나누었다면 return
    # 분할이 끝까지 가능했다 -> 중간에 이상한 것 없이 트리 순회를 마무리했다
    length = len(bin_num)
    if length == 0:
        return
    
    # 부모노드의 위치. 문제의 조건대로 배치하면 항상 길이의 절반위치
    root = length//2
    # 왼쪽, 오른쪽 서브트리
    left_tree = bin_num[:root]
    right_tree= bin_num[root+1:]

    # 부모가 0이라면 -> 양쪽 자식에 1이 있으면 안됨
    # -> 양쪽 자식이 둘 다 0이다
    # -> 서브트리의 전체가 0이어야 한다
    if bin_num[root] == '0':

        # 가지치기 2
        if flag:
            return
        
        # 서브트리의 전체에 1이 있다면 flag를 True로 바꿈
        if '1' in bin_num:
            flag = True
            return
        
    # 문제가 없다면 다시 양쪽 서브트리로 분할
    else:
        divide(left_tree)
        divide(right_tree)


def solution(numbers):

    
    answer = []
    # 전역변수로 flag 선언
    # 트리로 표현 불가능하다면 True가 될 것
    global flag

    for num in numbers:
        flag = False

        # 2진수 변환
        bin_num = bin(num)[2:]
        bin_len = len(bin_num)
        
        # 2진수를 완전트리로 표현하기 위해 계산
        height = ceil(log2(bin_len+1))
        # temp-1 은 트리의 노드 개수
        temp = 2**height

        # 빈 노드를 0으로 채워줌
        bin_num = bin_num.zfill(temp-1)
        # 분할정복 시작
        divide(bin_num)

        # flag가 True면 0, False라면 1
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
```

### **다른 풀이**

```python
def solution(numbers):
    def check(i, s):
        if numbers[i] and (L:=(len(s)//2)):
            if s[L]=='0' and ('1' in s):
                numbers[i] = 0
            else:
                check(i, s[:L]), check(i, s[L+1:])

    for i,n in enumerate(numbers):
        s, numbers[i] = bin(n)[2:], 1
        len_s, L = len(s), 1
        while len_s >= L:
            L *= 2        
        s = s.rjust(L-1, '0')
        check(i, s)
    return numbers
```

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150367)**<br/>