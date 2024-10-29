# [7662] 이중 우선순위 큐

### **난이도**
골드 4
## **📝문제**
이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다. 전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.

정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.

Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
### **입력**
입력 데이터는 표준입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 Q에 적용할 연산의 개수를 나타내는 정수 k (k ≤ 1,000,000)가 주어진다. 이어지는 k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어진다. ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다. ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다. 최댓값(최솟값)을 삭제하는 연산에서 최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨을 유념하기 바란다.

만약 Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다. Q에 저장될 모든 정수는 -231 이상 231 미만인 정수이다.
### **출력**
출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 모든 연산을 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라. 두 값은 한 줄에 출력하되 하나의 공백으로 구분하라. 만약 Q가 비어있다면 ‘EMPTY’를 출력하라.
### **예제입출력**

**예제 입력1**

```
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
```

**예제 출력1**

```
EMPTY
333 -45
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_heap = []
    max_heap = []
    visited = [False] * (k + 1)  # 삭제 여부를 추적하기 위한 배열

    for i in range(k):
        operation, num = input().split()
        num = int(num)
        
        if operation == 'I':
            # 삽입 연산
            heapq.heappush(min_heap, (num, i))  # 최소 힙에 삽입
            heapq.heappush(max_heap, (-num, i))  # 최대 힙에 삽입
            visited[i] = True  # 해당 인덱스는 아직 삭제되지 않음
            
        elif operation == 'D':
            if num == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)  # 이미 삭제된 값은 무시
                if max_heap:
                    visited[max_heap[0][1]] = False  # 실제로 삭제
                    heapq.heappop(max_heap)
            elif num == -1:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)  # 이미 삭제된 값은 무시
                if min_heap:
                    visited[min_heap[0][1]] = False  # 실제로 삭제
                    heapq.heappop(min_heap)
    
    # 최종적으로 유효한 값만 남기기 위해서
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|354024|3712|PyPy3|1634
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
```

### **다른 풀이**

```python
def main():
    import io, os, __pypy__
    from array import array
    from collections import defaultdict
    import heapq
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    output = __pypy__.builders.StringBuilder()
    T = int(input())
    for _ in range(T):
        k = int(input())
        maxq = array('i')
        minq = array('i')
        d = defaultdict(int)
        for _ in range(k):
            s = input()
            if s[0] == 68:
                if s[2] == 49:
                    while maxq:
                        e = -heapq.heappop(maxq) - 1
                        if d[e] != 0:
                            d[e] -= 1
                            break
                else:
                    while minq:
                        e = heapq.heappop(minq)
                        if d[e] != 0:
                            d[e] -= 1
                            break
            else:
                n = int(s[2:])
                heapq.heappush(maxq, -n - 1)
                heapq.heappush(minq, n)
                d[n] += 1
        while maxq:
            maxe = -heapq.heappop(maxq) - 1
            if d[maxe] != 0:
                break
        else:
            maxe = None
        while minq:
            mine = heapq.heappop(minq)
            if d[mine] != 0:
                break
        else:
            mine = None
        if maxe == None:
            output.append("EMPTY\n")
        else:
            output.append(str(maxe))
            output.append(' ')
            output.append(str(mine))
            output.append('\n')
    os.write(1, output.build().encode('ascii'))
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|279892|1732|PyPy3|1631