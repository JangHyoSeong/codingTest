# [7894] 큰 수

### **난이도**
골드 3
## **📝문제**
많은 어플리케이션은 매우 큰 수를 사용한다. 이러한 어플리케이션은 데이터를 안전하게 전송하고, 암호화하기 위해서 수를 키로 사용한다.

수가 주어지면, 그 수의 팩토리얼의 자리수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 수가 주어진다. 다음 줄부터 한 줄에 하나씩 정수 m이 주어진다. (1 ≤ m ≤ 107)
### **출력**
입력으로 주어지는 수 m마다 m!의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
2
10
20
```

**예제 출력1**

```
7
19
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import math

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers)

arr = [0] * (max_num + 1)
for i in range(1, max_num + 1):
    arr[i] = arr[i - 1] + math.log10(i)

for m in numbers:
    print(int(arr[m]) + 1)

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|266552|588|PyPy3|242
#### **📝해설**

**알고리즘**
```
1. 수학
```

### **다른 풀이**

```python
import math
from sys import stdin

def log_approximation(n):
    
    return math.log10((2*math.pi*n))/2 + n * (math.log10(n)-math.log10(math.e))

t = int(stdin.readline())

for _ in range(t):
    
    m = int(stdin.readline())

    print(int(log_approximation(m))+1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
gnzpstly2000|32540|36|Python3|267
#### **📝해설**

```python
import math

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers)

# 가장 큰 수까지 자릿수를 저장할 리스트
arr = [0] * (max_num + 1)

# 각 숫자의 자릿수를 구함
for i in range(1, max_num + 1):
    arr[i] = arr[i - 1] + math.log10(i)

# 출력
for m in numbers:
    print(int(arr[m]) + 1)
```