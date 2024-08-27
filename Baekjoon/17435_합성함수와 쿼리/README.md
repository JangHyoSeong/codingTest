# [17435] 합성함수와 쿼리

### **난이도**
골드 1
## **📝문제**
함수 f : {1, 2, ..., m}→{1, 2, ..., m}이 있다. 이때 fn : {1, 2, ..., m}→{1, 2, ..., m}을 다음과 같이 정의하자.

- f1(x) = f(x)
- fn+1(x) = f(fn(x))  
예를 들어 f4(1) = f(f(f(f(1))))이다.

n과 x가 주어질 때 fn(x)를 계산하는 쿼리를 수행하는 프로그램을 작성하시오.
### **입력**
첫 줄에 정수 m이 주어진다. (1 ≤ m ≤ 200,000)

다음 줄에 f(1), f(2), ..., f(m)이 차례대로 주어진다.

다음 줄에 쿼리의 개수 Q가 주어진다. (1 ≤ Q ≤ 200,000)

다음 Q개의 줄에 각각 정수 n과 x가 주어진다. (1 ≤ n ≤ 500,000; 1 ≤ x ≤ m)
### **출력**
주어지는 n, x마다 fn(x)를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
3 3 5 4 3
5
1 1
2 1
11 3
1000 4
5 1
```

**예제 출력1**

```
3
5
5
4
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from math import log2

m = int(input())
arr = [0] + list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]


LOG_K = int(log2(500000))
table = [[0] * (m+1) for _ in range(LOG_K + 1)]

for i in range(1, m+1):
    table[0][i] = arr[i]

for k in range(1, LOG_K+1):
    for i in range(1, m+1):
        temp = table[k-1][i]
        table[k][i] = table[k-1][temp]


for query in queries:
    count, cur = query
    temp_log = int(log2(count)) + 1

    idx = 0
    while idx < temp_log:
        if count % 2:
            cur = table[idx][cur]
        idx += 1
        count //= 2

    print(cur)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|174468|644|PyPy3|644
#### **📝해설**

**알고리즘**
```
1. 희소 배열 (Sparse Table)
```

### **다른 풀이**

```python
import io, os, sys


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    _ = input()
    arr = list(map(int, input().split()))
    arr = [x - 1 for x in arr]

    arrs = [arr]
    k = 1
    while k <= 500000:
        now = arrs[-1]
        now = [now[x] for x in now]
        arrs.append(now)
        k *= 2

    results = []

    for _ in range(int(input())):
        n, x = map(int, input().split())
        x -= 1
        for i in range(0, len(arrs)):
            if n & 1:
                x = arrs[i][x]
            n >>= 1
            if n == 0:
                break
        x += 1
        results.append(x)

    print("\n".join(map(str, results)))


sys.exit(main())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|173356|372|PyPy3|704
#### **📝해설**

```python
from math import log2

m = int(input())
arr = [0] + list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

# 2의 배수를 기준으로 2^k번 이동했을 때 도착하는 노드를 저장
LOG_K = int(log2(500000))
table = [[0] * (m+1) for _ in range(LOG_K + 1)]

for i in range(1, m+1):
    table[0][i] = arr[i]

for k in range(1, LOG_K+1):
    for i in range(1, m+1):
        temp = table[k-1][i]
        table[k][i] = table[k-1][temp]

# table을 기준으로 도착 노드를 찾음
for query in queries:
    count, cur = query
    temp_log = int(log2(count)) + 1

    idx = 0
    while idx < temp_log:
        if count % 2:
            cur = table[idx][cur]
        idx += 1
        count //= 2

    print(cur)
```

### **참고 사이트**

- [Sparse Table](https://namnamseo.tistory.com/entry/Sparse-Table)