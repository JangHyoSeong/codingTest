# [1039] 교환

### **난이도**
골드 2
## **📝문제**
0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

1 ≤ i < j ≤ M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 만약 연산을 K번 할 수 없으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
16375 1
```

**예제 출력1**

```
76315
```

**예제 입력2**

```
90 4
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
436659 2
```

**예제 출력3**

```
966354
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())
number = [int(digit) for digit in str(N)]
number_len = len(number)

q = deque()
result = set()
used = [set() for _ in range(K+1)]

q.append([number, 0])

while q:
    now_number, count = q.popleft()

    if count == K:
        result.add(int(''.join(map(str, now_number))))
        

    if count < K:
        for i in range(number_len):
            for j in range(i+1, number_len):

                now_number[i], now_number[j] = now_number[j], now_number[i]
                int_number = int(''.join(map(str, now_number)))

                if now_number[0] != 0 and not int_number in used[count+1]:
                    q.append([now_number[:], count+1])
                    used[count+1].add(int_number)

                now_number[i], now_number[j] = now_number[j], now_number[i]

if result:
    print(max(result))
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|114548|132|PyPy3|900
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
n,k = map(int,input().split())
num = []
tmp = n
while tmp:
    num.append(tmp%10)
    tmp //= 10
num.reverse()
if num[1:].count(0) == len(num[1:]) <= 1:
    print(-1)
    exit()

dup = False
for i in num:
    if num.count(i) > 1:
        dup = True
        break

big = sorted(num,reverse=True)

def swap(c,cur,ans):
    if c == 0 or num == big:
        if dup or c & 1 == 0:
            ans = max(ans,make_num(num))
        else:
            ans = max(ans,make_num(num[:-2]+[num[-1],num[-2]]))
        return ans
    while num[cur] == big[cur]:
        cur += 1
        
    bg = max(num[cur+1:])
    for tg,val in enumerate(num[cur+1:],cur+1):
        if val == bg:
            num[cur],num[tg] = num[tg],num[cur]
            ans = swap(c-1,cur+1,ans)
            num[cur],num[tg] = num[tg],num[cur]
    return ans

def make_num(arr):
    ret = 0
    for a in arr:
        ret = ret*10+a
    return ret

print(swap(k,0,0))   
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hwcho98|31120|40|Python3|927
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())
number = [int(digit) for digit in str(N)]
number_len = len(number)

# BFS 사용을 위한 queue 선언
q = deque()

# 모든 교환 후 결과를 저장할 set
result = set()

# 사용 여부를 검사할 집합의 리스트. 각 횟수마다 저장
used = [set() for _ in range(K+1)]

# 초기값 저장
q.append([number, 0])


# BFS 시작
while q:
    now_number, count = q.popleft()

    # 모든 횟수 교환했다면 result에 삽입
    if count == K:
        result.add(int(''.join(map(str, now_number))))
        

    # 아직 교환이 끝나지 않았다면
    if count < K:

        # 모든 자릿수에 대해
        for i in range(number_len):
            for j in range(i+1, number_len):

                # 각 자릿수의 숫자를 바꿈
                now_number[i], now_number[j] = now_number[j], now_number[i]
                int_number = int(''.join(map(str, now_number)))

                # 첫자리가 0인지, 이미 만든 숫자인지 검증
                if now_number[0] != 0 and not int_number in used[count+1]:
                    q.append([now_number[:], count+1])
                    used[count+1].add(int_number)

                # 다시 숫자를 바꿈
                now_number[i], now_number[j] = now_number[j], now_number[i]

if result:
    print(max(result))
else:
    print(-1)
```