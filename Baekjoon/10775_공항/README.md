# [10775] 공항

### **난이도**
골드 2
## **📝문제**
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?
### **입력**
첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.

두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.

이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.
### **출력**
승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
3
4
1
1
```

**예제 출력1**

```
2
```

**예제 입력2**

```
4
6
2
2
3
3
4
4
```

**예제 출력2**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)


G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(P)]

parent = list(range(G+1))
count = 0

for plane in arr:
    docking = find(plane)

    if docking == 0:
        break

    union(docking, docking-1)
    count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|41144|140|Python3|471
#### **📝해설**

**알고리즘**
```
1. 분리 집합
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

p = [-1]*(int(input())+1)

def find(x):
    if p[x] < 0: return x
    p[x] = find(p[x])
    return p[x]

def main():
    m = int(input())
    for i in range(m):
        if (xs:= find(int(input()))):
            p[xs] = find(xs-1)
        else:
            print(i)
            exit()

    print(m)

if __name__ == '__main__':
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|34972|88|Python3|375
#### **📝해설**

```python
import sys

# 부모 노드를 찾음
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# x게이트를 사용한다면 x-1 (y)와 연결
def union(x, y):
    parent[find(x)] = find(y)

# 입력받기
G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(P)]

# 부모 노드 리스트
parent = list(range(G+1))
count = 0

# 모든 비행기를 검사
for plane in arr:

    # x게이트를 사용
    docking = find(plane)

    # 사용할 수 있는 게이트가 없다면 종료
    if docking == 0:
        break
    
    # x게이트를 사용 처리(x, x-1을 합침)
    union(docking, docking-1)
    count += 1

print(count)
```