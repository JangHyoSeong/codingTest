# [1062] 가르침

### **난이도**
골드 4
## **📝문제**
남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다. 그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 김지민은 K개의 글자를 가르칠 시간 밖에 없다. 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다. 김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다. 둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다. 모든 단어는 중복되지 않는다.
### **출력**
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 6
antarctica
antahellotica
antacartica
```

**예제 출력1**

```
2
```

**예제 입력2**

```
2 3
antaxxxxxxxtica
antarctica
```

**예제 출력2**

```
0
```

**예제 입력3**

```
9 8
antabtica
antaxtica
antadtica
antaetica
antaftica
antagtica
antahtica
antajtica
antaktica
```

**예제 출력3**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations

N, K = map(int, input().split())
words = [input() for _ in range(N)]

essential = {"a", "n", "t", "i", "c"}

if K < 5:
    print(0)
    exit()

mid_parts = []
for word in words:
    mid = word[4:-4]
    mid_parts.append(set(mid) - essential)

max_count = 0
all_chars = set('abcdefghijklmnopqrstuvwxyz') - essential

for comb in combinations(all_chars, K-5):
    teach = set(comb)
    count = 0

    for mid in mid_parts:
        if mid.issubset(teach):
            count += 1
    
    max_count = max(max_count, count)

print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|1748|Python3|572
#### **📝해설**

**알고리즘**
```
1. 백트래킹
2. 비트마스킹
3. 브루트포스 알고리즘
```

### **다른 풀이**

```python
from itertools import combinations

def wordTobit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))

    return bit

# 입력 받기
N, K = map(int, input().split())

words = [input().rstrip() for _ in range(N)]
bits = list(map(wordTobit, words))
base_bit = wordTobit('antic')

# K가 5보다 작으면 a, c, i, n, t를 배우지 못하므로 읽을 수 있는 단어가 없음
if K < 5:
    print(0)
else:

    unlearned = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    max_readable = 0
    # 조합 생성 및 최대 읽을 수 있는 단어 수 계산
    for combo in combinations(unlearned, K - 5):
        know_bit = sum(combo) | base_bit
        readable_count = 0
        for bit in bits:
            if bit & know_bit == bit:
                readable_count += 1
        max_readable = max(max_readable, readable_count)    
    print(max_readable)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
gmdrnr|110460|180|PyPy3|907
#### **📝해설**

```python
from itertools import combinations

N, K = map(int, input().split())
words = [input() for _ in range(N)]

# 단어는 항상 anta, tica를 포함하기에, 항상 a, n, t, i, c를 포함함
essential = {"a", "n", "t", "i", "c"}

# 따라서, K가 5 이하인 경우 항상 답은 0
if K < 5:
    print(0)
    exit()

# 접두사, 접미사를 뺀 나머지 부분을 따로 추출
mid_parts = []
for word in words:
    mid = word[4:-4]

    # antic을 제외하고 사용하는 알파벳을 중복없이 기록
    mid_parts.append(set(mid) - essential)

# 최대로 가르칠 수 있는 단어의 개수
max_count = 0

# 꼭 필요한 알파벳을 제외하고 나머지 알파벳의 집합
all_chars = set('abcdefghijklmnopqrstuvwxyz') - essential


# 가능한 조합을 모두 고려하면서
for comb in combinations(all_chars, K-5):

    # 이 조합일 때 가르칠 수 있는 문자의 개수를 확인
    teach = set(comb)
    count = 0

    for mid in mid_parts:
        if mid.issubset(teach):
            count += 1

    # 최대값 갱신    
    max_count = max(max_count, count)

print(max_count)
```