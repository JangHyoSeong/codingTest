# [31264] 사격

### **난이도**
골드 5
## **📝문제**
성현이네 부대의 24-1분기 사격 훈련이 시작되었다!

성현이네 부대의 사격 훈련장에는 
$N$개의 표적이 있으며, 그중 
$i$번째 표적의 점수는 
$s_i$이다. 점수가 
$s_i$인 표적을 맞히기 위해선 사격 실력이 최소 
$s_i$ 이상이어야 한다. 만약 해당 표적을 성공적으로 맞혔다면, 표적의 점수만큼 사격 점수를 획득하며 사격 실력도 동일한 만큼 증가한다.

이번 사격 훈련에서는 최대 
$M$번 사격할 수 있으며, 성현이가 진급에 성공하기 위해서는 획득한 사격 점수의 총합이 
$A$점 이상이어야 한다.

사격 훈련을 시작하기 전 초기 사격 점수는 
$0$점이다. 성현이는 항상 자신이 맞힐 수 있는 표적 중 얻을 수 있는 사격 점수가 가장 높은 표적을 맞히며, 동일한 표적을 여러 번 맞히는 것도 가능하다.

진급이 절실했던 성현이는 사격 훈련이 시작하기 전 초기 사격 실력이 어느 정도여야 진급에 성공할 수 있을지 궁금해하고 있다. 성현이를 위해, 진급에 성공하기 위한 초기 사격 실력의 최솟값을 구해주자. 항상 진급에 성공할 수 있는 경우만 입력으로 주어진다.
### **입력**
첫 번째 줄에 표적의 개수 
$N$, 성현이의 최대 사격 횟수 
$M$과 진급에 필요한 최소 사격 점수를 나타내는 정수 
$A$가 공백으로 구분되어 주어진다.

두 번째 줄에 표적의 점수를 의미하는 
$N$개의 정수 
$s_1, \cdots, s_n$이 공백으로 구분되어 주어진다.
### **출력**
성현이가 진급할 수 있는 초기 사격 실력의 최솟값을 구하여라.
### **예제입출력**

**예제 입력1**

```
5 3 10
2 4 5 1 3
```

**예제 출력1**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M, A = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
left, right = 1, arr[N-1]

answer = A
while left <= right:
    mid = (left + right) // 2

    idx = 0
    now_shoot = mid
    now_score = 0
    for count in range(M):
        if now_shoot < arr[0]:
            break

        while idx + 1 < N and arr[idx + 1] <= now_shoot:
            idx += 1
        
        now_shoot += arr[idx]
        now_score += arr[idx]
    
    if now_score < A:
        left = mid + 1
    
    else:
        answer = mid
        right = mid - 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|122608|152|PyPy3|630
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
2. 그리디 알고리즘
```

#### **😅개선점**

1. 이분탐색 범위를 잘못잡아서 많이 틀렸다. 다음부터는 꼼꼼히 확인하자

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M, A = map(int, input().split())
s=  list(map(int, input().split()))
sett=0
s.sort()
S= 1
E = max(s)

def f(sett):
    val=0
    arr=sett
    idx=0
    er=False
    for i in range(M):
        if s[idx]>arr:
            er=True
            break
        while idx<N-1 and s[idx+1]<=arr:
            idx+=1
        arr+=s[idx]
        val+=s[idx]
    if er:
        return -1
    return val
        
while S<E:
    sett = (S+E)//2
    val=f(sett)
    if val>A:
        E = sett-1
    elif val<A:
        S = sett+1
    else:
        E=S=sett

for i in range(max(E-2, 1), E+2):
    if f(i)>=A:
        print(i)
        break
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
0318top|122660|148|PyPy3|663
#### **📝해설**

```python
import sys

N, M, A = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 표적을 오름차순으로 정렬
arr.sort()

# 이분탐색을 위한 최대, 최소값 정의
# 최소는 1, 최대는 표적중 최대값
left, right = 1, arr[N-1]

# 정답으로 사용할 값
answer = A

# 이분탐색 시작
while left <= right:
    mid = (left + right) // 2

    # 현재 어느 표적까지 사격 가능한지 나타낼 인덱스
    idx = 0

    # 현재 사격 실력, 현재 점수
    now_shoot = mid
    now_score = 0

    # M번 사격
    for count in range(M):

        # 아무런 표적도 맞출 수 없다면 이 케이스는 고려하지 않음
        if now_shoot < arr[0]:
            break
        
        # 현재 사격 실력으로 쏠 수 있는 최대값의 표적을 찾음
        while idx + 1 < N and arr[idx + 1] <= now_shoot:
            idx += 1
        
        # 사격
        now_shoot += arr[idx]
        now_score += arr[idx]
    
    # A를 넘기지 못한다면 값을 증가시켜 다시 확인
    if now_score < A:
        left = mid + 1
    
    # A 이상이라면 정답을 갱신하고 값을 줄여서 확인
    else:
        answer = mid
        right = mid - 1

print(answer)
```