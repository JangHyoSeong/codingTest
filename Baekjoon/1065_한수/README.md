# [1065] 한수

### **난이도**
실버 4
## **📝문제**
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
### **입력**
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
### **출력**
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
110
```

**예제 출력1**

```
99
```

**예제 입력2**

```
1
```

**예제 출력2**

```
1
```

**예제 입력3**

```
210
```

**예제 출력3**

```
105
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

def func(n):
    digits = list(map(int, str(n)))
    if len(digits) <= 2:
        return True
    
    return digits[0] - digits[1] == digits[1] - digits[2]

count = 0
for i in range(1, N+1):
    if func(i):
        count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|258
#### **📝해설**

**알고리즘**
```
1. 브루트포스 알고리즘
```

#### **📝해설**

```python
N = int(input())

def func(n):
    digits = list(map(int, str(n)))

    # 두자리수 이하라면 무조건 한수
    if len(digits) <= 2:
        return True
    
    # 세자리수인 경우 등차수열인지 판별
    return digits[0] - digits[1] == digits[1] - digits[2]

count = 0
for i in range(1, N+1):
    if func(i):
        count += 1

print(count)
```