# [2003] 수들의 합 2

### **난이도**
실버 4
## **📝문제**
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
### **출력**
첫째 줄에 경우의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
4 2
1 1 1 1
```

**예제 출력1**

```
3
```

**예제 입력2**

```
10 5
1 2 3 4 2 5 3 1 1 2
```

**예제 출력2**

```
3
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

left, right = 0, 1

count = 0
while right <= N:
    now_sum = prefix_sum[right] - prefix_sum[left]
    if now_sum == M:
        count += 1
        right += 1
        left += 1
    
    elif now_sum < M:
        right += 1
    
    else:
        left += 1
    
print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|40|Python3|490
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 누적합을 미리 계산
prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

# 투 포인터 설정
left, right = 0, 1

count = 0

# 인덱스를 벗어나기 전까지 확인
while right <= N:

    # 현재 구간의 합
    now_sum = prefix_sum[right] - prefix_sum[left]

    # 정확히 M이라면 정답 갯수를 더하고, 포인터를 각각 옆으로 이동
    if now_sum == M:
        count += 1
        right += 1
        left += 1
    
    # 작다면, 오른쪽 포인터만 이동
    elif now_sum < M:
        right += 1
    
    # 크다면 왼쪽 포인터만 이동
    else:
        left += 1
    
print(count)
```