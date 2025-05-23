# [12904] A와 B

### **난이도**
골드 5
## **📝문제**
수빈이는 A와 B로만 이루어진 영어 단어가 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

- 문자열의 뒤에 A를 추가한다.
- 문자열을 뒤집고 뒤에 B를 추가한다.  
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 
### **입력**
첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 999, 2 ≤ T의 길이 ≤ 1000, S의 길이 < T의 길이)
### **출력**
S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
B
ABBA
```

**예제 출력1**

```
1
```

**예제 입력2**

```
AB
ABB
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
S = input()
T = input()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

print(1 if T == S else 0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|162
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

#### **📝해설**

```python
S = input()
T = input()

# T의 문자열을 S로 바꾸는 방식은 오직 하나만 존재(문자열 끝이 A거나 B거나)
while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

# 끝까지 줄였을때 S와 T가 같지 않으면 0 출력
print(1 if T == S else 0)
```