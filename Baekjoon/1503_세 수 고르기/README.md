# [1503] 세 수 고르기

### **난이도**
실버 2
## **📝문제**
M개의 자연수로 이루어진 집합 S와 자연수 N이 주어진다.

S에 속하지 않는 자연수 x, y, z를 골라서, |N - xyz|의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 1,000)과 집합 S의 크기 M(0 ≤ M ≤ 50)이 주어진다. 둘째 줄에는 집합 S에 들어있는 수가 주어진다. 집합에 들어있는 수는 1,000보다 작거나 같은 자연수이고, 공백으로 구분되어져 있다. 또, 중복되는 수는 없다.

집합의 크기가 0인 경우에는 둘째 줄은 빈 줄이다.
### **출력**
첫째 줄에 |N - xyz|의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 2
2 4
```

**예제 출력1**

```
1
```

**예제 입력2**

```
10 1
1
```

**예제 출력2**

```
2
```

**예제 입력3**

```
10 2
1 2
```

**예제 출력3**

```
17
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
S = list(map(int, input().split())) if M > 0 else []

all_numbers = set(range(1, 1002))
valid_numbers = sorted(all_numbers - set(S))

min_diff = 21e8

for x in valid_numbers:
    for y in valid_numbers:
        for z in valid_numbers:
            min_diff = min(min_diff, abs(N-x*y*z))

print(min_diff)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110736|6792|PyPy3|335
#### **📝해설**

**알고리즘**
```
1. 브루트포스
```

#### **📝해설**

```python
N, M = map(int, input().split())
S = list(map(int, input().split())) if M > 0 else []

# 1000 - 1001의 경우가 존재할 수 있으니, 1002까지 자연수의 범위를 잡음
all_numbers = set(range(1, 1002))

# 집합 S에 속한 숫자는 뺌
valid_numbers = sorted(all_numbers - set(S))

# 최소값
min_diff = 21e8

# 모든 숫자를 순회하면서 최소값을 찾음
for x in valid_numbers:
    for y in valid_numbers:
        for z in valid_numbers:
            min_diff = min(min_diff, abs(N-x*y*z))

print(min_diff)
```