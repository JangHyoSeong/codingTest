# [1806] 부분합

### **난이도**
골드 4
## **📝문제**
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.
### **출력**
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
10 15
5 1 3 5 10 7 4 9 2 8
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

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N + 1)
prefix_sum[1] = arr[0]
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

left, right = 0, N-1
for i in range(1, N+1):
    if prefix_sum[i] >= S:
        right = i
        break
else:
    print(0)
    exit()

left = 0
min_length = N
while right <= N and left < right:
    if prefix_sum[right] - prefix_sum[left] >= S:
        min_length = min(min_length, right - left)
        left += 1
    else:
        right += 1

print(min_length)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42168|132|Python3|610
#### **📝해설**

**알고리즘**
```
1. 누적 합
2. 투 포인터
```

### **다른 풀이**

```python
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

min_length = N + 1
current_sum = 0
left = 0

for right in range(N):
    current_sum += arr[right]

    while current_sum >= S:
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_length == N + 1:
    print(0)
else:
    print(min_length)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wkdgyutmd200|42168|100|Python3|408
#### **📝해설**

```python
import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 배열의 누적합을 미리 계산
prefix_sum = [0] * (N + 1)
prefix_sum[1] = arr[0]
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

# 투 포인터 설정
left, right = 0, N-1
for i in range(1, N+1):

    # 처음으로 총합이 S를 넘을 때 인덱스를 오른쪽 인덱스로 저장
    if prefix_sum[i] >= S:
        right = i
        break

# S 이상인 배열이 없다면, 0을 출력하고 종료
else:
    print(0)
    exit()

# 최소 길이를 설정하고, 투 포인터가 만나기 전까지, 혹은 배열을 모두 탐색하기 전까지 반복
left = 0
min_length = N
while right <= N and left < right:

    # S 이상인 경우, left를 증가
    if prefix_sum[right] - prefix_sum[left] >= S:
        min_length = min(min_length, right - left)
        left += 1
    
    # S가 되지 않는다면 right를 증가
    else:
        right += 1

print(min_length)
```