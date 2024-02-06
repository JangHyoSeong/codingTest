# [1929] 소수 구하기

### **난이도**
실버 3
## **📝문제**

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

### **입력**
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
### **출력**
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 16
```

**예제 출력1**

```
3
5
7
11
13
```

### **출처**

## **🧐CODE REVIEW**

### **😫나의 오답 풀이**
- 시간 초과를 해결하기 위해 시간 복잡도를 최대한 줄임
### **🧾나의 풀이**

```python
from math import sqrt

def primeNumber(M, N):

    numbers = [1 for _ in range(0, N+1)]

    numbers[0] = 0
    numbers[1] = 0

    prime = 2
    while prime <= sqrt(N):
        if numbers[prime] == 0:
            prime += 1
            continue

        for idx in range(prime*prime, N+1):
            if idx % prime == 0:
                numbers[idx] = 0
        prime += 1

    for i in range(N+1):
        if i >= M and numbers[i] == 1:
            print(i)

M, N = map(int, input().split())
primeNumber(M, N)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|118080|2144|PyPy3|513
#### **📝해설**

**알고리즘**
```
1. 에라토스테네스의 체
2. 소수 판별
```
최대한 범위를 줄이기 위해 반복을 N의 제곱근까지 진행하였고, 또한 prime*prime을 시작점으로 두어 소수를 판별하였다.

#### **😅개선점**

1. 현재는 단순히 값을 0으로 바꾸어 판별하기 때문에, 소수가 아닌 수를 계속 순회한다
    - 따라서 LinkedList 등으로 구현하면 조금 더 실행시간을 줄일 수 있을 것

### **다른 풀이**

```python
import math


def eratosthenes_sieve(m, n):
    n += 1  # 범위를 m에서 n까지 포함하도록 n에 1을 더함

    # 처음에는 모든 숫자가 소수라고 가정하고, 리스트의 모든 원소를 True로 설정
    sieve = [True] * n

    # 3부터 n의 제곱근까지의 모든 숫자를 확인
    # 소수의 배수는 소수가 아니므로 해당 숫자의 배수들을 모두 False로 설정
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

        # 리스트에서 True로 남아있는 숫자들을 소수로 간주하고 이들을 모두 찾음
    # 그 중에서 m 이상인 숫자들만 선택
    primes = [a for a in range(3, n, 2) if sieve[a] and a >= m]

    # m이 2 이하인 경우 2를 소수 목록에 추가
    if m <= 2: primes = [2] + primes
    return primes  # 소수 목록을 반환


m, n = map(int, input().split())  # m과 n을 입력받음
prime_numbers = eratosthenes_sieve(m, n)  # m과 n 사이의 모든 소수를 찾음

# 찾은 소수들을 모두 출력
for prime in prime_numbers:
    print(prime)
```

아이디 |	문제	| 문제 제목 |	결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:---------:|:-----:|:-----:|:-----:|:----:|:--------:
eon8718|1929|소수 구하기|정답|44636|116|Python3|1151

### **🔖정리**

1. 에라토스테네스의 체가 무엇인지 알 수 있었다.
