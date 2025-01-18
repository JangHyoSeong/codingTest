# [9019] DSLR

### **난이도**
골드 4
## **📝문제**
네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 이 계산기에는 레지스터가 하나 있는데, 이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다. 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다. n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

1. D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
2. S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
3. L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
4. R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.  
위에서 언급한 것처럼, L 과 R 명령어는 십진 자릿수를 가정하고 연산을 수행한다. 예를 들어서 n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123 이 된다.

여러분이 작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다. 예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.

1234 →L 2341 →L 3412
1234 →R 4123 →R 3412

따라서 여러분의 프로그램은 이 경우에 LL 이나 RR 을 출력해야 한다.

n의 자릿수로 0 이 포함된 경우에 주의해야 한다. 예를 들어서 1000 에 L 을 적용하면 0001 이 되므로 결과는 1 이 된다. 그러나 R 을 적용하면 0100 이 되므로 결과는 100 이 된다.
### **입력**
프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.
### **출력**
A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.
### **예제입출력**

**예제 입력1**

```
3
1234 3412
1000 1
1 16
```

**예제 출력1**

```
LL
L
DDDD
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())
for testcase in range(T):
    a, b = map(int, input().split())
    
    q = deque([(a, "")])
    visited = set()
    visited.add(a)

    while q:
        num, cmd = q.popleft()

        if num == b:
            print(cmd)
            break
        
        D = (num * 2) % 10000
        S = 9999 if num == 0 else num - 1
        L = (num % 1000) * 10 + (num // 1000)
        R = (num % 10) * 1000 + (num // 10)

        for next_num, command in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            if next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cmd + command))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|213624|10652|PyPy3|664
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
def sol(start, end):
    dp = [0] * L

    def bfs():
        dp[start] = 1
        dp[end] = -1
        queue_for = [start]
        queue_rev = [end]

        for i, j in zip(range(2, 5000), range(-2, -5000, -1)):
            queue2_for = []
            for q in queue_for:
                for k in path_for[q]:
                    if not dp[k]:
                        dp[k] = i
                        queue2_for.append(k)
                    
                    elif dp[k] < 0: return i-1, j+2, k               
            
            queue_for = queue2_for

            queue2_rev = []
            for q in queue_rev:
                for k in path_rev[q]:
                    if not dp[k]:
                        dp[k] = j
                        queue2_rev.append(k)

                    elif dp[k] > 0: return i-1, j+1, k       
            
            queue_rev = queue2_rev

    i, j, k = bfs()
    # 최단 경로 역추적
    answer = [None] * (i-j)

    a = k
    for b in range(i, 0, -1):
        for char, c in zip(('S', 'L', 'R', 'D', 'D'), path_rev[a]):
            if dp[c] == b:
                answer[b-1] = char
                a = c
                break
    
    a = k
    for b in range(j, 0):
        for char, c in zip(('S', 'L', 'R', 'D'), path_for[a]):
            if dp[c] == b:
                answer[b] = char
                a = c
                break
    
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())
L = 10000
path_for = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
path_rev = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ppllaall02|36504|652|Python3|1910
#### **📝해설**

```python
from collections import deque

T = int(input())
for testcase in range(T):
    a, b = map(int, input().split())
    
    # 처음 숫자와, 그걸 만들때까지의 명령어를 큐에 삽입
    q = deque([(a, "")])

    # 이미 만들었던 숫자를 저장할 세트
    visited = set()
    visited.add(a)

    # BFS
    while q:
        num, cmd = q.popleft()

        if num == b:
            print(cmd)
            break
        
        D = (num * 2) % 10000
        S = 9999 if num == 0 else num - 1
        L = (num % 1000) * 10 + (num // 1000)
        R = (num % 10) * 1000 + (num // 10)

        # 다음에 만들 숫자를 탐색
        for next_num, command in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            if next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cmd + command))
```