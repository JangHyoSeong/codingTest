# [10868] 최솟값

### **난이도**
골드 1
## **📝문제**
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.

여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최솟값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.
### **입력**
첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.
### **출력**
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
```

**예제 출력1**

```
5
38
20
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2*node + 1, start, mid)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end)
        tree[node] = min(tree[2*node + 1], tree[2*node + 2])

def query_segment_tree(tree, node, start, end, left, right):
    if right < start or end < left:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_min = query_segment_tree(tree, 2*node + 1, start, mid, left, right)
    right_min = query_segment_tree(tree, 2*node + 2, mid+1, end, left, right)
    return min(left_min, right_min)

N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
tree = [0] * (4*N)
build_segment_tree(numbers, tree, 0, 0, N-1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(query_segment_tree(tree, 0, 0, N-1, a-1, b-1)))
    sys.stdout.write("\n")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|135576|984|PyPy3|1125
#### **📝해설**

**알고리즘**
```
1. 세그먼트 트리
2. 희소 배열
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

tree_height = 0
length = n

while length != 0:
    length //= 2
    tree_height += 1

tree_size = pow(2, tree_height + 1)

left_node_start_index = (tree_size // 2) - 1
tree = [sys.maxsize] * (tree_size+1)

for i in range(left_node_start_index+1,left_node_start_index+n+1):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        if tree[i//2] > tree[i]:
            tree[i//2] = tree[i]
        i -= 1

def get_sum(s,e):
    part_sum = sys.maxsize
    # 탐색종료 조건
    while s <= e:
        if s % 2 == 1:
            part_sum = min(tree[s],part_sum)
            s += 1
        if e % 2 == 0:
            part_sum = min(tree[e],part_sum)
            e -= 1
        # 부모 노드로 이동
        s = s//2
        e = e//2
    return part_sum

set_tree(tree_size-1) #초기 트리 생성

for _ in range(m):
    s, e = map(int,input().split())
    s = s + left_node_start_index
    e = e + left_node_start_index
    print(get_sum(s,e))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
bbqdnr|115536|236|PyPy3|1033
#### **📝해설**

```python
import sys

# 세그먼트 트리 구축
def build_segment_tree(arr, tree, node, start, end):

    # 리프노드인 경우
    if start == end:
        # 노드의 값을 트리에 삽입
        tree[node] = arr[start]

    # 리프노드가 아닌 경우
    else:

        # 가운데 값을 기준으로 왼쪽, 오른쪽을 나눔
        mid = (start + end) // 2

        # 자식 노드의 값을 재귀적으로 구함
        build_segment_tree(arr, tree, 2*node + 1, start, mid)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end)

        # 두 개의 자식 노드 중 최소값을 노드에 저장
        tree[node] = min(tree[2*node + 1], tree[2*node + 2])

# 구간 최소값 쿼리 (left, right == 찾고자 하는 범위)
def query_segment_tree(tree, node, start, end, left, right):
    # 범위를 벗어나면 inf 반환(최소값 계산을 위함)
    if right < start or end < left:
        return float('inf')

    # 찾고자 하는 범위가 주어진 값보다 넓은경우 현재 노드를 반환 (리프 노드)
    if left <= start and end <= right:
        return tree[node]
    
    # 가운데 노드의 인덱스를 구함
    mid = (start + end) // 2

    # 왼쪽 노드의 최소값을 재귀적으로 구함
    left_min = query_segment_tree(tree, 2*node + 1, start, mid, left, right)

    # 오른쪽 노드의 최소값을 재귀적으로 구함
    right_min = query_segment_tree(tree, 2*node + 2, mid+1, end, left, right)

    # 구한 값 중 최소값을 리턴
    return min(left_min, right_min)

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 트리의 크기 할당 (2**(트리의 높이 + 1) 이상이면 충분)
tree = [0] * (4*N)

# 트리 생성
build_segment_tree(numbers, tree, 0, 0, N-1)

# 쿼리 출력
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(query_segment_tree(tree, 0, 0, N-1, a-1, b-1)))
    sys.stdout.write("\n")
```

### **🔖정리**

1. 배운점