# [1038] 감소하는 수

### **난이도**
골드 5
## **📝문제**
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
### **입력**
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.
### **출력**
첫째 줄에 N번째 감소하는 수를 출력한다.


### **예제입출력**

**예제 입력1**

```
18
```

**예제 출력1**

```
42
```

**예제 입력2**

```
0
```

**예제 출력2**

```
0
```

**예제 입력3**

```
50000
```

**예제 출력3**

```
-1 
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

N = int(input())

arr = []
for i in range(1, 11):
    for comb in combinations(range(10), i):
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        arr.append(num)

    
arr.sort()

if N >= len(arr):
    print(-1)
else:
    print(arr[N])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|48|Python3|292
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
n = int(input())
ans = []

def decrease(x):
    ans.append(x)
    left = int(str(x)[0])
    for i in range(left+1, 10):
        decrease(int(str(i) + str(x)))

for i in range(10):
    decrease(i)
    
ans.sort()

try :
    print(ans[n])
except : 
    print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
whtmdgus56|30616|36|Python3|260
#### **📝해설**

```python
from itertools import combinations

N = int(input())

# 감소하는 수를 담을 리스트
arr = []

# 감소하는 수 생성
for i in range(1, 11):
    # 모든 자릿수에 대해 조합을 생성(중복 제거)
    for comb in combinations(range(10), i):
        # 정렬을 해서 감소하는 수로 만듦
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        arr.append(num)

# 정렬
arr.sort()

# N번째 감소하는 수 출력
if N >= len(arr):
    print(-1)
else:
    print(arr[N])
```