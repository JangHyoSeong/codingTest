# [4948] 베르트랑 공준

### **난이도**
실버 2
## **📝문제**
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
### **입력**
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.
### **출력**
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
1
10
13
100
1000
10000
100000
0
```

**예제 출력1**

```
1
4
3
21
135
1033
8392
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
numbers = []

while True:
    N = int(input())
    if N == 0:
        break

    numbers.append(N)

max_num = max(numbers)

size = 2 * max_num + 1
is_prime = [True] * size
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(size ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, size, i):
            is_prime[j] = False

for n in numbers:
    count = sum(1 for i in range(n+1, 2*n + 1) if is_prime[i])
    print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34340|292|Python3|443
#### **📝해설**

**알고리즘**
```
1. 소수
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

""" Sieve of Eratosthenes """
# soe = [True]*246913
# for i in range(2, 497): # sqrt(246913) \approx 496.90
#     if soe[i]:
#         j = 2
#         while i*j <= 246912:
#             soe[i*j] = False
#             j += 1

""" imporved Sieve of Eratosthenes"""
soe = [True]*246913
for i in range(3, 497, 2):
    if soe[i]: soe[i*i::2*i] = [False]*len(soe[i*i::2*i])


""" Solution 1) naive O(k) """
# while 1:
#     n = int(input())
#     if not n: break
    
#     cnt = 0
#     for i in range(n+1, 2*n+1):
#         if soe[i]: cnt += 1
#     print(str(cnt)+'\n')

""" Solution 2) O(n)으로 primes 구해놓고, bs 2번 """
def bs_lb(a, v):
    lo, hi = 0, len(a)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if a[mid] < v:
            lo = mid+1
        else:
            hi = mid-1

    return lo

def bs_ub(a, v):
    lo, hi = 0, len(a)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if a[mid] <= v:
            lo = mid+1
        else:
            hi = mid-1

    return lo

primes = [2] + [i for i in range(3, 246913, 2) if soe[i]]

while 1:
    n = int(input())
    if not n: break
    print(str(bs_ub(primes, 2*n) - bs_lb(primes, n+1))+'\n')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|33688|40|Python3|1230
#### **📝해설**

```python
numbers = []

# 입력받기
while True:
    N = int(input())
    if N == 0:
        break

    numbers.append(N)

# 최대값 기준으로 소수를 모두 구함
max_num = max(numbers)

# 2n까지 구해야해서 사이즈 설정
size = 2 * max_num + 1

# 일단 모두 소수라고 가정
is_prime = [True] * size

# 초기값
is_prime[0] = False
is_prime[1] = False

# 2부터, sqrt(2n)까지
for i in range(2, int(size ** 0.5) + 1):

    # 소수라면
    if is_prime[i]:

        # 자신의 배수를 모두 소수가 아니라고 설정
        for j in range(i * i, size, i):
            is_prime[j] = False

# 결과 출력
for n in numbers:
    count = sum(1 for i in range(n+1, 2*n + 1) if is_prime[i])
    print(count)
```