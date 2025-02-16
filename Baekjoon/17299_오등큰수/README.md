# [17299] 오등큰수

### **난이도**
골드 3
## **📝문제**
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.

Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오등큰수는 -1이다.

예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.
### **입력**
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
### **출력**
총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1 1 2 3 4 2 1
```

**예제 출력1**

```
-1 -1 1 2 2 1 -1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = Counter(arr)
result = [-1] * N

stack = []

for i in range(N):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|258048|PyPy3|346
#### **📝해설**

**알고리즘**
```
1. 스택
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

A = int(input())
arr = list(map(int, input().split(' ')))
count = [0] * 1000001
stack = []
res = [-1] * A

for elem in arr:
    count[elem] += 1

for i in range(A):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        res[stack.pop()] = arr[i]
    stack.append(i)

print(" ".join(map(str, res)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
simigami|233820|396|PyPy3|348
#### **📝해설**

```python
import sys
from collections import Counter

# 입력받기
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 숫자의 빈도를 구할 카운터
count = Counter(arr)

# 결과를 저장할 리스트
result = [-1] * N

# 연산을 위해 사용할 스택
stack = []

# 모든 숫자를 순회하면서
for i in range(N):

    # 스택이 차있을 때, 현재 요소의 등장 횟수가 스택 top의 요소보다 클 때
    while stack and count[arr[stack[-1]]] < count[arr[i]]:

        # 결과를 갱신
        result[stack.pop()] = arr[i]

    # 스택에 삽입
    stack.append(i)

# 결과 출력
print(*result)
```