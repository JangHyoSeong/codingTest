# [18114] 블랙 프라이데이

### **난이도**
골드 5
## **📝문제**
서강 백화점이 블랙 프라이데이를 맞아서 특별 이벤트를 진행한다. 백화점에서 제시하는 양의 정수의 무게 C에 딱 맞게 물건들을 가져오면 전부 만 원에 판매하는 이벤트이다.

선택할 수 있는 물건은 최대 3개까지이고, 같은 물건을 중복 선택하는 것은 불가능하다. 그리고 백화점에서 판매하는 물건들의 무게는 모두 다르다.

예를 들어, 백화점에서 판매하고 있는 물건 5개의 무게가 각각 1, 2, 3, 4, 5일 때, C가 5라면 {2, 3} 또는 {5}에 해당하는 물건의 조합을 만 원에 구매할 수 있다.

판매하는 물건 N개의 양의 정수의 무게가 각각 주어질 때, 만 원에 구매할 수 있는 조합이 있는지 출력하라.
### **입력**
첫 번째 줄에 물건의 개수 N과 제시하는 무게 C가 공백으로 구분되어 주어진다. (1 ≤ N ≤ 5,000, 1 ≤ C ≤ 108, N과 C는 양의 정수)

다음 줄에는 N개의 물건 각각의 무게 w가 공백으로 구분되어 주어진다. (1 ≤ w ≤ 108, w는 양의 정수)
### **출력**
문제의 조건을 만족하는 조합이 있으면 1, 그렇지 않으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5
1 2 3 4 5
```

**예제 출력1**

```
1
```

**예제 입력2**

```
3 13
3 7 8
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, C = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def check(N, C):
    if C in arr:
        return True

    front, rear = 0, N - 1
    while front < rear:
        now_sum = arr[front] + arr[rear]
        
        if now_sum == C:
            return True
        elif now_sum > C:
            rear -= 1
        else:
            target = C - now_sum
            if arr[front] != target and arr[rear] != target and binary_search(front + 1, rear - 1, target):
                return True
            front += 1

    return False

print(1 if check(N, C) else 0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110444|104|PyPy3|899
#### **📝해설**

**알고리즘**
```
1. 이진 탐색
2. 투 포인터
```

### **다른 풀이**

```python
import sys 
input = sys.stdin.readline

def sol(l):
    N,C = map(int,input().split())
    Thing = sorted(list(map(int,input().split())))
    set_of_Thing = set([0]+ Thing)
    if C in set_of_Thing:
        return 1
    while l < N-1:
        left,right = Thing[l], Thing[N-1]
        a = C-left-right
        if a != left and a != right and a in set_of_Thing:
            return 1
        if a < 0:
            N -= 1
        else:
            l += 1
    return 0
            
print(sol(0))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ekqls5264|31180|40|Python3|491
#### **📝해설**

```python
import sys

N, C = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

# 이진탐색
def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

# 투 포인터를 사용하고 가운데 값을 이진탐색으로 검색
def check(N, C):
    if C in arr:
        return True

    front, rear = 0, N - 1
    while front < rear:
        now_sum = arr[front] + arr[rear]
        
        if now_sum == C:
            return True
        elif now_sum > C:
            rear -= 1
        else:
            target = C - now_sum
            if arr[front] != target and arr[rear] != target and binary_search(front + 1, rear - 1, target):
                return True
            front += 1

    return False

print(1 if check(N, C) else 0)
```