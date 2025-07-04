# [4358] 생태학

### **난이도**
실버 2
## **📝문제**
생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.
### **입력**
프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다. 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.
### **출력**
주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.
### **예제입출력**

**예제 입력1**

```
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
```

**예제 출력1**

```
Ash 13.7931
Aspen 3.4483
Basswood 3.4483
Beech 3.4483
Black Walnut 3.4483
Cherry 3.4483
Cottonwood 3.4483
Cypress 3.4483
Gum 3.4483
Hackberry 3.4483
Hard Maple 3.4483
Hickory 3.4483
Pecan 3.4483
Poplan 3.4483
Red Alder 3.4483
Red Elm 3.4483
Red Oak 6.8966
Sassafras 3.4483
Soft Maple 3.4483
Sycamore 3.4483
White Oak 10.3448
Willow 3.4483
Yellow Birch 3.4483
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import defaultdict

counter = defaultdict(int)
total = 0

for line in sys.stdin:
    tree = line.strip()
    if tree:
        counter[tree] += 1
        total += 1

for tree in sorted(counter):
    print(f"{tree} {counter[tree] / total * 100:.4f}")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34900|464|Python3|276
#### **📝해설**

**알고리즘**
```
1. 문자열
```

### **다른 풀이**

```python
import sys
from collections import Counter

trees = Counter(sys.stdin.read().split("\n"))
del trees[""]
total = sum(trees.values())
for tree, count in sorted(trees.items()):
    print(f"{tree} {100 * count / total:.4f}")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|112996|240|Python3|221
#### **📝해설**

```python
import sys
from collections import defaultdict

# 나무가 몇개인지 세는 딕셔너리
counter = defaultdict(int)
total = 0

# 총 개수가 주어지지않기에 입력을 이런식으로 받음
for line in sys.stdin:

    # 입력받고
    tree = line.strip()

    # 공백이 아니라면
    if tree:

        # 해당나무의 개수를 +1, 전체 개수도 +1
        counter[tree] += 1
        total += 1

# 사전순으로 배치하면서
for tree in sorted(counter):

    # 총 비율을 출력
    print(f"{tree} {counter[tree] / total * 100:.4f}")
```