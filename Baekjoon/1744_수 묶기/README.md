# [1744] 수 묶기

### **난이도**
골드 4
## **📝문제**
길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
### **출력**
수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.
### **예제입출력**

**예제 입력1**

```
4
-1
2
1
3
```

**예제 출력1**

```
6
```

**예제 입력2**

```
6
0
1
2
4
3
5
```

**예제 출력2**

```
27
```

**예제 입력3**

```
1
-1
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

positive = []
negative = []
one = 0
zero = 0

for _ in range(N):
    num = int(input())

    if num > 1:
        positive.append(num)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        negative.append(num)

positive.sort()
negative.sort(reverse=True)

result = 0
while len(positive) > 1:
    result += positive.pop() * positive.pop()
if positive:
    result += positive[0]

while len(negative) > 1:
    result += negative.pop() * negative.pop()

if negative:
    if zero == 0:
        result += negative[0]

result += one
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|593
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

n = int(sys.stdin.readline())
nums_p = []
nums_m = []
result = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 1 :
        nums_p.append(tmp)
    elif tmp <= 0:
        nums_m.append(tmp)
    else:
        result += 1
nums_p.sort(reverse=True)
nums_m.sort()




for i in range(0,len(nums_p),2):
    if i+1 >= len(nums_p):
        result += nums_p[i]
    else:
        result += (nums_p[i]*nums_p[i+1])

for i in range(0, len(nums_m), 2):
    if i+1 >= len(nums_m):
        result += nums_m[i]
    else:
        result += (nums_m[i]*nums_m[i+1])

print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
zxc5932|31120|28|Python3|594
#### **📝해설**

```python
N = int(input())

# 각각 양의 정수, 음의 정수를 담을 리스트, 1의 개수, 0의 개수
positive = []
negative = []
one = 0
zero = 0

# 입력받기
for _ in range(N):
    num = int(input())

    if num > 1:
        positive.append(num)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        negative.append(num)

# 각각 절댓값이 작은 순으로 정렬
positive.sort()
negative.sort(reverse=True)

# 결과값
result = 0

# 양의 정수는 큰 순서대로 묶는 것이 최대. 묶을 수 있는 정수를 모두 묶어줌
while len(positive) > 1:
    result += positive.pop() * positive.pop()

# 묶고 남아있는 수가 생긴다면 그냥 더함
if positive:
    result += positive[0]

# 음의 정수도 절대값이 큰 순서대로 묶는것이 최대(양수가 됨)
while len(negative) > 1:
    result += negative.pop() * negative.pop()

# 남는 음수는 0이 있는 경우 묶고(0이 됨), 아니라면 더함
if negative:
    if zero == 0:
        result += negative[0]

# 1은 그냥 더해줌
result += one
print(result)
```