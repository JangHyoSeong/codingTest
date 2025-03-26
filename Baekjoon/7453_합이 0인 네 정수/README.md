# [7453] 합이 0인 네 정수

### **난이도**
골드 2
## **📝문제**
정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.

A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 배열의 크기 n (1 ≤ n ≤ 4000)이 주어진다. 다음 n개 줄에는 A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어진다. 배열에 들어있는 정수의 절댓값은 최대 2**28이다.
### **출력**
합이 0이 되는 쌍의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
```

**예제 출력1**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
arr = [list(x) for x in zip(*(map(int, sys.stdin.readline().rstrip().split()) for _ in range(N)))]

sum_AB = defaultdict(int)
for a in arr[0]:
    for b in arr[1]:
        sum_AB[a+b] += 1

count = 0
for c in arr[2]:
    for d in arr[3]:
        target = -(c + d)

        if target in sum_AB:
            count += sum_AB[target]

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|1190812|10000|PyPy3|430
#### **📝해설**

**알고리즘**
```
1. 해쉬 맵
```

### **다른 풀이**

```python
import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = tuple(map(sorted, zip(*arr)))

AB = [a+b for a in arr[0] for b in arr[1]]
CD = [c+d for c in arr[2] for d in arr[3]]
AB.sort()
CD.sort()
count = 0

i, j = 0, len(CD)-1
while i<len(AB) and j >= 0:
    if (sumval := AB[i]+CD[j]) == 0:
        ni, nj = i+1, j-1
        while ni < len(AB) and AB[i] == AB[ni]:
            ni += 1
        while nj >= 0 and CD[j] == CD[nj]:
            nj -= 1
        count += (ni-i)*(j-nj)
        i, j = ni, nj
    elif sumval < 0:
        i += 1
    else:
        j -= 1
print(count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pieces98|636868|3688|PyPy3|635
#### **📝해설**

```python
import sys
from collections import defaultdict

# 입력받기
N = int(sys.stdin.readline().rstrip())
arr = [list(x) for x in zip(*(map(int, sys.stdin.readline().rstrip().split()) for _ in range(N)))]

# AB배열의 합을 딕셔너리에 저장
sum_AB = defaultdict(int)

# A, B배열의 모든 가능한 합을 저장
for a in arr[0]:
    for b in arr[1]:
        sum_AB[a+b] += 1

# 합이 0이 되는 개수
count = 0

# CB의 합을 모두 구함
for c in arr[2]:
    for d in arr[3]:
        target = -(c + d)

        # 미리 구해둔 AB의 합과 더해서 0이 된다면
        if target in sum_AB:

            # 개수를 더함
            count += sum_AB[target]

print(count)
```