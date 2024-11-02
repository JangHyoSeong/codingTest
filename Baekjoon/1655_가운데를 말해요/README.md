# [1655] 가운데를 말해요

### **난이도**
골드 2
## **📝문제**
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.
### **출력**
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1
5
2
10
-99
7
5
```

**예제 출력1**

```
1
1
2
2
2
2
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush


N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

leftheap, rightheap = [], []
result = []

heappush(leftheap, -numbers[0])
result.append(numbers[0])

for i in range(1, N):
    num = numbers[i]

    if num <= -leftheap[0]:
        heappush(leftheap, -num)
    else:
        heappush(rightheap, num)

    if len(leftheap) > len(rightheap) + 1:
        heappush(rightheap, -heappop(leftheap))
    elif len(leftheap) < len(rightheap):
        heappush(leftheap, -heappop(rightheap))

    result.append(-leftheap[0])

print("\n".join(map(str, result)))

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124124|228|PyPy3|631
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
```

### **다른 풀이**

```python
from sys import stdin, stdout
import heapq as hq
write = stdout.write

n, *s = map(int, stdin.read().split())
# n, *s = [7,   1, 5, 2, 10, -99, 7, 5]
nh, mid, ph = [], s[0], []
ans = [str(s[0])]

if n <= 1:
    write('\n'.join(ans))
    quit(0)

for i in range(2, n, 2):
    if s[i-1] < mid:
        hq.heappush(nh, -s[i-1])
        ans.append(str(-nh[0]))
        if s[i] < mid:
            # hq.heappush(nh, -s[i])
            hq.heappush(ph, mid)
            # mid = -hq.heappop(nh)
            mid = -hq.heappushpop(nh, -s[i])
            ans.append(str(mid))
        else:
            hq.heappush(ph, s[i])
            ans.append(str(mid))
    else:
        hq.heappush(ph, s[i-1])
        ans.append(str(mid))
        if s[i] > mid:
            # hq.heappush(ph, s[i])
            hq.heappush(nh, -mid)
            # mid = hq.heappop(ph)
            mid = hq.heappushpop(ph, s[i])
            ans.append(str(mid))
        else:
            hq.heappush(nh, -s[i])
            ans.append(str(mid))
if n % 2 == 0:
    if s[n-1] < mid:
        hq.heappush(nh, -s[n-1])
        ans.append(str(-nh[0]))
    else:
        ans.append(str(mid))
write('\n'.join(ans))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
leengje|48532|128|Python3|1164
#### **📝해설**

```python
import sys
from heapq import heappop, heappush


N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 중간값 이하의 값을 저장, 중간값 이상의 값을 저장하는 힙
leftheap, rightheap = [], []
result = []

# 짝수라면, 왼쪽에있는걸 뽑기에 leftheap에 저장
# leftheap은 최대힙, rightheap은 최소힙
heappush(leftheap, -numbers[0])

# 일단 초기값은 중간값
result.append(numbers[0])


# 두번째 숫자부터
'''
새로운 숫자가 들어올때마다 leftheap, rightheap의 균형을 유지함.

중간값은 leftheap의 루트값(가장 큰 값)으로 유지
'''
for i in range(1, N):
    num = numbers[i]

    # 이번 숫자가 중간값보다 작다면 leftheap에 push
    if num <= -leftheap[0]:
        heappush(leftheap, -num)

    # 중간값보다 크다면 rightheap에 push
    else:
        heappush(rightheap, num)

    # push이후 leftheap이 rightheap보다 크다면
    if len(leftheap) > len(rightheap) + 1:

        # 균형을 맞추기 위해 rightheap에 push
        heappush(rightheap, -heappop(leftheap))

    # push이후 rightheap이 더 크다면, leftheap에 push
    elif len(leftheap) < len(rightheap):
        heappush(leftheap, -heappop(rightheap))

    # 그 후 중간값을 결과값으로 저장
    result.append(-leftheap[0])

# 출력
print("\n".join(map(str, result)))
```