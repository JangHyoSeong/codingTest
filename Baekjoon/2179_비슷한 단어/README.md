# [2179] 비슷한 단어

### **난이도**
골드 4
## **📝문제**
N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.

두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정한다. 접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다. 즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우를 구하는 것이다. "AHEHHEH", "AHAHEH"의 접두사는 "AH"가 되고, "AB", "CD"의 접두사는 ""(길이가 0)이 된다.

접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다. 즉, 답으로 S라는 문자열과 T라는 문자열을 출력한다고 했을 때, 우선 S가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력하고, 그런 경우도 여러 개 있을 때에는 그 중에서 T가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력한다.
### **입력**
첫째 줄에 N(2 ≤ N ≤ 20,000)이 주어진다. 다음 N개의 줄에 알파벳 소문자로만 이루어진 길이 100자 이하의 서로 다른 영단어가 주어진다.
### **출력**
첫째 줄에 S를, 둘째 줄에 T를 출력한다. 단, 이 두 단어는 서로 달라야 한다. 즉, 가장 비슷한 두 단어를 구할 때 같은 단어는 제외하는 것이다.
### **예제입출력**

**예제 입력1**

```
9
noon
is
lunch
for
most
noone
waits
until
two
```

**예제 출력1**

```
noon
noone
```

**예제 입력2**

```
4
abcd
abe
abc
abchldp
```

**예제 출력2**

```
abcd
abc
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def common_prefix_length(s1, s2):
    length = min(len(s1), len(s2))
    for i in range(length):
        if s1[i] != s2[i]:
            return i
    return length

N = int(sys.stdin.readline().strip())
words = [(sys.stdin.readline().strip(), i) for i in range(N)]

max_similarity = -1
best_pair = None

for i in range(N - 1):
    for j in range(i + 1, N):
        s1, idx1 = words[i]
        s2, idx2 = words[j]
        similarity = common_prefix_length(s1, s2)

        if similarity > max_similarity:
            max_similarity = similarity
            best_pair = (s1, s2, idx1, idx2)

        elif similarity == max_similarity:
            if idx1 < best_pair[2] or (idx1 == best_pair[2] and idx2 < best_pair[3]):
                best_pair = (s1, s2, idx1, idx2)

print(best_pair[0])
print(best_pair[1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113620|4868|PyPy3|820
#### **📝해설**

**알고리즘**
```
1. 문자열
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    answer = [[words[0], words[1]]]
    words_idx = {word: idx for idx, word in enumerate(words)}
    words.sort()
    max_len = 0

    for i in range(1, n):
        w1, w2 = words[i-1], words[i]
        if len(w1) < max_len or len(w2) < max_len:
            continue
        count = 0
        for x in range(min(len(w1), len(w2))):
            if w1[x] == w2[x]:
                count += 1
            else:
                break
        if count < max_len or count == 0:
            continue

        if count == max_len:
            if answer[-1][-1] == w1:
                answer[-1].append(w2)
            else:
                answer.append([w1, w2])
        elif count > max_len:
            max_len = count
            answer = [[w1, w2]]

    answer_idx = [sorted((words_idx[x], x) for x in lst) for lst in answer]
    answer_idx.sort()

    print(answer_idx[0][0][1])
    print(answer_idx[0][1][1])


solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
to6289|33572|48|Python3|1048
#### **📝해설**

```python
import sys

# 두 문자열에서 공통 부분의 길이를 추출하는 함수
def common_prefix_length(s1, s2):
    length = min(len(s1), len(s2))
    for i in range(length):
        if s1[i] != s2[i]:
            return i
    return length

# 단어를 인덱스와 함께 저장
N = int(sys.stdin.readline().strip())
words = [(sys.stdin.readline().strip(), i) for i in range(N)]

# 최대 유사도와 그 때의 단어 쌍
max_similarity = -1
best_pair = None

# 모든 단어들을 비교
for i in range(N - 1):
    for j in range(i + 1, N):
        s1, idx1 = words[i]
        s2, idx2 = words[j]
        similarity = common_prefix_length(s1, s2)

        if similarity > max_similarity:
            max_similarity = similarity
            best_pair = (s1, s2, idx1, idx2)

        elif similarity == max_similarity:
            if idx1 < best_pair[2] or (idx1 == best_pair[2] and idx2 < best_pair[3]):
                best_pair = (s1, s2, idx1, idx2)

print(best_pair[0])
print(best_pair[1])
```

### **🔖정리**

1. 최적화를 잘하자