# [25635] 자유 이용권

### **난이도**
골드 4
## **📝문제**
자유 이용권은 놀이공원의 모든 놀이기구를 횟수의 제한 없이 마음껏 이용할 수 있는 이용권이다. 준원이는 ANA 놀이공원의 자유 이용권을 구매했고, 최대한 많이 놀이기구를 이용할 생각이다. 단, 연속으로 같은 놀이기구를 이용하지는 않기로 했다.

그런데 준원이가 구매한 자유 이용권을 잘 살펴보니 놀이공원의 모든 놀이기구별로 이용 횟수의 제한이 명시되어 있었다. 이 자유 이용권으로, 연속으로 같은 놀이기구를 이용하지 않고 놀이기구를 이용할 수 있는 최대 횟수는 얼마일까?
### **입력**
첫째 줄에 놀이기구의 종류의 개수 
$N(1\le N \le 100\ 000)$이 주어진다.

둘째 줄에 정수 
$a_1, a_2, ..., a_N$이 주어진다. 
$a_i(1 \le a_i \le 10^9)$는 
$i$번째 놀이기구 이용 횟수 제한이다.
### **출력**
연속으로 같은 놀이기구를 이용하지 않고 놀이기구를 이용할 수 있는 최대 횟수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
1 1 3
```

**예제 출력1**

```
5
```

**예제 입력2**

```
2
3 5
```

**예제 출력2**

```
7
```

**예제 입력3**

```
4
2 2 2 3
```

**예제 출력3**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

total = sum(arr)
max_val = max(arr)

if max_val <= total - max_val + 1:
    print(total)
else:
    print((total - max_val) * 2 + 1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|44748|60|Python3|243
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
n = int(input())

A = list(map(int,input().split()))

m = max(A)
s = sum(A)

r = s - m

if m <= r+1:
    
    print(s)

else:
    
    print(2*r+1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
gnzpstly2000|44748|60|Python3|147
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 총 합
total = sum(arr)

# 가장 큰 값
max_val = max(arr)

# 가장 많이 타는 놀이기구가 나머지의 총합 + 1 보다 작다면 모든 놀이기구를 횟수만큼 탈 수 있음
if max_val <= total - max_val + 1:
    print(total)

# 아닌 경우
else:
    print((total - max_val) * 2 + 1)
```