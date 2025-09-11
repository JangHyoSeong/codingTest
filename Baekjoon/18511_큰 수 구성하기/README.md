# [18511] 큰 수 구성하기

### **난이도**
실버 5
## **📝문제**
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.
### **입력**
첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3) 둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다. 각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.
### **출력**
첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
657 3
1 5 7
```

**예제 출력1**

```
577
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, k = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort(reverse=True)

answer = 0

def dfs(s):
    global answer

    if s:
        num = int(s)
        if num <= N:
            answer = max(answer, num)
        else:
            return
        
    if len(s) >= len(str(N)):
        return
    
    for d in digits:
        dfs(s + str(d))

dfs("")
print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|393
#### **📝해설**

**알고리즘**
```
1. 재귀
```

### **다른 풀이**

```python
from itertools import product

N,k = map(int,input().split())
box = list(input().split())
r = len(str(N))
while True:
    found = False
    for i in sorted(list(map(int,map(''.join,product(box, repeat=r)))), reverse = True):
        if N >= i:
            print(i)
            found = True
            break
    if found:
        break
    else:
        r -= 1
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
chiws93|31120|32|Python3|360
#### **📝해설**

```python
N, k = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort(reverse=True)

answer = 0

# 재귀적으로 앞에서부터 숫자를 만들어감
def dfs(s):

    # 전역변수 설정
    global answer

    # s가 값이 있는 경우에만
    if s:
        num = int(s)

        # N보다 작은 경우, 최대 값을 갱신
        if num <= N:
            answer = max(answer, num)
        
        # N보다 커진다면 이 케이스는 종료
        else:
            return
    
    # 길이를 넘어간다면 종료
    if len(s) >= len(str(N)):
        return
    
    # 모든 숫자를 하나씩 다 확인
    for d in digits:
        dfs(s + str(d))

dfs("")
print(answer)
```