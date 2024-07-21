# [25200] 곰곰이와 자판기

### **난이도**
플래티넘 5
## **📝문제**
곰곰이는 좋아하는 음료수 자판기가 있다. 이 자판기에는 "랜덤" 버튼이 있는데, 이 버튼을 누르면 이세계에서 출발한 음료수가 
$M$ 번의 차원 이동 후 자판기 상품 출구로 떨어진다.

하지만 차원 이동은 불안정하기 때문에, 음료수 종류가 도중에 바뀌는 일도 있다. 정확히는 아래와 같은 규칙에 의해 바뀐다.

 
$i\ (1 \le i \le M)$ 번째 차원 이동 중에, 음료수 종류 
$U_i$ 는 
$V_i$ 로 변경된다. 
$(1 \le U_i, V_i \le N)$ 
곰곰이는 
$1$ 부터 
$N$ 까지 모든 종류의 음료수에 대해, 각각 
$M$ 번의 차원 이동을 거쳐 최종적으로 어떤 종류의 음료수가 되는지 알고 싶다.
### **입력**
첫 번째 줄에 음료수의 종류 개수 
$N$, 차원 이동 횟수 
$M$ 이 공백을 사이에 두고 주어진다. 
$(2 \le N, M \le 300\,000)$ 

두 번째 줄부터 
$M$개의 줄에 걸쳐 정수 
$U_i, V_i$ 가 공백을 사이에 두고 주어진다. 
$(1 \le i \le M,\ 1 \le U_i, V_i \le N,\ U_i \ne V_i)$ 
### **출력**
$f(k)$ 가 음료수 종류 
$k$ 가 
$M$ 번의 차원 이동을 거쳐 최종적으로 변하는 음료수 종류라고 할 때, 
$f(1), f(2), \cdots, f(N)$ 을 첫 번째 줄에 공백을 사이에 두고 출력하라.
### **예제입출력**

**예제 입력1**

```
5 4
1 3
3 2
4 3
2 4
```

**예제 출력1**

```
4 4 4 3 5
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from sys import stdin

N, M = map(int, stdin.readline().strip().split())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

result = list(range(N+1))

for a, b in reversed(arr):
    result[a] = result[b]

result = result[1:]
print(" ".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|126528|632|Python3|283
#### **📝해설**

**알고리즘**
```
1. 자료구조
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

drink = list(range(N + 1))

U, V = [], []
for _ in range(M):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)

for i in range(M - 1, -1, -1):
    drink[U[i]] = drink[V[i]]

print(*drink[1:])

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
oh040411|155780|324|PyPy3|284
#### **📝해설**

```python
from sys import stdin

N, M = map(int, stdin.readline().strip().split())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

result = list(range(N+1))

for a, b in reversed(arr):
    result[a] = result[b]

result = result[1:]
print(" ".join(map(str, result)))
```