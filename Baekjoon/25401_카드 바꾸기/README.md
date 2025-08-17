# [25401] 카드 바꾸기

### **난이도**
골드 5
## **📝문제**
 
$N$개의 카드가 놓여있다. 편의상 가장 왼쪽에 있는 카드를 
$1$번 카드, 그 다음에 있는 카드를 
$2$번 카드 
$\dots$, 가장 오른쪽에 있는 카드가 
$N$번 카드라고 하자.

 
$N$개의 카드에는 각각 정수가 하나씩 적혀있다. 
$i$번 카드에 적혀있는 수를 
$x_i$라고 하자.

 
$N$개의 카드 중 일부에 적혀있는 수들을 적절히 바꾸어서, 왼쪽에서 오른쪽으로 갈수록 카드에 적혀있는 수들이 일정하게 증가하거나, 감소하거나, 또는 모든 수들이 같도록 하고 싶다.

카드에 적혀있는 수들을 바꿀 때는 정수 값으로만 바꿀 수 있으며, 바꾸는 횟수를 최소화해야 한다.

예를 들어, 아래의 그림과 같이 카드들이 주어졌다고 하자.



이 경우 
$3$번 카드에 적혀있는 수를 
$3$으로 바꾸면 아래와 같이 
$1$씩 증가하도록 할 수 있고, 적혀있는 수를 바꾼 카드의 수는 
$1$개이다.



다음과 같이 모든 카드에 적혀있는 수를 
$2$가 되도록 할 수도 있다. 이때, 적혀있는 수를 바꾼 카드의 수는 
$2$개이다.



가장 왼쪽에 있는 카드부터 가장 오른쪽에 있는 카드까지 각 카드에 적혀있는 수들이 순서대로 주어질 때, 조건을 만족하도록 하려면 바꿔야 할 카드 수의 최솟값을 구하여라.
### **입력**
첫 번째 줄에 카드의 수 
$N$이 주어진다.

두 번째 줄에는 각 카드에 적힌 수 
$x_i$가 공백을 사이에 두고 순서대로 주어진다.
### **출력**
첫 번째 줄에 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 2 2 4
```

**예제 출력1**

```
1
```

**예제 입력2**

```
5
6 3 3 1 -1
```

**예제 출력2**

```
2
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

counter = Counter(cards)
max_len = max(counter.values())

for i in range(N):
    for j in range(i + 1, N):
        diff = cards[j] - cards[i]
        step = j - i

        if diff % step != 0:
            continue

        d = diff // step

        length = 0
        for k in range(N):
            if cards[i] + (k - i) * d == cards[k]:
                length += 1
        
        max_len = max(max_len, length)

print(N - max_len)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----|:-----:|:-----:|:-----:|:--------:
정답|112216|556|PyPy3|524
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [*map(int, input().split())]
    mx = 0
    for i in range(n):
        cnt = {}
        for j in range(i+1, n):
            y = a[j]-a[i]
            x = j-i
            if y%x: continue
            d = y//x
            cnt[d] = cnt.get(d, 0) + 1
            if cnt[d] > mx: mx = cnt[d]
    print(n-1-mx)


if __name__ == "__main__": main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|32544|80|Python3|420
#### **📝해설**

```python
from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

# 각 카드가 몇개있는지 확인
counter = Counter(cards)

# 가장 많은 카드 개수
max_len = max(counter.values())

# 2중 반복문을 통해 공차를 확인
for i in range(N):
    for j in range(i + 1, N):

        # 현재 차이
        diff = cards[j] - cards[i]

        # 인덱스 차이
        step = j - i

        # 정수 공차가 아닌 경우 넘어감
        if diff % step != 0:
            continue
        
        # 현재 공차
        d = diff // step

        # 이 공차를 적용했을 때, 수열을 만족하는 숫자가 몇개인지 셈
        length = 0
        for k in range(N):
            if cards[i] + (k - i) * d == cards[k]:
                length += 1
        
        # 최대값 갱신
        max_len = max(max_len, length)

print(N - max_len)
```