# [17298] 오큰수

### **난이도**
골드 4
## **📝문제**
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
### **입력**
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
### **출력**
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
### **예제입출력**

**예제 입력1**

```
4
3 5 2 7
```

**예제 출력1**

```
5 7 7 -1
```

**예제 입력2**

```
4
9 5 4 8
```

**예제 출력2**

```
-1 8 8 -1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

result = [-1] * N
stack = []

for i in range(N):
    
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|202408|908|Python3|246
#### **📝해설**

**알고리즘**
```
1. 스택
```

#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# 결과를 저장할 리스트. 초기값은 -1로 초기화
result = [-1] * N
# 오큰수를 구할때 사용할 스택
stack = []

# 숫자를 순회하면서
for i in range(N):
    
    # 스택이 비어있지 않고, 현재 스택의 top보다 이번 인덱스의 숫자가 크다면 
    # -> 처음으로 큰 숫자를 만났다면
    # 그 숫자의 오큰수는 arr[i]
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    
    # 스택에 값을 삽입
    stack.append(i)

print(' '.join(map(str, result)))
```