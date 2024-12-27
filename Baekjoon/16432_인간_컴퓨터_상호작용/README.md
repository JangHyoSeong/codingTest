# [16432] 인간-컴퓨터 상호작용

### **난이도**
실버 1
## **📝문제**
승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다. 

'문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'

승재를 도와 특정 문자열 
$S$, 특정 알파벳 
$\alpha$와 문자열의 구간 
$[l,r]$이 주어지면 
$S$의 
$l$번째 문자부터 
$r$번째 문자 사이에 
$\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 
$0$번째부터 세며, 
$l$번째와 
$r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 
$q$번 할 것이다.
### **입력**
첫 줄에 문자열 
$S$가 주어진다. 문자열의 길이는 
$200,000$자 이하이며 알파벳 소문자로만 구성되었다. 두 번째 줄에는 질문의 수 
$q$가 주어지며, 문제의 수는 
$1\leq q\leq 200,000$을 만족한다. 세 번째 줄부터 
$(q+2)$번째 줄에는 질문이 주어진다. 각 질문은 알파벳 소문자 
$\alpha_i$와 
$0\leq l_i\leq r_i<|S|$를 만족하는 정수 
$l_i,r_i$가 공백으로 구분되어 주어진다.
### **출력**
각 질문마다 줄을 구분해 순서대로 답변한다. 
$i$번째 줄에 
$S$의 
$l_i$번째 문자부터 
$r_i$번째 문자 사이에 
$\alpha_i$가 나타나는 횟수를 출력한다.
### **예제입출력**

**예제 입력1**

```
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
```

**예제 출력1**

```
0
1
2
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.stdin.readline().rstrip()

string = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline().rstrip())

len_string = len(string)
char_dict = {}
for num in range(ord('a'), ord('z')+1):
    char_dict[chr(num)] = [0] * (len_string + 1)

for i in range(1, len_string + 1):
    for num in range(ord('a'), ord('z')+1):
        char_dict[chr(num)][i] = char_dict[chr(num)][i-1]
    
    char_dict[string[i-1]][i] += 1

for _ in range(q):
    c, l, r = sys.stdin.readline().rstrip().split()
    print(char_dict[c][int(r)+1] - char_dict[c][int(l)])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|153116|588|PyPy3|526
#### **📝해설**

**알고리즘**
```
1. 누적합
```

### **다른 풀이**

```python
import sys
input =sys.stdin.readline
s = input().strip()
q = int(input())
count_list = [[0] * (len(s)+1) for _ in range(26)]

for i in range(1,len(s)+1):
    count_list[ord(s[i-1]) - ord('a')][i] += 1

for i in range(26):
    for j in range(1,len(s)+1):
        count_list[i][j] += count_list[i][j-1]

for i in range(q):
    a,l,r = input().split()
    l = int(l); r= int(r)
    print(count_list[ord(a) - ord('a')][r+1] - count_list[ord(a)- ord('a')][l])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ckdgh6589|152948|260|PyPy3|454
#### **📝해설**

```python
import sys

# 입력받기
string = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline().rstrip())

len_string = len(string)

# 각 문자가 해당 인덱스까지 몇개나왔는지 저장할 딕셔너리
char_dict = {}

# a-z 까지 모든 알파벳에 대해 리스트를 선언
for num in range(ord('a'), ord('z')+1):
    char_dict[chr(num)] = [0] * (len_string + 1)

# 문자열을 모두 검사하면서
for i in range(1, len_string + 1):

    # 일단은 누적합을 계산하기 위해 앞의 숫자를 저장
    for num in range(ord('a'), ord('z')+1):
        char_dict[chr(num)][i] = char_dict[chr(num)][i-1]
    
    # 해당하는 문자는 ++
    char_dict[string[i-1]][i] += 1

# 질문에 대해 출력
for _ in range(q):
    c, l, r = sys.stdin.readline().rstrip().split()
    print(char_dict[c][int(r)+1] - char_dict[c][int(l)])
```