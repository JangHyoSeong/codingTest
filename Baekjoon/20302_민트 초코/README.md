# [20302] 민트 초코

### **난이도**
골드 4
## **📝문제**
상원이는 아주 특별한 방법으로 디저트를 고른다.

상원이는 정수의 곱셈과 나눗셈으로만 이뤄진 임의의 수식을 적고, 그 결과가 정수이면 “민트 초코”를, 정수가 아닌 유리수이면 “치약”을 먹기로 했다.

상원이가 적은 수식이 주어졌을 때, 어떤 디저트를 먹게 될지 맞혀보자.
### **입력**
첫째 줄에 수식을 이루는 수의 개수 
$N$이 주어진다. (
$1 \leq N \leq 100\ 000$)

둘째 줄에 수식이 주어진다. 수식은 정수와 연산자(*, /)가 공백으로 구분되어 주어진다. 수식은 정수와 연산자가 번갈아 주어지며, 항상 정수로 시작해서 정수로 끝난다. 수식을 이루는 모든 정수는 
$-100\ 000$ 이상 
$100\ 000$ 이하이다.

올바른 수식만 주어지고, 
$0$으로 나누는 경우는 주어지지 않는다.
### **출력**
상원이가 고른 디저트가 “민트 초코”인 경우 mint chocolate, “치약”인 경우 toothpaste를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
1 * 2 / 3 / 4 * 5 * 6
```

**예제 출력1**

```
mint chocolate
```

**예제 입력2**

```
6
1 * 2 / 3 / 4 / 5 * 6
```

**예제 출력2**

```
toothpaste
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().split())

factor_count = defaultdict(int)

def factorize(x, sign):
    x = abs(x)
    if x <= 1:
        return
    d = 2
    while d * d <= x:
        while x % d == 0:
            factor_count[d] += sign
            x //= d
        d += 1
    if x > 1:
        factor_count[x] += sign

first = int(arr[0])
if first == 0:
    print("mint chocolate")
    exit()

factorize(first, 1)

for i in range(1, len(arr), 2):
    op = arr[i]
    num = int(arr[i + 1])

    if op == "*":
        if num == 0:
            print("mint chocolate")
            exit()
        factorize(num, 1)
    else:
        factorize(num, -1)

for v in factor_count.values():
    if v < 0:
        print("toothpaste")
        break
else:
    print("mint chocolate")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|131820|496|PyPy3|858
#### **📝해설**

**알고리즘**
```
1. 소수
2. 수학
```

### **다른 풀이**

```python
max_num = 100001
sp = [0] * (max_num + 1)
primes = []
for i in range(2, max_num + 1):
    if sp[i] == 0:
        sp[i] = i
        primes.append(i)
        
    j = 0
    while j < len(primes) and i * primes[j] <= max_num and primes[j] <= sp[i]:
        sp[i * primes[j]] = primes[j]
        j += 1

n = int(input())
li = input().split()

ct = [0] * 100001

is_zero = False

v = abs(int(li[0]))
if v == 0:
    is_zero = True
while v > 1:
    ct[sp[v]] += 1
    v //= sp[v]

for i in range(1, len(li), 2):
    v = abs(int(li[i + 1]))
    is_div = li[i] == '/'
    
    if v == 0:
        is_zero = True
        break
        
    while v > 1:
        ct[sp[v]] += 1 - 2 * is_div
        v //= sp[v]
        
if is_zero:
    print('mint chocolate')
else:
    ip = True
    for p in primes:
        if ct[p] < 0:
            ip = False
            break
            
    if ip:
        print('mint chocolate')
    else:
        print('toothpaste')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hsh8086|139236|180|PyPy3|944
#### **📝해설**

```python
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().split())

# 현재 수를 소인수분해 했을 때 각 소수의 갯수
factor_count = defaultdict(int)

# 소인수분해 (x: 수, sign: 곱하기면 1, 나누기면 -1)
def factorize(x, sign):

    # 1 이하면 그대로
    x = abs(x)
    if x <= 1:
        return

    # 소인수분해 알고리즘
    d = 2
    while d * d <= x:
        while x % d == 0:
            factor_count[d] += sign
            x //= d
        d += 1
    if x > 1:
        factor_count[x] += sign

# 첫번째 수
first = int(arr[0])

# 0으로 시작하면 무조건 정수
if first == 0:
    print("mint chocolate")
    exit()

factorize(first, 1)

# 이후 소인수분해
for i in range(1, len(arr), 2):
    op = arr[i]
    num = int(arr[i + 1])

    if op == "*":
        # 0이면 앞으로도 계속 0
        if num == 0:
            print("mint chocolate")
            exit()
        factorize(num, 1)
    else:
        factorize(num, -1)

# 소인수 분해 했을 때, 한 값이 음수가 있다면 정수가 아님
for v in factor_count.values():
    if v < 0:
        print("toothpaste")
        break
else:
    print("mint chocolate")

```