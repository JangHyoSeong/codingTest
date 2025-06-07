# [11729] 하노이 탑 이동 순서

### **난이도**
골드 5
## **📝문제**
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11729/hanoi.png)

### **입력**
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.
### **출력**
첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
### **예제입출력**

**예제 입력1**

```
3
```

**예제 출력1**

```
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

moves = []
def hanoi(n, start, end, temp):
    if n == 1:
        moves.append((start, end))
        return
    
    hanoi(n-1, start, temp, end)
    moves.append((start, end))
    hanoi(n-1, temp, end, start)

hanoi(N, 1, 3, 2)
print(len(moves))
for move in moves:
    print(" ".join(map(str, move)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|107220|1132|Python3|319
#### **📝해설**

**알고리즘**
```
1. 재귀
```

### **다른 풀이**

```python
import sys

def hanoi(i, s, e, v):
    k = (i, s, e, v)
    if k in memo: return memo[k]
    if i == 1: return f'{s} {e}'
    res = '\n'.join([hanoi(i - 1, s, v, e), f'{s} {e}', hanoi(i - 1, v, e, s)])
    memo[k] = res
    return res

n = int(sys.stdin.readline())
memo = dict()
print((1 << n) - 1)
print(hanoi(n, 1, 3, 2))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|49996|44|Python3|324
#### **📝해설**

```python
N = int(input())

# 이동을 담을 리스트
moves = []

# 재귀적으로 호출되며 하노이탑 이동을 함
def hanoi(n, start, end, temp): # 현재 단계, 시작위치, 옮길위치, 나머지 위치

    # 1칸이라면, 그냥 옮김
    if n == 1:
        moves.append((start, end))
        return
    
    # N-1개 이동
    hanoi(n-1, start, temp, end)

    # 가장 큰 원판 이동
    moves.append((start, end))

    # 나머지를 목적지로 이동
    hanoi(n-1, temp, end, start)

# 시작
hanoi(N, 1, 3, 2)
print(len(moves))
for move in moves:
    print(" ".join(map(str, move)))
```