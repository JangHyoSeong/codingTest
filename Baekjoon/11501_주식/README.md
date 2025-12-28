# [11501] 주식

### **난이도**
실버 2
## **📝문제**
홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.
### **입력**
입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.
### **출력**
각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.
### **예제입출력**

**예제 입력1**

```
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
```

**예제 출력1**

```
0
10
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    prices = list(map(int, sys.stdin.readline().rstrip().split()))

    max_price = 0
    profit = 0

    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        
        else:
            profit += max_price - prices[i]
    
    print(profit)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|338420|1256|PyPy3|412
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
# 백준 11501

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    prevMax = A[N-1]
    total = 0
    for i in range(N-2, -1, -1):
        if prevMax > A[i]:
            total += prevMax - A[i]
        else:
            prevMax = A[i]

    return total


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(solve(N, A))


main()

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jkyungho07|328920|904|PyPy3|455
#### **📝해설**

```python
import sys

# 입력받기
T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    prices = list(map(int, sys.stdin.readline().rstrip().split()))

    # 뒤에서부터 순회했을 때, 최대값
    max_price = 0
    # 이득
    profit = 0

    # 뒤에서부터 순회
    for i in range(N-1, -1, -1):

        # 최대값이 갱신이 가능하다면 갱신
        if prices[i] > max_price:
            max_price = prices[i]
        
        # 최대값이 아니라면, 현재 가격을 최대값에 판다고 생각하고 이득을 증가
        else:
            profit += max_price - prices[i]
    
    print(profit)
```