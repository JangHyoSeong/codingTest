# [16936] 나3곱2

### **난이도**
골드 5
## **📝문제**
나3곱2 게임은 정수 하나를 이용한다. 가장 먼저, 정수 x로 시작하고, 연산을 N-1번 적용한다. 적용할 수 있는 연산은 두 가지 있고, 아래와 같다.

- 나3: x를 3으로 나눈다. x는 3으로 나누어 떨어져야 한다.
- 곱2: x에 2를 곱한다.  
나3곱2 게임을 진행하면서, 만든 수를 모두 기록하면 수열 A를 만들 수 있다. 예를 들어, x = 9, N = 6이고, 적용한 연산이 곱2, 곱2, 나3, 곱2, 나3인 경우에 A = [9, 18, 36, 12, 24, 8] 이다.

수열 A의 순서를 섞은 수열 B가 주어졌을 때, 수열 A를 구해보자.
### **입력**
첫째 줄에 수열의 크기 N(2 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 수열 B가 주어진다. B에 포함된 원소는 1018 보다 작거나 같은 자연수이다.
### **출력**
나3곱2 게임의 결과 수열 A를 출력한다. 항상 정답이 존재하는 경우에만 입력으로 주어지며, 가능한 정답이 여러가지인 경우에는 아무거나 출력한다.
### **예제입출력**

**예제 입력1**

```
6
4 8 6 3 12 9
```

**예제 출력1**

```
9 3 6 12 4 8
```

**예제 입력2**

```
4
42 28 84 126
```

**예제 출력2**

```
126 42 84 28
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

num_map = {num: True for num in arr}

# 수열의 시작점을 찾는다.
for num in arr:
    found = True
    current = num
    for _ in range(N - 1):
        if current % 3 == 0 and num_map.get(current // 3, False):
            current //= 3
        elif num_map.get(current * 2, False):
            current *= 2
        else:
            found = False
            break
    if found:
        start_num = num
        break

# 수열 A를 구성한다.
result = [start_num]
for _ in range(N - 1):
    current = result[-1]
    if current % 3 == 0 and num_map.get(current // 3, False):
        result.append(current // 3)
    elif num_map.get(current * 2, False):
        result.append(current * 2)

print(" ".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|40|Python3|789
#### **📝해설**

**알고리즘**
```
1. 수학
```

### **다른 풀이**

```python
def log(under: int, number: int):
    if number % under:
        return 0
    return log(under, number//under) + 1


def ingredient(number: int):
    return log(2, number), -log(3, number), number


N = int(input())
B = list(map(ingredient, map(int, input().split())))
B.sort()
print(*map(lambda x: x[2], B))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
leeholeo|30616|36|Python3|317
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

num_map = {num: True for num in arr}

# 수열의 시작점을 찾는다.
for num in arr:
    found = True
    current = num
    for _ in range(N - 1):
        if current % 3 == 0 and num_map.get(current // 3, False):
            current //= 3
        elif num_map.get(current * 2, False):
            current *= 2
        else:
            found = False
            break
    if found:
        start_num = num
        break

# 수열 A를 구성한다.
result = [start_num]
for _ in range(N - 1):
    current = result[-1]
    if current % 3 == 0 and num_map.get(current // 3, False):
        result.append(current // 3)
    elif num_map.get(current * 2, False):
        result.append(current * 2)

print(" ".join(map(str, result)))
```