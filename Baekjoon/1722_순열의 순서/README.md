# [1722] 순열의 순서

### **난이도**
골드 5
## **📝문제**
1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.

임의의 순열은 정렬을 할 수 있다. 예를 들어  N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다. 첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이….

N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄의 첫 번째 수는 소문제 번호이다. 1인 경우 k(1 ≤ k ≤ N!)를 입력받고, 2인 경우 임의의 순열을 나타내는 N개의 수를 입력받는다. N개의 수에는 1부터 N까지의 정수가 한 번씩만 나타난다.
### **출력**
k번째 수열을 나타내는 N개의 수를 출력하거나, 몇 번째 수열인지를 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
4
1 3
```

**예제 출력1**

```
1 3 2 4
```

**예제 입력2**

```
4
2 1 3 2 4
```

**예제 출력2**

```
3
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from math import factorial

N = int(input())
k, *arr = map(int, input().split())

if k == 1:
    c = arr[0] - 1
    result = []
    numbers = list(range(1, N + 1))

    for i in range(N):
        fact = factorial(N - 1 - i)
        idx = c // fact
        result.append(numbers[idx])
        numbers.pop(idx)
        c %= fact

    print(*result)

else:
    perm = arr
    count = 0
    numbers = list(range(1, N + 1))

    for i in range(N):
        idx = numbers.index(perm[i])
        count += idx * factorial(N - 1 - i)
        numbers.pop(idx)

    print(count + 1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34536|36|Python3|570
#### **📝해설**

**알고리즘**
```
1. 수학
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N = int(input())
c = list(map(int, input().split()))

def fact(i):
    if i <= 1:
        return 1
    else:
        return i * fact(i-1)

if c[0] == 1:
    k = c[1] - 1
    num = list(range(1,N+1))
    tmp = []

    while N > 0:
        f = fact(N-1)
        idx = k // f
        tmp.append(num.pop(idx))
        k %= f
        N -= 1
    print(" ".join(map(str, tmp)))

elif c[0] == 2:
    data = c[1:]
    num = list(range(1, N+1))
    rs = 0

    for i in range(N):
        f = fact(N-i-1)
        idx = num.index(data[i])
        rs += idx * f
        num.pop(idx)
    print(rs + 1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
heo9290|31120|32|Pyuthon3|626
#### **📝해설**

```python
from math import factorial

N = int(input())
k, *arr = map(int, input().split())

# K가 1인경우 arr[0]번째 찾기
if k == 1:
    # 인덱싱을 위해 arr[0]--
    c = arr[0] - 1

    # 결과로 출력할 순열
    result = []
    numbers = list(range(1, N + 1))

    # N번 반복하면서
    for i in range(N):

        # 예를 들어 시작이 10으로 시작한다면 그때까지의 인덱스는 10!
        # 각 자릿수의 팩토리얼을 더하면서 해당 순열을 찾음
        fact = factorial(N - 1 - i)
        idx = c // fact
        result.append(numbers[idx])
        numbers.pop(idx)
        c %= fact

    print(*result)

# 해당 순열이 몇번째인지 찾기
else:
    perm = arr
    count = 0
    numbers = list(range(1, N + 1))

    # 팩토리얼을 통해 찾음
    for i in range(N):
        idx = numbers.index(perm[i])
        count += idx * factorial(N - 1 - i)
        numbers.pop(idx)

    print(count + 1)
```