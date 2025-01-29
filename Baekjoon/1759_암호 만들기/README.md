# [1759] 암호 만들기

### **난이도**
골드 5
## **📝문제**
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.
### **출력**
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
### **예제입출력**

**예제 입력1**

```
4 6
a t c i s w
```

**예제 출력1**

```
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())

combs = combinations(arr, L)
result = []
for comb in combs:
    vowel = 0
    for c in list(comb):
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1

    if 1 <= vowel <= L-2:
        result.append(sorted(list(comb)))

result.sort()
for answer in result:
    print("".join(map(str, answer)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|405
#### **📝해설**

**알고리즘**
```
1. 조합
2. 백트래킹
```

### **다른 풀이**

```python
from itertools import combinations

a = ['a','e','i','o','u']
L, C = input().split()
L = int(L)
C = int(C)

def is_possible(word):
	vow = 0
	for i in a:
		vow = vow + (i in word)
	con = L - vow
	return (vow >= 1) & (con >= 2)



s_input = input().split()
s_input.sort()

for comb in combinations(s_input,L):
	if is_possible(comb):
		print(''.join(comb))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
xk130|31120|28|Python3|353
#### **📝해설**

```python
from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())

# 가능한 모든 조합을 생성
combs = combinations(arr, L)

# 비밀번호로 가능한 문자열을 저장할 리스트
result = []

# 모든 조합을 순회하면서
for comb in combs:

    # 모음 개수를 셈
    vowel = 0
    for c in list(comb):
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1

    # 최소 모음 하나, 자음 2개를 만족한다면
    if 1 <= vowel <= L-2:
        # 정답리스트에 정렬해서 삽입
        result.append(sorted(list(comb)))

# 정답 리스트도 정렬
result.sort()

# 출력
for answer in result:
    print("".join(map(str, answer)))
```