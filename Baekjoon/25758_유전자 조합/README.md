# [25758] 유전자 조합

### **난이도**
실버 1
## **📝문제**
서울과기대 학생들은 실험을 하다가 처음보는 생물의 유전자를 발견했다. 이 유전자는 형질 두 개로 나타낼 수 있고 형질은 대문자 알파벳으로 나타낼 수 있다. 유전자는 다른 유전자와 조합할 수 있는데, 두 유전자를 조합하면 첫 번째 유전자의 첫 번째 형질과 두 번째 유전자의 두 번째 형질이 붙은 다음 세대 유전자가 생긴다. 유전자의 두 형질에 있는 알파벳 중 사전순으로 같거나 큰 알파벳을 유전자의 표현형이라고 하자.

 
$N$개의 1세대 유전자가 주어졌을 때 이들은 서로 다른 모든 1세대 유전자들과 조합할 수 있다. 조합을 통해 생긴 2세대 유전자의 표현형으로 가능한 알파벳의 수와 그 알파벳을 구해보자.
### **입력**
첫 번째 줄에 유전자의 개수 
$N$이 주어진다. (
$2 \le N \le 100\,000$)

두 번째 줄에는 1세대 유전자 
$N$개가 공백으로 구분되어 주어진다.
### **출력**
첫 번째 줄에 2세대 유전자의 표현형으로 가능한 알파벳 수를 출력한다.

두 번째 줄에는 2세대 유전자의 표현형을 알파벳 순서대로 정렬 후 공백으로 구분하여 출력한다.
### **예제입출력**

**예제 입력1**

```
3
AB DC XP
```

**예제 출력1**

```
4
C D P X
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
genoms = input().split()

phenotypes = set()

for x in range(ord('A'), ord('Z') + 1):
    x_char = chr(x)
    count = 0

    for genom in genoms:
        if genom[0] == x_char:
            count += 1

    if count > 1:
        for genom in genoms:
            phenotypes.add(max(x_char, genom[1]))
    elif count == 1:
        for genom in genoms:
            if genom[0] != x_char:
                phenotypes.add(max(x_char, genom[1]))

sorted_phenotypes = sorted(phenotypes)

print(len(sorted_phenotypes))
print(" ".join(sorted_phenotypes))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|38608|616|Python3|560
#### **📝해설**

**알고리즘**
```
1. 집합
```

### **다른 풀이**

```python
N = int(input())
arr = input().split()
valid = [0] * 26
for i in range(N):
    n0 = ord(arr[i][0]) - 65
    if not valid[n0]:
        for j in range(N):
            if i != j and arr[j][1] <= arr[i][0]:
                valid[n0] = 1
                break
    n1 = ord(arr[i][1]) - 65
    if not valid[n1]:
        for j in range(N):
            if i != j and arr[j][0] <= arr[i][1]:
                valid[n1] = 1
                break
ans = []
for i in range(26):
    if valid[i]:
        ans.append(chr(i + 65))
print(len(ans))
print(*ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
danamusukana|38580|76|Python3|540
#### **📝해설**

```python
N = int(input())
genoms = input().split()

# 2세대 유전자를 담을 집합
phenotypes = set()

# 모든 케이스에 대해 반복할 필요 없이 알파벳으로 순회를 하면 됨
for x in range(ord('A'), ord('Z') + 1):
    x_char = chr(x)
    count = 0

    # 현재 알파벳이 포함되어있다면
    for genom in genoms:
        if genom[0] == x_char:
            count += 1

    if count > 1:
        for genom in genoms:
            phenotypes.add(max(x_char, genom[1]))
    elif count == 1:
        for genom in genoms:
            if genom[0] != x_char:
                phenotypes.add(max(x_char, genom[1]))

sorted_phenotypes = sorted(phenotypes)

print(len(sorted_phenotypes))
print(" ".join(sorted_phenotypes))
```