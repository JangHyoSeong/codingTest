# [1342] 행운의 문자열

### **난이도**
실버 1
## **📝문제**
민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.
### **입력**
첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 10이고, 알파벳 소문자로만 이루어져 있다.
### **출력**
첫째 줄에 위치를 재배치해서 얻은 서로 다른 행운의 문자열의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
aabbbaa
```

**예제 출력1**

```
1
```

**예제 입력2**

```
ab
```

**예제 출력2**

```
2
```

**예제 입력3**

```
aaab
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import Counter

S = input()
counter = Counter(S)
result = 0

path = []

stack = [(path, counter)]

while stack:
    current_path, current_counter = stack.pop()

    if len(current_path) == len(S):
        result += 1
        continue

    for char in current_counter:
        if current_counter[char] > 0:
            if current_path and current_path[-1] == char:
                continue
        
            next_path = current_path + [char]
            next_counter = current_counter.copy()
            next_counter[char] -= 1
            
            stack.append((next_path, next_counter))

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119336|4124|PyPy3|626
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
from collections import Counter

# 문자열 입력
S = input().strip()

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if len(S) == len(set(S)):
    print(factorial(len(S)))
else:
    counter = Counter(S)
    
    memo = {}

    def backtrack(prev, counts):
        if sum(counts.values()) == 0:
            return 1
        
        key = (prev, tuple(sorted(counts.items())))
        if key in memo:
            return memo[key]
        
        total = 0
        for c in counts:
            if counts[c] > 0 and c != prev:
                counts[c] -= 1
                total += backtrack(c, counts)
                counts[c] += 1
        
        memo[key] = total
        return total
    
    print(backtrack('', counter))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
nomiro76|36048|96|Python3|767
#### **📝해설**

```python
from collections import Counter

S = input()
counter = Counter(S)
result = 0

path = []

# 현재까지 만든 문자열을 저장할 스택
stack = [(path, counter)]

while stack:
    current_path, current_counter = stack.pop()

    # 문자열을 끝까지 만들었다면
    if len(current_path) == len(S):

        # ++
        result += 1
        continue

    # 문자열을 아직 다 만들지 못했다면 만듦
    for char in current_counter:
        if current_counter[char] > 0:

            # 이웃한 문자와 같다면 고려하지 않음
            if current_path and current_path[-1] == char:
                continue
        
            next_path = current_path + [char]
            next_counter = current_counter.copy()
            next_counter[char] -= 1
            
            stack.append((next_path, next_counter))

print(result)
```