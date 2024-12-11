# [18869] 멀티버스 2

### **난이도**
골드 5
## **📝문제**
M개의 우주가 있고, 각 우주에는 1부터 N까지 번호가 매겨진 행성이 N개 있다. 행성의 크기를 알고 있을때, 균등한 우주의 쌍이 몇 개인지 구해보려고 한다. 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다.

두 우주 A와 B가 있고, 우주 A에 있는 행성의 크기는 A1, A2, ..., AN, 우주 B에 있는 행성의 크기는 B1, B2, ..., BN라고 하자. 두 우주의 행성 크기가 모든 1 ≤ i, j ≤ N에 대해서 아래와 같은 조건을 만족한다면, 두 우주를 균등하다고 한다.

- Ai < Aj → Bi < Bj
- Ai = Aj → Bi = Bj
- Ai > Aj → Bi > Bj
### **입력**
첫째 줄에 우주의 개수 M과 각 우주에 있는 행성의 개수 N이 주어진다. 둘째 줄부터 M개의 줄에 공백으로 구분된 행성의 크기가 한 줄에 하나씩 1번 우주부터 차례대로 주어진다.
### **출력**
첫째 줄에 균등한 우주의 쌍의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
2 3
1 3 2
12 50 31
```

**예제 출력1**

```
1
```

**예제 입력2**

```
2 3
1 3 2
12 50 10
```

**예제 출력2**

```
0
```

**예제 입력3**

```
5 3
20 10 30
10 20 60
80 25 79
30 50 80
80 25 81
```

**예제 출력3**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import defaultdict

def count_uniform_universes(M, N, universes):
    # 좌표 압축을 통해 각 우주의 순위 배열을 계산
    def compress(universe):
        sorted_uni = sorted(set(universe))
        rank_map = {value: rank for rank, value in enumerate(sorted_uni)}
        return tuple(rank_map[value] for value in universe)

    # 모든 우주를 압축된 순위 배열로 변환
    compressed_universes = [compress(universe) for universe in universes]

    # 순위 배열을 카운팅하여 균등한 쌍 계산
    freq = defaultdict(int)
    for compressed in compressed_universes:
        freq[compressed] += 1

    # 같은 순위 배열이 나타난 횟수로 균등한 쌍의 개수를 계산
    result = 0
    for count in freq.values():
        if count > 1:
            result += count * (count - 1) // 2  # 조합 계산

    return result

# 입력 처리
M, N = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(M)]

# 균등한 우주의 쌍 계산
result = count_uniform_universes(M, N, universes)
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|169584|592|PyPy3|1100
#### **📝해설**

**알고리즘**
```
1. 좌표 압축
```

### **다른 풀이**

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

def zip_distance(arr):
    distance = {idx:num for num,idx in enumerate(sorted(arr))}
    return ''.join(map(str,[distance[i] for i in arr]))
def check(array):
    cnt = 0
    for idx in array:
        num = array[idx]
        cnt += num * (num - 1) // 2
    return cnt
while 1:
    n,m = map(int,input().split())
    tmp = defaultdict(int)
    for _ in range(n):
        arr = list(map(int,input().split()))
        res = zip_distance(arr)
        tmp[res] += 1
    ans = check(tmp)
    print(ans)
    break
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
zxcv1072|135492|508|PyPy3|583