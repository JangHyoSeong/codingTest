# [9081] 단어 맞추기

### **난이도**
실버 1
## **📝문제**
BEER라는 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬하게 되면

BEER
BERE
BREE
EBER
EBRE
EEBR
EERB
ERBE
EREB
RBEE
REBE
REEB
와 같이 된다. 이러한 순서에서 BEER 다음에 오는 단어는 BERE가 된다. 이와 같이 단어를 주면 그 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬할 때에 주어진 단어 다음에 나오는 단어를 찾는 프로그램을 작성하시오.
### **입력**
입력의 첫 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 하나의 단어가 한 줄로 주어진다. 단어는 알파벳 A~Z 대문자로만 이루어지며 항상 공백이 없는 연속된 알파벳으로 이루어진다. 단어의 길이는 100을 넘지 않는다.
### **출력**
각 테스트 케이스에 대해서 주어진 단어 바로 다음에 나타나는 단어를 한 줄에 하나씩 출력하시오. 만일 주어진 단어가 마지막 단어이라면 그냥 주어진 단어를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
HELLO
DRINK
SHUTTLE
ZOO
```

**예제 출력1**

```
HELOL
DRKIN
SLEHTTU
ZOO
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
words = [list(input()) for _ in range(N)]

for word in words:
    i = len(word) - 1

    while i > 0 and word[i-1] >= word[i]:
        i -= 1
    
    if i == 0:
        print("".join(map(str, word)))
        continue

    j = len(word) - 1
    while word[i-1] >= word[j]:
        j -= 1

    word[i-1], word[j] = word[j], word[i-1]
    word[i:] = sorted(word[i:])
    
    print("".join(map(str, word)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|32|Python3|421
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
for z in [*open(0)][1:]:
    s = list(z.strip())
    for i in range(len(s)-1,0,-1):
        if s[i-1] < s[i]:
            break
    else:
        print(''.join(s))
        continue
    for j in range(len(s)-1,i-2,-1):
        if s[i-1] < s[j]:
            break
    s[i-1],s[j] = s[j],s[i-1]
    s[i:] = s[i:][::-1]
    print(''.join(s))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
codebabo|30616|32|Python3|337
#### **📝해설**

```python
N = int(input())
words = [list(input()) for _ in range(N)]

for word in words:

    # 단어의 맨 마지막 인덱스
    i = len(word) - 1

    # 뒤에서 부터 검사하면서 오름차순이 유지될때까지 인덱스를 감소
    # 오름차순이 유지되지 않는 구간의 인덱스를 저장하게 됨
    while i > 0 and word[i-1] >= word[i]:
        i -= 1
    
    # 단어가 끝까지 내림차순이라면 사전순으로 맨 마지막
    if i == 0:

        # 그대로 출력
        print("".join(map(str, word)))
        continue
    
    # 다시 뒤에서부터 검사
    j = len(word) - 1

    # i-1의 값보다 큰 값 j를 찾음
    while word[i-1] >= word[j]:
        j -= 1

    # 찾은 위치의 문자를 바꿈
    word[i-1], word[j] = word[j], word[i-1]

    # 나머지 문자는 사전순 배열이 되도록 정렬
    word[i:] = sorted(word[i:])
    
    print("".join(map(str, word)))
```