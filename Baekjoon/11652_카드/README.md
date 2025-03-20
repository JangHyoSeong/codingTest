# [11652] 카드

### **난이도**
실버 4
## **📝문제**
준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
### **입력**
첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
### **출력**
첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
1
2
1
2
1
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6
1
2
1
2
1
2
```

**예제 출력2**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

counter = Counter(cards)
most_common = counter.most_common()
max_count = most_common[0][1]

min_most_frequent = min(num for num, count in most_common if count == max_count)

print(min_most_frequent)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|136360|184|PyPy3|345
#### **📝해설**

**알고리즘**
```
1. 해쉬
```

### **다른 풀이**

```python
n, *a = map(int, open(0).read().split())
m = c = t = 0
prev = ''
for i in sorted(a):
    if prev != i:
        if c < t:
            c = t
            m = prev
        prev = i
        t = 1
    else:
        t += 1
if c < t:
    m = prev
print(m)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
joseph97|45108|92|Python3|247
#### **📝해설**

```python
import sys
from collections import Counter

# 입력받기
N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 배열에서 각 원소가 몇개있는지 세는 라이브러리
counter = Counter(cards)

# 각 원소의 빈도수를 저장 [(원소, 빈도수), ...]
most_common = counter.most_common()
max_count = most_common[0][1]

# 가장 자주나오고, 작은 원소를 출력
min_most_frequent = min(num for num, count in most_common if count == max_count)

print(min_most_frequent)
```