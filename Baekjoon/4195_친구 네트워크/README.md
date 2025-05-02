# [4195] 친구 네트워크

### **난이도**
골드 2
## **📝문제**
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.
### **입력**
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.
### **출력**
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
### **예제입출력**

**예제 입력1**

```
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
```

**예제 출력1**

```
2
3
4
2
2
4
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
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]

    return size[x_root]

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = {}
    size = {}
    name_to_id = {}
    id_counter = 0

    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()
        for person in [a, b]:
            if person not in name_to_id:
                name_to_id[person] = id_counter
                parent[id_counter] = id_counter
                size[id_counter] = 1
                id_counter += 1

        a_id = name_to_id[a]
        b_id = name_to_id[b]
        print(union(a_id, b_id))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|193068|452|PyPy3|869
#### **📝해설**

**알고리즘**
```
1. 해쉬
2. 유니온파인드
```

### **다른 풀이**

```python
import sys
def find(x):
    if isinstance(parent[x], str):
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    if a != b:
        parent[a] += parent[b]
        parent[b] = a
    return parent[a]

def sol():
    global parent
    data = sys.stdin.read().split("\n")
    idx = 0
    T = int(data[idx])
    result = []
    for _ in range(T):
        idx += 1
        F = int(data[idx])
        parent = {}
        for _ in range(F):
            idx += 1
            a, b = data[idx].split()
            parent.setdefault(a, 1)
            parent.setdefault(b, 1)
            root_a, root_b = find(a), find(b)
            result.append(str(union(root_a, root_b)))
    sys.stdout.write("\n".join(result)+"\n")

sol()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
svhost1466|68780|184|Python3|756
#### **📝해설**

```python
import sys

# 분리집합의 부모 노드를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 집합을 합치는 함수
def union(x, y):
    x_root = find(x)
    y_root = find(y)

    # 부모가 같지 않다면
    if x_root != y_root:
        # 부모 노드를 갱신
        parent[y_root] = x_root
        # 집합의 크기를 더해줌
        size[x_root] += size[y_root]

    # 현재 입력받은 집합의 크기를 리턴
    return size[x_root]

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    F = int(sys.stdin.readline().rstrip())

    # 부모 노드를 저장할 딕셔너리
    parent = {}
    # 각 원소의 집합의 크기를 저장할 딕셔너리
    size = {}
    # 이름을 번호로 인덱싱하기 위한 딕셔너리
    name_to_id = {}
    # 1씩 증가하면서 이름을 번호로 매핑
    id_counter = 0

    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()
        # a, b를 각각 딕셔너리에 매핑
        for person in [a, b]:
            # 이미 입력받은 사람이라면 건너뜀
            if person not in name_to_id:
                name_to_id[person] = id_counter
                parent[id_counter] = id_counter
                size[id_counter] = 1
                id_counter += 1

        # 인덱스로 바꾼 뒤
        a_id = name_to_id[a]
        b_id = name_to_id[b]
        # 합치고 결과를 출력
        print(union(a_id, b_id))

```