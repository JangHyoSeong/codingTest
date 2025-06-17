# [2217] 로프

### **난이도**
실버 4
## **📝문제**
N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
### **입력**
첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
### **출력**
첫째 줄에 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
10
15
```

**예제 출력1**

```
20
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

arr.sort(reverse=True)

max_weight = 0
for i in range(N):
    weight = arr[i] * (i + 1)
    max_weight = max(max_weight, weight)

print(max_weight)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36264|112|Python3|260
#### **📝해설**

**알고리즘**
```
1. 정렬
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import io, os

def main():
    input = io.BufferedReader(io.FileIO(0), buffer_size=1 << 18).readline
    N = int(input())
    cnt = [0] * 10001
    for _ in range(N):
        cnt[int(input())] += 1
    i = 0
    print(max([ai * (i := i + cnt[ai]) for ai in range(10000, 0, -1)]), flush=True)
    os._exit(0)

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|31120|48|Python3|315
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 내림차순으로 정렬
arr.sort(reverse=True)

# 최대 무게
max_weight = 0

# 내림차순으로 순회하면서
for i in range(N):

    # 가장 하중부담이 낮은 로프 * 현재까지 로프의 개수 => 현재까지 기준 최대중량
    weight = arr[i] * (i + 1)

    # 최대 중량을 갱신
    max_weight = max(max_weight, weight)

print(max_weight)
```