# [1339] 단어 수학

### **난이도**
골드 4
## **📝문제**
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.
### **입력**
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.
### **출력**
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
AAA
AAA
```

**예제 출력1**

```
1998
```

**예제 입력2**

```
2
GCF
ACDEB
```

**예제 출력2**

```

99437
```

**예제 입력3**

```
10
A
B
C
D
E
F
G
H
I
J
```

**예제 출력3**

```
45
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
words = [input() for _ in range(N)]

weight = {}
for word in words:
    power = len(word) - 1

    for char in word:
        if char in weight:
            weight[char] += 10 ** power
        else:
            weight[char] = 10 ** power
        
        power -= 1
    
sorted_weight = sorted(weight.items(), key=lambda x : x[1], reverse=True)
num = 9
char_to_digit = {}
for char, _ in sorted_weight:
    char_to_digit[char] = num
    num -= 1

total = 0
for word in words:
    number = ''
    for char in word:
        number += str(char_to_digit[char])
    total += int(number)

print(total)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|610
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
arr=[0]*26
for i in range(int(input())):
     s=input()
     for j in range(len(s)):
          arr[ord(s[j])-65]+=10**(len(s)-j-1)
arr.sort(reverse=True)
result=0
for i in range(10):
     result+=arr[i]*(9-i)
print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tomario2485|31120|32|Python3|222
#### **📝해설**

```python
N = int(input())
words = [input() for _ in range(N)]

# 각 알파벳의 가중치를 계산(높은 자릿수에서 나올수록 높음)
weight = {}
for word in words:
    power = len(word) - 1

    for char in word:
        if char in weight:
            weight[char] += 10 ** power
        else:
            weight[char] = 10 ** power
        
        power -= 1

# 가중치가 높은 순서대로 정렬
sorted_weight = sorted(weight.items(), key=lambda x : x[1], reverse=True)

# 가중치가 높은 알파벳부터 높은 숫자를 할당
num = 9
char_to_digit = {}
for char, _ in sorted_weight:
    char_to_digit[char] = num
    num -= 1

# 모든 문자를 확인하면서 숫자로 변환
total = 0
for word in words:
    number = ''
    for char in word:
        number += str(char_to_digit[char])
    total += int(number)

print(total)
```