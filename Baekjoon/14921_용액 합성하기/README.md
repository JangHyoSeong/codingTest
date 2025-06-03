# [14921] 용액 합성하기

### **난이도**
골드 5
## **📝문제**
홍익대 화학연구소는 다양한 용액을 보유하고 있다. 각 용액은 -100,000,000부터 100,000,000사이의 특성 값을 갖는데,

같은 양의 두 용액을 혼합하면, 그 특성값은 두 용액의 특성값의 합이 된다.

당신은 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 하는데, 각 용액은 10ml시험관에 10ml씩 들어있고, 빈 20ml 시험관이 단 하나 있다. 게다가 용액을 계량할 수 없어서, 두 용액을 섞을 때는 10ml씩 섞어서 20ml로 만드는데, 단 한번밖에 할 수 없다. 그래서 미리 용액의 특성값들을 보고, 어떤 두 용액을 섞을 것인지 정해야 한다.

예를 들어, 연구소에 있는 용액들의 특성값이 [-101, -3, -1, 5, 93]이라고 하자. 이 경우에 특성 값이 각각 -101, 93인 용액을 혼합하면 -8인 용액을 만들 수 있다. 또한 특성값이 5인 용액과 93인 용액을 혼합하면 특성 값이 98인 용액을 만들 수 있다. 모든 가능한 조합을 생각해 보면, 특성값이 2인 용액이 0에 가장 가까운 용액이다.

용액들의 특성값 A1, … ,AN이 오름차순으로 주어졌을 때, 이 중 두 개의 용액을 혼합하여 만들 수 있는 0에 가장 가까운 특성값 B를 출력하시오.
### **입력**
N
A1 A2 … AN
### **출력**
B
### **예제입출력**

**예제 입력1**

```
5
-101 -3 -1 5 93
```

**예제 출력1**

```
2
```

**예제 입력2**

```
2
-100000 -99999
```

**예제 출력2**

```
-199999
```

**예제 입력3**

```
7
-698 -332 -123 54 531 535 699
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

front, rear = 0, N-1
min_gap = int(21e8)
while front < rear:
    temp_gap = arr[rear] + arr[front]

    if abs(min_gap) > abs(temp_gap):
        min_gap = temp_gap
        
    if temp_gap == 0:
        min_gap = 0
        break

    elif temp_gap > 0:
        rear -= 1

    else:
        front += 1

print(min_gap)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|123852|128|PyPy3|428
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = float("inf")
    real_ans = 0
    nums.sort()
    left, right = 0, N - 1
    while left < right:
        result = nums[left] + nums[right]
        if abs(result) < ans:
            ans = abs(result)
            real_ans = result
        if result < 0:
            left += 1
        elif result == 0:
            print(0)
            return
        else:  # result > 0
            right -= 1
    print(real_ans)


solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iamhelpingstar|43724|52|Python3|592
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 투 포인터를 위한 인덱스
front, rear = 0, N-1

# 최소 차이를 저장할 변수
min_gap = int(21e8)

# 투 포인터가 만나기 전까지 반복
while front < rear:

    # 현재 차이
    temp_gap = arr[rear] + arr[front]

    # 만약, 현재 차이가 갱신이 가능하다면 갱신
    if abs(min_gap) > abs(temp_gap):
        min_gap = temp_gap
    
    # 0 이라면 더이상 감소시킬 수 없으니 종료
    if temp_gap == 0:
        min_gap = 0
        break
    
    # 현재 차이가 0보다 크다면 rear 감소
    elif temp_gap > 0:
        rear -= 1

    # 0보다 작다면 front 증가
    else:
        front += 1

print(min_gap)
```