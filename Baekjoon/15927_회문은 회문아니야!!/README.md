# [15927] 회문은 회문아니야!!

### **난이도**
골드 5
## **📝문제**
팰린드롬이란 앞으로 읽으나 뒤로 읽으나 같은 문자열을 말한다. 팰린드롬의 예시로 POP, ABBA 등이 있고, 팰린드롬이 아닌 것의 예시로 ABCA, PALINDROME 등이 있다.

같은 의미를 가지는 여러 단어들을 보자.

회문 (한국어)
- palindrome (영어, 프랑스어, 노르웨이어, 그리스어, 라틴어)
- 回文 (일본어, 중국어)
- palindrom (독일어, 덴마크어)
- palindromi (핀란드어)
- palíndromo (스페인어, 포르투갈어)
- palindromo (이탈리아어, 에스페란토어)
- палиндром (러시아어)
- قلب مستو (아랍어)
뭔가 이상한 점이 보이지 않는가? 그 어떤 언어에서도 팰린드롬을 뜻하는 단어는 팰린드롬이 아니다! 많은 사람들이 추구하는 “대칭의 아름다움”은 그저 허상에 불과하다.

알파벳 대문자로 이루어진 문자열이 주어졌을 때, 팰린드롬이 아닌 가장 긴 부분문자열의 길이를 구해 보자. 이때 부분문자열을 이루는 글자는 연속해야 한다. AB는 ABCD의 부분문자열이지만, AC는 아니다.
### **입력**
길이가 1 이상 50만 이하인 문자열이 주어진다.
### **출력**
팰린드롬이 아닌 가장 긴 부분문자열의 길이를 출력한다. 그런 부분문자열이 없으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
ABCBA
```

**예제 출력1**

```
4
```

**예제 입력2**

```
PALINDROME
```

**예제 출력2**

```
10
```

**예제 입력3**

```
ZZZ
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

string = sys.stdin.readline().rstrip()
n = len(string)

all_same = True
for i in range(1, n):
    if string[i] != string[0]:
        all_same = False
        break

if all_same:
    print(-1)
    sys.exit()

left, right = 0, n-1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(n-1 if is_palindrome else n)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33392|112|Python3|430
#### **📝해설**

**알고리즘**
```
1. 문자열
```

#### **📝해설**

```python
'''
1. 문자 전체가 같은 단어인 경우 : 무조건 회문이니 -1
2. 문자 전체가 회문인 경우: 전체 길이가 N이라면, 무조건 N-1이 회문이 아님
3. 문자가 회문이 아닌경우 : 무조건 N
'''
import sys

string = sys.stdin.readline().rstrip()
n = len(string)

all_same = True
for i in range(1, n):
    if string[i] != string[0]:
        all_same = False
        break

if all_same:
    print(-1)
    sys.exit()

left, right = 0, n-1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(n-1 if is_palindrome else n)
```