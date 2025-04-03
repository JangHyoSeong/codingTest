# [19538] 루머

### **난이도**
골드 4
## **📝문제**
당신은 루머를 믿는가?

한 유명 심리학 실험에서는 사람들에게 두 개의 줄을 보여주고, 어떤 줄이 더 긴지 말하라 했다. 사실 한 사람을 제외하고 나머지는 실험자에 의해 사전에 조작된 사람들이었다. 조작된 사람들은 사실상 더 짧은 줄을 더 길다고 말했다. 주변 모두가 같은 답변을 하자, 진짜 피실험자 또한 짧은 줄이 더 길다고 말했다. 이 실험은 사람들이 주변인의 영향을 강하게 받는다는 것을 보여주었는데, 루머도 이와 같다.

루머는 최초 유포자로부터 시작한다. 최초 유포자는 여러 명일 수 있고, 최초 유포자를 제외하고 스스로 루머를 만들어 믿는 사람은 없다.

매분 루머를 믿는 사람은 모든 주변인에게 루머를 동시에 퍼트리며, 군중 속 사람은 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿는다.

루머를 믿는 순간부터 다른 말은 듣지 않기 때문에, 한번 믿은 루머는 계속 믿는다.

이때, 사람들이 루머를 처음 믿기 시작하는 시간을 알아내 보자.
### **입력**
첫째 줄에 사람의 수 
$N$이 주어진다. (
$1 \leq N \leq 200\ 000$) 이는 
$1$번 사람부터 
$N$번 사람까지 있음을 의미한다.

둘째 줄부터 
$N$개의 줄이 주어진다. 이 중 
$i(1 \leq i \leq N)$번째 줄에는 
$i$번 사람의 주변인들의 번호와 입력의 마지막을 나타내는 0이 공백으로 구분되어 주어진다. 번호는 
$1$ 이상 
$N$ 이하의 자연수이고, 같은 줄에 중복된 번호는 없다. 자기 자신이 주변인이거나 일방적으로 주변인인 경우는 없으며, 전체 양방향 주변인 관계는 
$1\ 000\ 000$개를 넘지 않는다.

다음 줄에는 루머를 퍼뜨리는 최초 유포자의 수 
$M$이 주어진다. 
$(1 \leq M \leq N)$ 

마지막 줄에는 최초 유포자의 번호가 공백으로 구분되어 주어진다. 최초 유포자의 번호는 중복되지 않는다.
### **출력**
 
$N$개의 정수 
$t_1,t_2,\cdots,t_N$을 공백 단위로 출력한다. 
$t_i$는 
$i$번 사람이 루머를 처음 믿기 시작한 시간(분)이며, 충분히 많은 시간이 지나도 루머를 믿지 않을 경우 
$-1$이다. 최초 유포자는 루머를 
$0$분부터 믿기 시작했다고 생각한다.
### **예제입출력**

**예제 입력1**

```
7
2 3 0
1 3 0
1 2 4 0
3 5 0
4 0
0
0
2
1 6
```

**예제 출력1**

```
0 1 2 3 4 0 -1
```

**예제 입력2**

```
7
2 4 0
1 3 0
2 5 0
1 5 6 0
3 4 6 7 0
4 5 7 0
5 6 0
1
6
```

**예제 출력2**

```
4 4 3 3 2 0 1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    edges[i] = list(map(int, sys.stdin.readline().rstrip().split()[:-1]))

M = int(sys.stdin.readline().rstrip())
start = list(map(int, sys.stdin.readline().rstrip().split()))

result = [-1] * (N + 1)
believe_count = [0] * (N + 1)

q = deque()
for person in start:
    result[person] = 0
    q.append(person)

while q:
    now = q.popleft()

    for next in edges[now]:
        if result[next] == -1:
            believe_count[next] += 1

            if believe_count[next] >= (len(edges[next]) + 1) // 2:
                result[next] = result[now] + 1
                q.append(next)

print(" ".join(map(str, result[1:])))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|193408|608|PyPy3|765
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N + 1)]

# 마지막 0을 빼고 주변인을 입력받음
for i in range(1, N + 1):
    edges[i] = list(map(int, sys.stdin.readline().rstrip().split()[:-1]))

# 루머 유포자 입력
M = int(sys.stdin.readline().rstrip())
start = list(map(int, sys.stdin.readline().rstrip().split()))

# 결과값 (유포까지 걸린 시간)
result = [-1] * (N + 1)

# 주변인 중 루머를 믿는 사람의 숫자
believe_count = [0] * (N + 1)

# BFS를 위해 queue선언, 루머 유포자를 0으로 초기화
q = deque()
for person in start:
    result[person] = 0
    q.append(person)

# BFS
while q:
    now = q.popleft()

    # 주변인들을 검사하면서
    for next in edges[now]:

        # 아직 루머를 믿지 않는다면, 주변인 루머유포자를 ++
        if result[next] == -1:
            believe_count[next] += 1

            # 주변인의 절반 이상이 루머를 믿는다면 큐에 추가
            if believe_count[next] >= (len(edges[next]) + 1) // 2:
                result[next] = result[now] + 1
                q.append(next)

# 출력
print(" ".join(map(str, result[1:])))
```