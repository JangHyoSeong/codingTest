# [1477] 휴게소 세우기

### **난이도**
골드 4
## **📝문제**
다솜이는 유료 고속도로를 가지고 있다. 다솜이는 현재 고속도로에 휴게소를 N개 가지고 있는데, 휴게소의 위치는 고속도로의 시작으로부터 얼만큼 떨어져 있는지로 주어진다. 다솜이는 지금 휴게소를 M개 더 세우려고 한다.

다솜이는 이미 휴게소가 있는 곳에 휴게소를 또 세울 수 없고, 고속도로의 끝에도 휴게소를 세울 수 없다. 휴게소는 정수 위치에만 세울 수 있다.

다솜이는 이 고속도로를 이용할 때, 모든 휴게소를 방문한다. 다솜이는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다. (반드시 M개를 모두 지어야 한다.)

예를 들어, 고속도로의 길이가 1000이고, 현재 휴게소가 {200, 701, 800}에 있고, 휴게소를 1개 더 세우려고 한다고 해보자.

일단, 지금 이 고속도로를 타고 달릴 때, 휴게소가 없는 구간의 최댓값은 200~701구간인 501이다. 하지만, 새로운 휴게소를 451구간에 짓게 되면, 최대가 251이 되어서 최소가 된다.
### **입력**
첫째 줄에 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L이 주어진다. 둘째 줄에 현재 휴게소의 위치가 공백을 사이에 두고 주어진다. N = 0인 경우 둘째 줄은 빈 줄이다.
### **출력**
첫째 줄에 M개의 휴게소를 짓고 난 후에 휴게소가 없는 구간의 최댓값의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
6 7 800
622 411 201 555 755 82
```

**예제 출력1**

```
70
```

**예제 입력2**

```
3 1 1000
200 701 800
```

**예제 출력2**

```
251
```

**예제 입력3**

```
3 1 1000
300 701 800
```

**예제 출력3**

```
300
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, L = map(int, input().split())

if N != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

arr.append(0)
arr.append(L)
arr.sort()

sections = []
for i in range(1, len(arr)):
    sections.append(arr[i] - arr[i-1])

def can_build(max_dist):
    count = 0
    for section in sections:
        if section > max_dist:
            count += (section - 1) // max_dist
    
    return count <= M

left, right = 1, L
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_build(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|604
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

def find_location(rest, L, M):
    count = 0
    for i in range(1, len(rest)):
        count += (rest[i] - rest[i - 1] - 1) // L
    return count <= M

def binary_search():
    lt = 1
    rt = L

    while lt < rt:
        mid = (lt + rt)//2
        if find_location(rest, mid, M):
            rt = mid
        else:
            lt = mid + 1
    
    return lt 

rest = list(map(int, input().split()))
rest.append(0)
rest.append(L)
rest.sort() 

print(binary_search())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jaenam2060|31120|32|Python3|552
#### **📝해설**

```python
N, M, L = map(int, input().split())

if N != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

# 시작점과 끝점을 추가하고 정렬
arr.append(0)
arr.append(L)
arr.sort()

# 휴게소 사이의 구간의 거리를 저장
sections = []
for i in range(1, len(arr)):
    sections.append(arr[i] - arr[i-1])

# 현재 구간의 거리가 정해둔 길이 안에 포함되는지 확인하는 함수
def can_build(max_dist):
    count = 0
    for section in sections:
        
        # 정해둔 길이보다 큰 구간이 있다면
        if section > max_dist:

            # 구간을 나눔(나눈 횟수를 추가)
            count += (section - 1) // max_dist
    
    # M개 안에 나눌 수 있다면 True, 아니라면 False
    return count <= M

# 이분탐색. 최대 구간 거리를 찾음
left, right = 1, L
answer = 0

while left <= right:
    mid = (left + right) // 2
    # 최대 구간을 mid로 뒀을 때 M개 안에 나눌 수 있다면
    if can_build(mid):
        answer = mid
        # 최대 구간 크기를 늘림
        right = mid - 1
    
    # 최대 구간 크기를 줄임
    else:
        left = mid + 1

print(answer)
```