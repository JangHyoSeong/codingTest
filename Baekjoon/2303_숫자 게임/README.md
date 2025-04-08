# [2303] 숫자 게임

### **난이도**
실버 5
## **📝문제**
N명이 모여 숫자 게임을 하고자 한다. 각 사람에게는 1부터 10사이의 수가 적혀진 다섯 장의 카드가 주어진다. 그 중 세 장의 카드를 골라 합을 구한 후 일의 자리 수가 가장 큰 사람이 게임을 이기게 된다. 세 장의 카드가 (7, 8, 10)인 경우에는 합은 7+8+10 = 25가 되고 일의 자리 수는 5가 된다. 어떤 사람이 받은 카드가 (7, 5, 5, 4, 9)인 경우 (7, 4, 9)를 선택하면 합이 20이 되어 일의 자리 수는 0이 되고, (5, 5, 9)를 선택하면 합이 19가 되어 일의 자리 수는 9가 된다. 게임을 이기기 위해서는 세 장의 카드를 선택할 때 그 합의 일의 자리 수가 가장 크게 되도록 선택하여야 한다.

예를 들어, N=3일 때

- 1번 사람이 (7, 5, 5, 4, 9),
- 2번 사람이 (1, 1, 1, 1, 1),
- 3번 사람이 (2, 3, 3, 2, 10)의   
카드들을 받았을 경우, 세 수의 합에서 일의 자리 수가 가장 크게 되도록 세 수를 선택하면

- 1번 사람은 (5, 5, 9)에서 9,
- 2번 사람은 (1, 1, 1)에서 3,
- 3번 사람은 (2, 3, 3)에서 8의  
결과를 각각 얻을 수 있으므로 첫 번째 사람이 이 게임을 이기게 된다.

N명에게 각각 다섯 장의 카드가 주어졌을 때, 세 장의 카드를 골라 합을 구한 후 일의 자리 수가 가장 큰 사람을 찾는 프로그램을 작성하시오. 가장 큰 수를 갖는 사람이 두 명 이상일 경우에는 번호가 가장 큰 사람의 번호를 출력한다.
### **입력**
첫 줄에는 사람의 수를 나타내는 정수 N이 주어진다. N은 2이상 1,000이하이다. 그 다음 N 줄에는 1번부터 N번까지 각 사람이 가진 카드가 주어지는 데, 각 줄에는 1부터 10사이의 정수가 다섯 개씩 주어진다. 각 정수 사이에는 한 개의 빈칸이 있다.
### **출력**
게임에서 이긴 사람의 번호를 첫 번째 줄에 출력한다. 이긴 사람이 두 명 이상일 경우에는 번호가 가장 큰 사람의 번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10
```

**예제 출력1**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
cards = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_sum = 0
result = 0

for i in range(N):
    card = cards[i]
    comb = combinations(card, 3)
    
    temp_max = 0
    for numbers in comb:
        temp_sum = sum(numbers) % 10
        temp_max = max(temp_max, temp_sum)
    
    if temp_max >= max_sum:
        result = i + 1
        max_sum = temp_max

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|489
#### **📝해설**

**알고리즘**
```
1. 구현
```

#### **😅개선점**
1. 변수명을 좀 더 성의있게 짓자

### **다른 풀이**

```python
def solution():
    import sys
    N = int(sys.stdin.readline())
    cards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    p, result = 0, 0
    for idx, card in enumerate(cards):
        for i in range(len(card)):
            for j in range(i+1, len(card)):
                calc = (sum(card) - card[i] - card[j]) % 10
                if calc >= result:
                    result = calc
                    p = idx
    print(p+1)
    
solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
swoos|31120|32|Python3|468
#### **📝해설**

```python
import sys
from itertools import combinations

# 입력받기
N = int(sys.stdin.readline().rstrip())
cards = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 가장 큰 1의 자리
max_sum = 0

# 그 떄의 번호
result = 0

# 모든 사람을 확인하면서
for i in range(N):
    card = cards[i]

    # 가능한 모든 조합을 생성
    comb = combinations(card, 3)
    
    # 모든 조합을 검사하면서 1의자리 최대값을 찾음
    temp_max = 0
    for numbers in comb:
        temp_sum = sum(numbers) % 10
        temp_max = max(temp_max, temp_sum)
    
    # 크거나 같다면 갱신
    if temp_max >= max_sum:
        result = i + 1
        max_sum = temp_max

# 출력
print(result)
```