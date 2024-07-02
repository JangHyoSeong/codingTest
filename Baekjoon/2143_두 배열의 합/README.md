# [2143] 두 배열의 합

### **난이도**
골드 3
## **📝문제**
한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

```
T(=5) = A[1] + B[1] + B[2]
      = A[1] + A[2] + B[1]
      = A[2] + B[3]
      = A[2] + A[3] + B[1]
      = A[3] + B[1] + B[2]
      = A[3] + A[4] + B[3]
      = A[4] + B[2] 
```
### **입력**
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.
### **출력**
첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.


### **예제입출력**

**예제 입력1**

```
5
4
1 3 1 2
3
1 3 2
```

**예제 출력1**

```
7
```
### **출처**
Olympiad > 한국정보올림피아드 > KOI 2001 > 고등부 1번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import Counter

def find_subarray_sums(arr):
    subarray_sums = []
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            subarray_sums.append(current_sum)
    return subarray_sums

def count_pairs_with_sum(A, B, T):
    subarray_sums_A = find_subarray_sums(A)
    subarray_sums_B = find_subarray_sums(B)
    
    count_B = Counter(subarray_sums_B)
    
    count = 0
    for sum_A in subarray_sums_A:
        required_B = T - sum_A
        if required_B in count_B:
            count += count_B[required_B]
    
    return count

# 입력
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 결과 출력
result = count_pairs_with_sum(A, B, T)
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|98136|268|Python3|836
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
2. 누적합
```

### **다른 풀이**

```python
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sa = [0]
cumul = 0
for i in range(n):
    cumul += a[i]
    sa.append(cumul)

sb = [0]
cumul = 0
for i in range(m):
    cumul += b[i]
    sb.append(cumul)

ca = dict()
for i in range(n):
    for j in range(i + 1, n + 1):
        s = sa[j] - sa[i]
        if s not in ca:
            ca[s] = 1
        else:
            ca[s] += 1
            
total = 0
for i in range(m):
    for j in range(i + 1, m + 1):
        s = sb[j] - sb[i]
        f = t - s
        
        if f in ca:
            total += ca[f]
        
print(total)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hsh8086|190968|208|PyPy3|651
#### **📝해설**

```python
from collections import Counter

def find_subarray_sums(arr):
    # 모든 부분 배열의 합을 리스트에 저장
    subarray_sums = []
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            subarray_sums.append(current_sum)
    return subarray_sums

def count_pairs_with_sum(A, B, T):
    # 모든 부분 배열의 합을 생성
    subarray_sums_A = find_subarray_sums(A)
    subarray_sums_B = find_subarray_sums(B)
    
    # 
    count_B = Counter(subarray_sums_B)
    
    count = 0
    for sum_A in subarray_sums_A:
        required_B = T - sum_A
        if required_B in count_B:
            count += count_B[required_B]
    
    return count

# 입력
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 결과 출력
result = count_pairs_with_sum(A, B, T)
print(result)
```

### **🔖정리**

1. 배운점