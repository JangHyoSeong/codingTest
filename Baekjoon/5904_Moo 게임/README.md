# [5904] Moo 게임

### **난이도**
골드 5
## **📝문제**
Moo는 술자리에서 즐겁게 할 수 있는 게임이다. 이 게임은 Moo수열을 각 사람이 하나씩 순서대로 외치면 되는 게임이다.

Moo 수열은 길이가 무한대이며, 다음과 같이 생겼다. 

m o o m o o o m o o m o o o o m o o m o o o m o o m o o o o o 
Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다. 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자. 1보다 크거나 같은 모든 k에 대해서, S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다.

S(0) = "m o o"
S(1) = "m o o m o o o m o o"
S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"
위와 같은 식으로 만들면, 길이가 무한대인 문자열을 만들 수 있으며, 그 수열을 Moo 수열이라고 한다.

N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N (1 ≤ N ≤ 109)이 주어진다.
### **출력**
N번째 글자를 출력한다.
### **예제입출력**

**예제 입력1**

```
11
```

**예제 출력1**

```
m
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def get_length(k):
    if k == 0:
        return 3
    
    if length[k] != -1:
        return length[k]
    
    length[k] = get_length(k-1) * 2 + (k+3)

    return length[k]

def solve(n, k):
    if k == 0:
        return "moo"[n-1]
    
    left = get_length(k-1)
    middle = k + 3

    if n <= left:
        return solve(n, k-1)
    
    elif n <= left + middle:
        if n - left == 1:
            return "m"
        
        else:
            return "o"
    
    else:
        return solve(n - left - middle, k - 1)

N = int(input())

length = [-1] * 32
k = 0

while get_length(k) < N:
    k += 1

print(solve(N, k))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|32|Python3|625
#### **📝해설**

**알고리즘**
```
1. 분할 정복
```

### **다른 풀이**

```python
# 문제 URL : https://www.acmicpc.net/problem/17419
import sys
input = sys.stdin.readline

N = int(input())

if N <= 3:
    if N == 1:
        print('m')
    else:
        print('o')
    exit()

lnth = [3]
i = 0
while True:
    nxt = (lnth[i] * 2) + (i + 4)
    lnth.append(nxt) 
    i += 1
    if nxt > N:
        break

while True:
    i -= 1
    if N > lnth[i] + (i + 4):
        N = N - (lnth[i] + (i + 4))
        if N <= 3:
            break
    elif N > lnth[i]:
        N = N - lnth[i]
        break

if N == 1:
    print('m')
else:
    print('o')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pcy4196|31120|28|Python3|556
#### **📝해설**

```python
def get_length(k):

    # S(k)일 때, 그 수열의 길이를 구하는 재귀함수

    # k==0인 경우 길이는 moo : 3
    if k == 0:
        return 3
    
    # 이미 구해진 길이라면 그 값을 바로 리턴
    if length[k] != -1:
        return length[k]
    
    # S(k) = S(k-1) * 2 + m + o *(k+2)
    length[k] = get_length(k-1) * 2 + (k+3)

    # 현재 길이 리턴
    return length[k]

def solve(n, k):

    # 분할 정복으로 N번째 위치의 값을 찾음

    # 마지막까지 왔다면, moo에서 어느 위치인지 리턴
    if k == 0:
        return "moo"[n-1]
    
    # 왼쪽 Moo배열의 길이
    left = get_length(k-1)

    # 가운데 moo를 더한 뒤 길이
    middle = k + 3

    # 왼쪽에 있다면
    if n <= left:

        # 분할정복으로 더 깊게 들어감
        return solve(n, k-1)
    
    # 가운데 있다면
    elif n <= left + middle:

        # moo 중 값을 찾아 리턴
        if n - left == 1:
            return "m"
        
        else:
            return "o"
    
    # 오른쪽에 있다면 다시 분할정복
    else:
        return solve(n - left - middle, k - 1)

N = int(input())

# K가 최대 32까지라고 가정
length = [-1] * 32
k = 0

while get_length(k) < N:
    k += 1

print(solve(N, k))
```