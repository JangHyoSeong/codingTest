# [12931] 두 배 더하기

### **난이도**
골드 5
## **📝문제**
모든 값이 0으로 채워져 있는 길이가 N인 배열 A가 있다. 영선이는 다음과 같은 두 연산을 수행할 수 있다.

- 배열에 있는 값 하나를 1 증가시킨다.
- 배열에 있는 모든 값을 두 배 시킨다.
배열 B가 주어졌을 때, 배열 A를 B로 만들기 위한 연산의 최소 횟수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 배열의 크기 N이 주어진다. (1 ≤ N ≤ 50)

둘째 줄에는 배열 B에 들어있는 원소가 공백으로 구분해서 주어진다. 배열에 B에 들어있는 값은 0보다 크거나 같고, 1,000보다 작거나 같다.
### **출력**
첫째 줄에 배열 A를 B로 바꾸기 위한 최소 연산 횟수를 출력한다.
### **예제입출력**

**예제 입력1**

```
2
2 1
```

**예제 출력1**

```
3
```

**예제 입력2**

```
3
16 16 16
```

**예제 출력2**

```
7
```

**예제 입력3**

```
1
100
```

**예제 출력3**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

count = 0
while any(arr):
    for i in range(N):
        if arr[i] % 2 == 1:
            arr[i] -= 1
            count += 1
    
    if all(num == 0 for num in arr):
        break

    arr = [num // 2 for num in arr]
    count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|301
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
n = int(input())
arr = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        if arr[i] % 2:
            arr[i] -= 1
            ans += 1
    if sum(arr) == 0:
        break
    arr = [x // 2 for x in arr]
    ans += 1
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dhtlq777|31120|32|Python3|258
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# 연산 횟수
count = 0

# 입력받은 배열에서 모든 값을 0으로 만들 때까지 반복
while any(arr):

    # 홀수인 경우 짝수가 되어야함
    for i in range(N):
        if arr[i] % 2 == 1:
            arr[i] -= 1
            count += 1

    # 모든 값이 0이라면 반복 종료    
    if all(num == 0 for num in arr):
        break

    # 모든 값을 2로 나눔
    arr = [num // 2 for num in arr]
    count += 1

print(count)
```