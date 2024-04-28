# [13975] 파일 합치기 3

### **난이도**
골드 4
## **📝문제**
소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다. 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다. 이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, C1, C2, C3, C4가 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이때 비용 60이 필요하다. 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 다른 방법으로 파일을 합치면 비용을 줄일 수 있다. 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이때 필요한 총 비용은 70+80+150=300 이다.

소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.
### **입력**
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데, T는 입력의 맨 첫 줄에 주어진다.각 테스트 데이터는 두 개의 행으로 주어지는데, 첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 1,000,000)가 주어진다. 두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다. 파일의 크기는 10,000을 초과하지 않는다.
### **출력**
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행에 출력하는데, 모든 장을 합치는데 필요한 최소비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
```

**예제 출력1**

```
300
826
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

T = int(input())

for testcase in range(T):
    N = int(input())
    files = list(map(int, input().split()))

    cost = 0
    pq = []
    for i in range(N):
        heappush(pq, files[i])

    i = N-1
    while i > 0:
        a, b = heappop(pq), heappop(pq)
        new_file = a+b
        heappush(pq, new_file)
        cost += new_file
        i -= 1

    print(cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|263108|2460|PyPy3|406
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

from collections import deque

def get_ints():
    return map(int, input().split())

def get_strs():
    return input().split()

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        test_list = sorted(get_ints())
        left = deque(test_list)
        right = deque()
        total = 0
        for _ in range(K - 1):
            sum_ = 0
            for _ in range(2):
                if not left:
                    sum_ += right.popleft()
                elif not right:
                    sum_ += left.popleft()
                else:
                    if left[0] > right[0]:
                        sum_ += right.popleft()
                    else:
                        sum_ += left.popleft()
            right.append(sum_)
            total += sum_
        print(total)
        

if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
eypk5683|283568|996|PyPy3|904
#### **📝해설**

```python
from heapq import heappush, heappop

# 테스트케이스 개수 입력받음
T = int(input())

for testcase in range(T):
    # 입력받음
    N = int(input())
    files = list(map(int, input().split()))

    # 파일 합치는 비용
    cost = 0

    '''
    파이썬은 내장 모듈로 heap이 존재한다
    heappush, heappop을 통해 우선순위 큐를 구현할 수 있다

    이 문제에서 우선순위 큐를 사용해야 하는 이유
    파일을 합칠 때 작은 파일부터 순서대로 합치는 것이 최소값을 구하는 방법이다
    그렇기에 파일을 합친 후에 새로 생성된 파일의 크기 또한, 원래 파일과 비교해서
    우선순위 큐에 넣어야한다. 이를 위해 힙을 사용한다
    '''

    # 우선순위 큐로 사용할 pq. (힙)
    pq = []
    
    # 힙에 모든 파일들을 삽입한다
    for i in range(N):
        heappush(pq, files[i])

    # 파일의 개수. 모든 파일이 합쳐질 때까지 반복
    i = N-1
    while i > 0:

        # 파일 두개를 힙에서 빼낸다 (가장 작은 수 2개)
        a, b = heappop(pq), heappop(pq)

        # 새로운 파일을 만들고 heap에 push한다
        new_file = a+b
        heappush(pq, new_file)

        # 파일 합치는 비용을 더해주고, 파일 2개가 1개가 됐으므로 인덱스를 1 감소시킨다
        cost += new_file
        i -= 1

    print(cost)
```