# GPT식 숫자 비교

### **난이도**
LV. 2
## **📝문제**
얼마 전 GPT의 실수 비교 방식이 화제가 된 적이 있었다.

질문) "3.9와 3.11 중에 뭐가 더 커?" / 답변) "3.11이 더 큽니다."

수학 시간에 졸지 않은 사람들은 3.9가 3.11보다 크다고 생각하지만, GPT의 눈으로 보면 Python 3.9와 Python 3.11 중 후자를 더 크게 보는 학습 데이터가 많아 저렇게 생각할 수 있다. GPT의 세상에서 3.1은 3보다 크고, 마찬가지로 3.9는 3.2보다 크지만, 3.10은 3.2보다 큰 값으로 처리된다.

구체적으로, 소수점을 기준으로 왼쪽을 수로 읽은 값을 x, 오른쪽을 수로 읽은 값을 y라고 할 때 두 수의 비교가 다음과 같이 이루어진다:

x값이 더 작으면 더 작은 수이다.
x값이 같을 경우 y값이 더 작으면 더 작은 수이다.
소수점이 없는 경우는 같은 수의 소수점이 있는 경우보다 항상 작게 취급된다. (다시 말해, GPT에게 3은 3.0보다 작다.)
N개의 수들이 주어졌을 때, 이를 GPT의 기준에 따라 비내림차순으로 정렬해보자.
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
numbers = [list(map(int, sys.stdin.readline().rstrip().split("."))) for _ in range(N)]

for number in numbers:
    if len(number) == 1:
        number.append(-1)

numbers.sort()

for number in numbers:
    if number[1] != -1:
        print(f'{number[0]}.{number[1]}')
    else:
        print(number[0])
```

#### **📝해설**

**알고리즘**
```
1. 정렬
```

#### **📝해설**

```python
import sys

# 숫자를 소숫점 기준으로 파싱해서 입력
N = int(sys.stdin.readline().rstrip())
numbers = [list(map(int, sys.stdin.readline().rstrip().split("."))) for _ in range(N)]

# 모든 숫자들을 검사해서 소숫점이 없었던 숫자는 반드시 소숫점이 있는 숫자보다 작게끔 -1을 임의로 입력
for number in numbers:
    if len(number) == 1:
        number.append(-1)

# 정렬
numbers.sort()

# 출력
for number in numbers:
    if number[1] != -1:
        print(f'{number[0]}.{number[1]}')
    else:
        print(number[0])
```

### **🔖정리**
