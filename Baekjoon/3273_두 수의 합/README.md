# [3273] 두 수의 합

### **난이도**
실버 3
## **📝문제**
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)
### **출력**
문제의 조건을 만족하는 쌍의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
9
5 12 7 10 9 1 2 3 11
13
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()
left, right = 0, N - 1
count = 0

while left < right:
    total = arr[left] + arr[right]
    if total == x:
        count += 1
        left += 1
        right -= 1
    elif total < x:
        left += 1
    else:
        right -= 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121756|112|PyPy3|379
#### **📝해설**

**알고리즘**
```
1. 정렬
2. 투포인터
```

### **다른 풀이**

```python
def solution(arr, x):
    numset = set(arr)
    cnt = 0
    for num in arr:
        if x - num in numset:
            cnt += 1
    return cnt // 2

# 백준 입출력
_ = int(input())
arr = list(map(int, input().split(' ')))
x = int(input())
print(solution(arr, x))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kgy556|44092|60|Python3|265
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

# 오름차순 정렬
arr.sort()
# 투 포인터 설정
left, right = 0, N - 1
count = 0

while left < right:
    total = arr[left] + arr[right]
    # 합이 x라면 count를 1 더하고 각각의 포인터를 움직임
    if total == x:
        count += 1
        left += 1
        right -= 1
    elif total < x:
        left += 1
    else:
        right -= 1

print(count)
```