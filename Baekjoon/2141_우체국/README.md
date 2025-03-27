# [2141] 우체국

### **난이도**
골드 4
## **📝문제**
수직선과 같은 일직선상에 N개의 마을이 위치해 있다. i번째 마을은 X[i]에 위치해 있으며, A[i]명의 사람이 살고 있다.

이 마을들을 위해서 우체국을 하나 세우려고 하는데, 그 위치를 어느 곳으로 할지를 현재 고민 중이다. 고민 끝에 나라에서는 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정하였다. 우체국을 세울 위치를 구하는 프로그램을 작성하시오.

각 마을까지의 거리의 합이 아니라, 각 사람까지의 거리의 합임에 유의한다
### **입력**
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 X[1], A[1], X[2], A[2], …, X[N], A[N]이 주어진다. 범위는 |X[i]| ≤ 1,000,000,000, 1 ≤ A[i] ≤ 1,000,000,000 이며 모든 입력은 정수이다.
### **출력**
첫째 줄에 우체국의 위치를 출력한다. 가능한 경우가 여러 가지인 경우에는 더 작은 위치를 출력하도록 한다.
### **예제입출력**

**예제 입력1**

```
3
1 3
2 5
3 3
```

**예제 출력1**

```
2
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

towns.sort(key=lambda x : x[0])

total_population = sum(town[1] for town in towns)

current_population = 0
for town in towns:
    current_population += town[1]
    if current_population >= (total_population + 1) // 2:
        print(town[0])
        break
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121952|228|PyPy3|388
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```
### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    villages = []
    cnt = 0
    for _ in range(N):
        x, a = map(int, input().split())
        villages.append((x, a))
        cnt += a
    villages.sort(key=lambda y: y[0])
    if cnt%2:
        cnt = cnt//2+1
    else:
        cnt //= 2
    for x, a in villages:
        cnt -= a
        if cnt <= 0:
            print(x)
            return

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|45756|156|Python3|438
#### **📝해설**

```python
import sys

# 입력받기
N = int(sys.stdin.readline().rstrip())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 마을의 위치 기준으로 오름차순 정렬
towns.sort(key=lambda x : x[0])

# 마을의 인구 총 합
total_population = sum(town[1] for town in towns)

# 마을을 순회하면서 현재까지의 인구 총 합
current_population = 0

'''
총 인구수가 N이라 할 때 인구수의 합이 (N+1) // 2인 마을의 위치가 항상 최적이 된다
'''
for town in towns:
    current_population += town[1]
    if current_population >= (total_population + 1) // 2:
        print(town[0])
        break
```