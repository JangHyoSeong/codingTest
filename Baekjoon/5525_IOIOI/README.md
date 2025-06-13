# [5525] IOIOI

### **난이도**
실버 1
## **📝문제**
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

- P1 IOI
- P2 IOIOI
- P3 IOIOIOI
- PN IOIOI...OI (O가 N개)

I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.
### **출력**
S에 PN이 몇 군데 포함되어 있는지 출력한다.
### **예제입출력**

**예제 입력1**

```
1
13
OOIOIOIOIIOII
```

**예제 출력1**

```
4
```

**예제 입력2**

```
2
13
OOIOIOIOIIOII
```

**예제 출력2**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

count = 0
i = 0
pattern = 0

while i < M - 1:
    if S[i] == "I" and S[i+1] == "O":
        j  = i + 1
        while j + 1 < M and S[j] == "O" and S[j+1] == "I":
            pattern += 1
            j += 2
            if pattern == N:
                count += 1
                pattern -= 1
        i = j
        pattern = 0
    
    else:
        i += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34368|252|Python3|493
#### **📝해설**

**알고리즘**
```
1. KMP
2. 문자열
```

### **다른 풀이**

```python
from sys import stdin

def get_continuous_num(s, start_index):
    count = 1
    while True:
        if s[start_index : start_index + 2] == "OI":
            count += 1
            start_index += 2
        else:
            return count

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()
target = "I" + "OI" * n


count = 0
while True:
    target_index = s.find(target)
    if target_index == -1:
        break

    continuous_num = get_continuous_num(s, target_index + len(target))
    count += continuous_num
    s = s[target_index + len(target) + (len("OI") * (continuous_num - 1)):]

print(count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
glaehfdl1654|34184|84|Python3|633
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

# 정답, 인덱스, 중첩확인
count = 0
i = 0
pattern = 0

# S 문자열을 반복으로 확인
while i < M - 1:

    # 만약 I로 시작하고, 다음이 O일 때
    if S[i] == "I" and S[i+1] == "O":

        # 다음 문자부터 확인
        j  = i + 1

        # 다음 문자가 O로 시작하고, 그다음이 I라면,
        while j + 1 < M and S[j] == "O" and S[j+1] == "I":

            # IOI가 하나 있음을 확인하기 위해 ++
            pattern += 1

            # 두칸 뒤를 확인
            j += 2

            # 현재 IOI가 N개만큼 있다면
            if pattern == N:

                # count ++
                count += 1

                # 두칸 뒤로 넘어갔으니 pattern을 --
                pattern -= 1

        # 반복이 끝났다면 확인한 부분만큼 건너뜀
        i = j
        pattern = 0
    
    # 패턴이 없다면 바로 i++
    else:
        i += 1

print(count)
```