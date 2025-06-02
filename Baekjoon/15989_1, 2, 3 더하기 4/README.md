# [15989] 1, 2, 3 더하기 4

### **난이도**
골드 5
## **📝문제**
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

- 1+1+1+1
- 2+1+1 (1+1+2, 1+2+1)
- 2+2
- 1+3 (3+1)  
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 10,000보다 작거나 같다.
### **출력**
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
4
7
10
```

**예제 출력1**

```
4
8
14
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

dp_len = max(arr)
dp = [0] * (dp_len + 1)

dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, dp_len + 1):
        dp[i] += dp[i - num]

for n in arr:
    print(dp[n])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|40|Python3|286
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

t = int(input())

dp = [1]*10001

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3,10001):
    dp[i] += dp[i-3]

for i in range(t):
    print(dp[int(input())])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ironee1|31120|32|Python3|214
#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

# 입력받은 N중에 최대값을 DP배열의 길이로 정의
dp_len = max(arr)
dp = [0] * (dp_len + 1)

# 0을 만드는 경우의 수는 1
dp[0] = 1

# 각 경우의 수에서 1, 2, 3을 더하는 경우의 수를 구함
for num in [1, 2, 3]:
    for i in range(num, dp_len + 1):
        dp[i] += dp[i - num]

for n in arr:
    print(dp[n])
```