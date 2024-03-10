# [2606] 바이러스

### **난이도**
실버3
## **📝문제**
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.


어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
### **출력**
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

**예제 출력1**

```
4
```

### **출처**
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 초등부 3번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
num_of_computers = int(input())
N = int(input())


graph = [[] for _ in range(num_of_computers+1)]
visited = [False] * (num_of_computers+1)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1
stack = [1]
visited[1] = True

while stack:
    now = stack.pop()
    count += 1

    for i in graph[now]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|48|Python3|460
#### **📝해설**

**알고리즘**
```
1.그래프
2.DFS
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

a = int(input())

b = int(input())

b_lst = []

result = set()
for i in range(b) :
    num = list(map(int,input().split()))
    if 1 in num :
        result.add(num[0])
        result.add(num[1])
    else :
        b_lst.append(num)
    
while True :
    for i in b_lst :
        if i[0] in result :
            result.add(i[1])
            b_lst.remove(i)
            break
        elif i[1] in result :
            result.add(i[0])
            b_lst.remove(i)
            break
    else :
        break


print(len(result) - 1 )
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
obk0502|31388|40|Python3|590