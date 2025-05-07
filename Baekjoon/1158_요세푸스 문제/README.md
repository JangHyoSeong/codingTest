# [1158] 요세푸스 문제

### **난이도**
실버 4
## **📝문제**
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
### **출력**
예제와 같이 요세푸스 순열을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 3
```

**예제 출력1**

```
<3, 6, 2, 7, 5, 1, 4>
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())

q = deque(range(1, N+1))

count = 0
result = []
while q:
    temp = q.popleft()
    count += 1

    if count == K:
        result.append(temp)
        count = 0
    else:
        q.append(temp)

print("<" + ", ".join(map(str, result)) + ">")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|227068|448|PyPy3|306
#### **📝해설**

**알고리즘**
```
1. 큐
```

### **다른 풀이**

```python
n, k=map(int,input().split())
li=[i for i in range(1,n+1)]
answer,num=[],0
while len(answer)!=n:
    num=(num+(k-1))%len(li)
    answer.append(li.pop(num))
print('<'+", ".join(map(str,answer))+'>')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
luckisstick0220|31120|32|Python3|207
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())

# 큐에 1 ~ N 까지 숫자를 저장
q = deque(range(1, N+1))

count = 0
result = []

# 큐가 빌때까지 반복
while q:
    temp = q.popleft()
    count += 1

    # K번 빼냈다면
    if count == K:
        # 큐에 다시 집어넣지 않고 결과에 저장
        result.append(temp)
        # 빼낸 횟수를 초기화
        count = 0
    # 아직 K가 되지 않았다면 큐에 다시 삽입
    else:
        q.append(temp)

# 출력
print("<" + ", ".join(map(str, result)) + ">")
```