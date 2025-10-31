# [12892] 생일 선물

### **난이도**
골드 5
## **📝문제**
오늘은 강민이의 생일이다. 강민이는 친구 N명이 있는데, 각 친구는 모두 강민이를 위한 생일 선물을 하나씩 준비했다. 각각의 선물은 P와 V를 가진다. P는 해당 선물의 가격이며, V는 만족도로 해당 선물을 받았을 때 강민이가 기뻐하는 정도를 수치화한 것이다.

강민이는 모든 선물을 다 받고 싶지만, 어떤 친구가 준 선물의 가격이 다른 친구가 준 선물의 가격과 D 이상 차이 나면 더 낮은 가격의 선물을 준 친구가 미안함을 느끼게 될 수 있다. 강민이는 자신의 행복도 중요하지만, 생일선물로 친구에게 미안함을 느끼게 하고 싶지는 않다. 고심 끝에 강민이는 일부 친구들에게만 선물을 받기로 결심했다. 누구도 미안하지 않을 수 있게 선물을 받으면서, 강민이가 느낄 수 있는 만족도의 최대 합은 얼마인지 구해보자.
### **입력**
첫 줄에 친구의 수 N(1 ≤ N ≤ 100,000)과 미안함을 느끼게 되는 최소가격차 D(1 ≤ D ≤ 1,000,000,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 선물의 가격 P와 만족도 V(0 ≤ P ≤ 1,000,000,000, 0 ≤ V ≤ 1,000,000,001)가 주어진다.
### **출력**
한 줄에 강민이가 최대 얼만큼 기뻐할 수 있는지를 출력하라.
### **예제입출력**

**예제 입력1**

```
4 2
13 10
10 20
11 30
12 40
```

**예제 출력1**

```
70
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, D = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort()

left = 0
max_happiness = 0
now_happiness = 0

for right in range(N):
    now_happiness += arr[right][1]

    while arr[right][0] - arr[left][0] >= D:
        now_happiness -= arr[left][1]
        left += 1
    
    max_happiness = max(max_happiness, now_happiness)

print(max_happiness)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|51624|300|Python3|446
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda item:item[0])

left, right, total, max_total = 0, 0, 0, 0

while right < N:
    total += arr[right][1]
    while arr[right][0] - arr[left][0] >= D:
        total -= arr[left][1]
        left += 1
    max_total = max(max_total, total)    
    right += 1
print(max_total)    
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
developerjy|46936|212|Python3|424
#### **📝해설**

```python
import sys

N, D = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 물건을 가격순서대로 정렬
arr.sort()

# 투포인터 사용을 위한 왼쪽 인덱스 설정
left = 0

# 최대 행복, 현재 행복 합
max_happiness = 0
now_happiness = 0

# 오른쪽 인덱스를 하나씩 늘려가며 확인
for right in range(N):

    # 현재 행복도에 이번 물건을 포함
    now_happiness += arr[right][1]

    # 만약 최대 가격과 최소 가격이 D를 넘는다면
    while arr[right][0] - arr[left][0] >= D:

        # 가격이 낮은 순서대로 하나씩 제외
        now_happiness -= arr[left][1]
        left += 1
    
    # 최대 행복도를 확인
    max_happiness = max(max_happiness, now_happiness)

print(max_happiness)
```