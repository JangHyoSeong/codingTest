# [17245] 서버실

### **난이도**
실버 2
## **📝문제**
서버실은 여러 대의 서버 컴퓨터들을 안정적으로 운영할 수 있는 환경을 유지하기 위해 설치된 공간을 말한다.

이 회사의 서버실은 N×N 칸으로 구분되어 있고, 각 칸마다 서버 랙이 있어 컴퓨터를 여러 대 쌓을 수 있다. 서버가 과열되지 않도록 서버실에는 언제나 냉방기가 작동하고 있다. 그런데 회사가 경제적으로 어려움에 처한 나머지, 서버실의 운영 비용을 줄이기 위해 서버실 내의 컴퓨터 중 절반만 정상적으로 관리하기로 하였다.

냉방기에서 나온 차가운 공기는 서버실의 아래쪽부터 서서히 차오른다. 1분마다 컴퓨터 한 대의 높이만큼 방을 채운다. 이 회사의 서버 컴퓨터는 환경에 매우 민감하여 차가운 공기를 받아야만 동작하고 그렇지 못하면 장애를 일으킨다.

서버실의 컴퓨터 중 절반 이상이 켜지려면 몇 분이 필요할까?
### **입력**
정수 N이 주어진다. (1 ≤ N ≤ 1000)

N×N개의 각 칸에 컴퓨터가 몇 대 쌓여있는지가 입력된다. 한 칸에는 최대 10,000,000대까지 쌓여있을 수 있다.
### **출력**
몇 분이 지나야 전체 컴퓨터의 절반 이상이 장애를 일으키지 않고 동작할 수 있는지 출력한다.
### **예제입출력**

**예제 입력1**

```
5
1 4 0 2 1
0 0 5 6 3
8 4 7 2 0
7 1 0 5 3
4 5 7 9 1
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

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

total = sum(sum(row) for row in table)
half = (total + 1) // 2

left, right = 0, max(max(row) for row in table)
answer = right

while left <= right:
    mid = (left + right) // 2

    count = 0

    for i in range(N):
        for j in range(N):
            count += min(table[i][j], mid)
    
    if count >= half:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120596|476|PyPy3|541
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import sys
n=int(input())
input=sys.stdin.readline
lst=[]
com=0

for i in range(n):
    lst.extend(map(int,input().split(' ')))
com+=sum(lst)
def f(t):
    count=0
    for i in range(n*n):
        count+=min(t,lst[i])
    return count>=(com+1)//2
l,r=0,max(lst)
while l<r:
    p=(l+r)//2
    if f(p):
        r=p
    else:
        l=p+1
print(r)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yubhg|159632|376|PyPy3|346
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 총 컴퓨터 개수
total = sum(sum(row) for row in table)

# 컴퓨터를 냉각해야 하는 개수
half = (total + 1) // 2

# 이분탐색을 위해 최대 최소값 설정
left, right = 0, max(max(row) for row in table)
answer = right

while left <= right:
    mid = (left + right) // 2

    count = 0

    # 모든 위치를 확인하면서 냉각할 컴퓨터를 구함
    for i in range(N):
        for j in range(N):
            count += min(table[i][j], mid)
    
    if count >= half:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
```