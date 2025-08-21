# [13164] 행복 유치원

### **난이도**
골드 5
## **📝문제**
행복 유치원 원장인 태양이는 어느 날 N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나누려고 한다. 각 조에는 원생이 적어도 한 명 있어야 하며, 같은 조에 속한 원생들은 서로 인접해 있어야 한다. 조별로 인원수가 같을 필요는 없다.

이렇게 나뉘어진 조들은 각자 단체 티셔츠를 맞추려고 한다. 조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다. 최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다. 태양이를 도와 최소의 비용을 구하자.
### **입력**
입력의 첫 줄에는 유치원에 있는 원생의 수를 나타내는 자연수 N(1 ≤ N ≤ 300,000)과 나누려고 하는 조의 개수를 나타내는 자연수 K(1 ≤ K ≤ N)가 공백으로 구분되어 주어진다. 다음 줄에는 원생들의 키를 나타내는 N개의 자연수가 공백으로 구분되어 줄 서 있는 순서대로 주어진다. 태양이는 원생들을 키 순서대로 줄 세웠으므로, 왼쪽에 있는 원생이 오른쪽에 있는 원생보다 크지 않다. 원생의 키는 109를 넘지 않는 자연수이다.
### **출력**
티셔츠 만드는 비용이 최소가 되도록 K개의 조로 나누었을 때, 티셔츠 만드는 비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
1 3 5 6 10
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heapify, heappop

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

gaps = [-(arr[i+1] - arr[i]) for i in range(N-1)]
heapify(gaps)

for _ in range(K-1):
    heappop(gaps)

print(-sum(gaps))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|169084|368|PyPy3|285
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
def main():
    import io, os  # isort: skip
    from itertools import pairwise

    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    darr = [a2 - a1 for a1, a2 in pairwise(arr)]
    darr.sort()

    ans = sum(darr[: n - k])
    print(ans, flush=True)

    os._exit(0)  # type: ignore


main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|64380|164|Python3|406
#### **📝해설**

```python
import sys
from heapq import heapify, heappop

# 입력받기
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 각 원소간의 차이를 배열로 저장
gaps = [-(arr[i+1] - arr[i]) for i in range(N-1)]

# 최대 힙으로 만듦
heapify(gaps)

# K개 조를 만든다면, K-1개 만큼 차이를 무시할 수 있음
for _ in range(K-1):
    heappop(gaps)

print(-sum(gaps))
```