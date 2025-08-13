# [1522] 문자열 교환

### **난이도**
실버 1
## **📝문제**
a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.

이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.

예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.
### **입력**
첫째 줄에 문자열이 주어진다. 문자열의 길이는 최대 1,000이다.
### **출력**
첫째 줄에 필요한 교환의 회수의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
abababababababa
```

**예제 출력1**

```
3
```

**예제 입력2**

```
ba
```

**예제 출력2**

```
0
```

**예제 입력3**

```
aaaabbbbba
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
string = list(input())
a_count = string.count('a')
n = len(string)

if a_count == 0 or a_count == n:
    print(0)
    exit()

extended = string * 2

b_count = extended[:a_count].count('b')
min_swaps = b_count

for i in range(a_count, len(extended)):
    if extended[i] == 'b':
        b_count += 1
    
    if extended[i - a_count] == 'b':
        b_count -= 1
    
    min_swaps = min(min_swaps, b_count)

print(min_swaps)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32544|36|Python3|423
#### **📝해설**

**알고리즘**
```
1. 슬라이딩 윈도우
```

### **다른 풀이**

```python
import sys

arr = sys.stdin.readline().strip()
a = arr.count('a')
arr += arr[:a-1]

res = float('inf')
for i in range(len(arr)-(a-1)):
    res = min(res, arr[i: i+a].count('b'))
    
print(res)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
heoraeng|31120|32|Python3|194
#### **📝해설**

```python
string = list(input())

# 현재 문자열에서 a가 몇개 있는지 확인
a_count = string.count('a')
n = len(string)

# 만약 a가 하나도 없거나 모두 a라면 답은 0
if a_count == 0 or a_count == n:
    print(0)
    exit()


# 원형으로 이어져있으니, 뒤까지 확인하기 위해 길이를 2배로 늘림
extended = string * 2


# 현재 0인덱스부터 a의 개수만큼 확인하면서, b가 몇개있는지 셈
b_count = extended[:a_count].count('b')

# b의 개수만큼 교환을 해야함. 이 때 최소가 될 때가 정답
min_swaps = b_count

# 슬라이딩 윈도우
for i in range(a_count, len(extended)):

    # 이번에 추가된 문자가 b라면
    if extended[i] == 'b':

        # b 개수 추가
        b_count += 1
    
    # 이번에 빠진 문자가 b라면
    if extended[i - a_count] == 'b':

        # b 개수 감소
        b_count -= 1
    
    # 최소값 갱신
    min_swaps = min(min_swaps, b_count)

print(min_swaps)
```