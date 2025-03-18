# [1991] 트리 순회

### **난이도**
실버 1
## **📝문제**
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

[이미지](https://www.acmicpc.net/JudgeOnline/upload/201007/trtr.png)

예를 들어 위와 같은 이진 트리가 입력되면,

- 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
- 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
- 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)  
가 된다.
### **입력**
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
### **출력**
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
```

**예제 출력1**

```
ABDCEFG
DBAECFG
DBEGFCA
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|585
#### **📝해설**

**알고리즘**
```
1. 트리
```

#### **📝해설**

```python
N = int(input())

# 트리를 딕셔너리의 형태로 저장. key는 노드. value는 (왼쪽 노드, 오른쪽 노드)
tree = {}

# 입력받기
for _ in range(N):
    root, left, right = input().split()
    # 트리를 저장
    tree[root] = (left, right)

# 전위 표기법
def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 표기법
def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

# 후위 표기법
def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
```