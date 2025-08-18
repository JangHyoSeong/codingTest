# [1174] 줄어드는 수

### **난이도**
골드 5
## **📝문제**
음이 아닌 정수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소할 때, 그 수를 줄어드는 수라고 한다. 예를 들어, 321와 950은 줄어드는 수이고, 322와 958은 아니다.

N번째로 작은 줄어드는 수를 출력하는 프로그램을 작성하시오. 만약 그러한 수가 없을 때는 -1을 출력한다. 가장 작은 줄어드는 수가 1번째 작은 줄어드는 수이다.
### **입력**
N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 N번째 작은 줄어드는 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
1
```

**예제 출력1**

```
0
```

**예제 입력2**

```
19
```

**예제 출력2**

```
42
```

**예제 입력3**

```
500000
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

nums = []

for length in range(1, 11):
    for comb in combinations(range(10), length):
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        nums.append(num)

nums.sort()

if N > len(nums):
    print(-1)

else:
    print(nums[N-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|305
#### **📝해설**

**알고리즘**
```
1. 조합
2. 브루트포스
```

### **다른 풀이**

```python
def f(n):return [0]if n == 0 else(l:=f(n-1))+[int(str(n)+str(i)) for i in l]+[n]
l,n=f(9),int(input())-1
print(sorted(l)[n]if n<len(l)else -1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jwdoctor08|31120|32|Python3|142
#### **📝해설**

```python
from itertools import combinations

N = int(input())

# 줄어드는 수를 순서대로 저장할 리스트
nums = []

# 1 ~ 10자리 수를 만듦
for length in range(1, 11):

    # 조합을 뽑는다면, 줄어드는 수로 만들 수 있음
    for comb in combinations(range(10), length):

        # 내림차순으로 정렬 후 삽입
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        nums.append(num)

# 전체 정렬
nums.sort()

# 출력
if N > len(nums):
    print(-1)

else:
    print(nums[N-1])
```