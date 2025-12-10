# [5555] 반지

### **난이도**
실버 5
## **📝문제**
당신은 N개의 반지를 가지고 있다. 각각의 반지는 대문자 10 문자로 이루어진 문자열이 새겨져 있다. 반지는 문자열의 시작과 끝이 연결된 형태로 문자가 새겨져 있다. 반지에 각인된 문자열을 거꾸로 읽는 걱정은 없다.

찾고자하는 문자열이 주어졌을 때 그 문자열을 포함하는 반지가 몇 개인지를 발견하는 프로그램을 작성하라.
### **입력**
입력은 총 2 + N 줄 이다.

첫 번째 줄에는 1 자 이상 10 자 이하의 대문자로 구성된 찾고자 하는 문자열이 적혀있다.

두 번째 줄에는 반지의 개수 N (1 ≦ N ≦ 100)이 적혀있다.

2+i 줄(1 ≦ i ≦ N)엔 i개의 반지에 새겨져있고, 10 문자로 이루어진 문자열이 적혀있다.
### **출력**
찾고자하는 문자열을 포함 반지의 개수를 나타내는 정수를 한 줄로 출력하라.
### **예제입출력**

**예제 입력1**

```
ABCD
3
ABCDXXXXXX
YYYYABCDXX
DCBAZZZZZZ
```

**예제 출력1**

```
2
```

**예제 입력2**

```
XYZ
1
ZAAAAAAAXY
```

**예제 출력2**

```
1
```

**예제 입력3**

```
PQR
3
PQRAAAAPQR
BBPQRBBBBB
CCCCCCCCCC
```

**예제 출력3**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
target = input()
target_len = len(target)
N = int(input())

count = 0
for _ in range(N):
    ring = input()
    ring = ring + ring

    for i in range(20 - target_len):
        if target == ring[i:i+target_len]:
            count += 1
            break

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|32|Python3|266
#### **📝해설**

**알고리즘**
```
1. 문자열
```

### **다른 풀이**

```python
import sys
target = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
rings = [sys.stdin.readline().strip() for i in range(N)]

cnt = 0
for ring in rings:
    if target in ring * 2:
        cnt += 1
        
print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
guswnee00|31120|28|Python3|235
#### **📝해설**

```python
target = input()
target_len = len(target)
N = int(input())

# 정답 갯수
count = 0

for _ in range(N):
    
    # 문자열 끝에서 다시 이어질 수 있기 때문에, 문자열을 두배로 늘림
    ring = input()
    ring = ring + ring

    # 일치하는 곳이 있는지 확인
    for i in range(20 - target_len):
        if target == ring[i:i+target_len]:
            count += 1
            break

print(count)
```