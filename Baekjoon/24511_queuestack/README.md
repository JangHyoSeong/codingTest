# [24511] queuestack

### **난이도**
실버 3
## **📝문제**
한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

queuestack의 구조는 다음과 같다. 
$1$번, 
$2$번, ... , 
$N$번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

queuestack의 작동은 다음과 같다.

 
- $x_0$을 입력받는다. 
- $x_0$을 $1$번 자료구조에 삽입한 뒤 $1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_1$이라 한다.
- $x_1$을 $2$번 자료구조에 삽입한 뒤 $2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_2$이라 한다.
- ... 
- $x_{N-1}$을 $N$번 자료구조에 삽입한 뒤 $N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_N$이라 한다. 
- $x_N$을 리턴한다.  

도현이는 길이 
$M$의 수열 
$C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 
$1$ 참고)

queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.
### **입력**
첫째 줄에 queuestack을 구성하는 자료구조의 개수 
$N$이 주어진다. (
$1 \leq N \leq 100\,000$)

둘째 줄에 길이 
$N$의 수열 
$A$가 주어진다. 
$i$번 자료구조가 큐라면 
$A_i = 0$, 스택이라면 
$A_i = 1$이다.

셋째 줄에 길이 
$N$의 수열 
$B$가 주어진다. 
$B_i$는 
$i$번 자료구조에 들어 있는 원소이다. (
$1 \leq B_i \leq 1\,000\,000\,000$)

넷째 줄에 삽입할 수열의 길이 
$M$이 주어진다. (
$1 \leq M \leq 100\,000$)

다섯째 줄에 queuestack에 삽입할 원소를 담고 있는 길이 
$M$의 수열 
$C$가 주어진다. (
$1 \leq C_i \leq 1\,000\,000\,000$)

입력으로 주어지는 모든 수는 정수이다.
### **출력**
수열 
$C$의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.
### **예제입출력**

**예제 입력1**

```
4
0 1 1 0
1 2 3 4
3
2 4 7
```

**예제 출력1**

```
4 1 2
```

**예제 입력2**

```
5
1 1 1 1 1
1 2 3 4 5
3
1 3 5
```

**예제 출력2**

```
1 3 5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
M = int(input())
input_numbers = list(map(int, input().split()))

new_arr = deque()
for i in range(N):
    if arr_1[i] == 0:
        new_arr.append(arr_2[i])


for number in input_numbers:
    new_arr.appendleft(number)
    print(new_arr.pop(), end=" ")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|49464|204|Python3|381
#### **📝해설**

**알고리즘**
```
1. 자료구조
```

#### **📝해설**

```python
from collections import deque

# 입력받기
N = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
M = int(input())
input_numbers = list(map(int, input().split()))

# 문제 특성상, 스택은 입력받은 숫자가 그대로나옴. 따라서 고려하지 않아도 됨
new_arr = deque()

# 큐의 경우만 하나의 큐로 관리
for i in range(N):
    if arr_1[i] == 0:
        new_arr.append(arr_2[i])

# 여러개의 큐는 하나의 큐로 간주할 수 있음
for number in input_numbers:
    new_arr.appendleft(number)
    print(new_arr.pop(), end=" ")
```

### **🔖정리**

1. 자료구조만 사용하면 되는 줄 알고 헤맸는데, 생각을 잘 해야했다