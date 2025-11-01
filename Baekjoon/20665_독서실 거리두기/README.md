# [20665] 독서실 거리두기

### **난이도**
골드 4
## **📝문제**
코로나 바이러스로 사회적 거리두기가 한창이다. 하지만 이러한 시국 이전에도 거리두기가 잘 지켜지던 곳이 있었으니... 바로 독서실이다.

독서실에서 관리자로 근무 중이던 민규는 놀라운 사실을 발견했다. 사람들은 항상 서로 더 멀리 앉으려고 노력한다는 것이었다.

민규는 이러한 사실을 관찰하여 잘 정리해보았다.

1. 사람들은 가장 가까이에 앉아있는 사람이 가장 먼 자리를 선호한다. 만약 독서실을 이용하는 사람이 없다면 좌석번호 1번 자리를 가장 선호한다.
2. 1번 규칙으로 비교할 수 없다면, 가장 먼 좌석들 중에서 좌석 번호가 가장 작은 자리를 선호한다.

독서실 관리자로 오래 근무한 민규에게는 선호하는 좌석이 있다. 하지만 민규는 매우 소심하기 때문에, 사람들이 본인 때문에 이용하고자하는 자리를 이용하지 못하는 일은 피하고 싶다.

민규가 근무하는 독서실은 09:00 부터 21:00 까지 운영되며, 철저히 예약제로 운영되기 때문에 민규는 사람들이 언제부터 언제까지 독서실을 이용하는지 알 수 있다.

이러한 정보를 토대로, 민규는 자신이 선호하는 자리를 얼마나 이용할 수 있는지 계산해보고자 한다.
### **입력**
첫 번째 줄에 독서실 좌석의 개수 N, 독서실 예약자 수 T, 민규가 좋아하는 좌석 번호 P 가 공백으로 구분되어 주어진다. (1 ≤ N ≤ 100, 1 ≤ T ≤ 500, 1 ≤ P ≤ N)

다음 T 개의 줄에는 독서실 입실 시간, 독서실 퇴실 시간이 HHMM HHMM 형태로 입력된다.

(0900 ≤ HHMM ≤ 2100, 0910 0900와 같이 퇴실 시간이 입실 시간보다 빠른 경우는 없다)
### **출력**
민규가 선호하는 좌석을 이용할 수 있는 시간이 총 몇분인지 출력하시오.

### **제한**
독서실의 모든 좌석은 비어있는 상태로 시작한다.

독서실 예약이 같은 시각에 시작된다면 짧은 이용시간을 가진 사람을 먼저 앉힌다.

독서실 예약 리스트에 있는 예약자들이 좌석이 없어서 못 앉는 상태는 존재하지 않는다.

민규는 선호하는 좌석을 얼마나 이용할 수 있는지 계산하고 싶어하는 것이기 때문에 예약인원들이 자리를 이용하는 것에 영향을 주지 않는다.
### **예제입출력**

**예제 입력1**

```
5 6 1
0915 0930
0940 2040
0910 0920
2040 2050
2043 2047
2044 2046
```

**예제 출력1**

```
40
```

**예제 입력2**

```
8 6 3
2000 2020
2020 2030
0900 2100
0910 2100
0920 2100
0930 2000
```

**예제 출력2**

```
720
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def to_min(t):
    h, m = int(t[:2]), int(t[2:])
    return h * 60 + m

N, T, P = map(int, input().split())
arr = []

for _ in range(T):
    s, e = input().split()
    arr.append((to_min(s), to_min(e)))

arr.sort(key=lambda x : (x[0], x[1] - x[0]))

seats = [0] * (N + 1)
P_occupied = [False] * 1260

for start, end in arr:
    now = start
    occupied = [i for i in range(1, N+1) if seats[i] > now]

    best_seat, best_dist = 0, -1
    for seat in range(1, N+1):
        if seats[seat] > now:
            continue

        dist = min([abs(seat - o) for o in occupied], default=N)
        if dist > best_dist:
            best_dist, best_seat = dist, seat
    
    seats[best_seat] = end
    if best_seat == P:
        for t in range(start, end):
            P_occupied[t] = True
    
total_time = 720
used_time = sum(P_occupied[540:1260])
print(total_time - used_time)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|84|Python3|870
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
n,t,p=map(int,input().split())

time=[]
for _ in range(t): # 시 분으로 되어 있는 것을 분 단위로 바꾼다.
    s,e=map(int,input().split())
    s=s//100*60+s%100
    e=e//100*60+e%100
    time.append((s,e)) # 시 분으로 바꿔준다.

time.sort() # 시간기준으로 정렬해준다.
ans=60*12 # 독서실 운영시간이 09:00~21:00라고 했으니 초기변수 최대 12시간으로 설정해둔다

def find_seat(arr): # 앉을 자리 선택
    if not arr:
        return 1    
    candidate=[] # 앉을 자리 후보
    if arr[0][0] !=1: # 1번 좌석이 비어 있는 경우
        candidate.append((arr[0][0]-1,1)) # (거리, 좌석번호)

    if arr[-1][0] !=n: # 마지막 n번이 비어있는 경우
        candidate.append((n-arr[-1][0],n)) # (가장끝-현재 거리, 좌석번호)
        
     # 사용 중인 좌석들 사이의 빈 공간 확인
    for i in range(1, len(arr)):
        # 현재 좌석과 이전 좌석 사이의 거리
        distance = arr[i][0] - arr[i-1][0]
        
        # 거리가 2 이상이면 중간에 앉을 수 있음 # 바로 옆이면은 중간에 앉을 수가 없다 
        if distance > 1:
            # 중간 좌석 계산 (중간에 여러 좌석이 있을 경우 거리의 절반 위치)
            mid_seat = arr[i-1][0] + distance // 2
            # 후보 목록에 (거리의 절반, 중간 좌석) 추가
            candidate.append((distance // 2, mid_seat))

    # 조건에 맞는 자리 1자리만 리턴    
    return sorted(candidate,key=lambda x:(-x[0],x[1]))[0][1] # 첫번쨰 기준: 거리가 큰 순서대로(-x[0]), 두 번째 기준: 좌석번호가 작은 순서대로(x[1])

used=[]

for s,e in time:
    new_used=[] # 현재(시간: s) 사용중인 좌석
    for u in used: # 퇴실한 좌석 걸러내기 
        if u[1]>s: 
            new_used.append(u)
    res=find_seat(new_used)
    if res==p: # 민규가 좋아하는 자리에 누가 앉음
        ans-=(e-s) # 총 앉아 있을 수 있는 시간에서 다른 사람이 차지하고 있는 시간을 뺴서 총 앉아있을 수 있는 시간을 고른다
    new_used.append((res,e)) # 
    used=sorted(new_used)

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jmjung1997|32412|52|Python3|2194
#### **📝해설**

```python

# 시간을 분단위로 변경
def to_min(t):
    h, m = int(t[:2]), int(t[2:])
    return h * 60 + m

N, T, P = map(int, input().split())
arr = []

# 입력받기
for _ in range(T):
    s, e = input().split()
    arr.append((to_min(s), to_min(e)))

# 정렬(시작 시간, 점유 시간 기준 오름차순)
arr.sort(key=lambda x : (x[0], x[1] - x[0]))

# 좌석이 언제까지 점유중인지 나타낼 리스트
seats = [0] * (N + 1)

# 선호좌석이 얼마나 사용 가능한지 저장할 리스트
P_occupied = [False] * 1260

# 점유 시간을 확인하면서
for start, end in arr:

    # 기존의 점유 좌석들이 사용가능한 상태인지 확인
    now = start
    occupied = [i for i in range(1, N+1) if seats[i] > now]

    # 현재 사람이 앉을 자리를 확인
    best_seat, best_dist = 0, -1
    for seat in range(1, N+1):

        # 이미 사람이 있는 자리는 넘어감
        if seats[seat] > now:
            continue
        
        # 현재 자리에서 가장 먼 자리를 구함
        dist = min([abs(seat - o) for o in occupied], default=N)
        if dist > best_dist:
            best_dist, best_seat = dist, seat
    
    # 이 자리에 그 시간동안 앉음
    seats[best_seat] = end

    # 선호 좌석에 누군가 앉는다면 그 동안에는 자리를 못앉음
    if best_seat == P:
        for t in range(start, end):
            P_occupied[t] = True

# 총 시간(9:00 ~ 21:00)
total_time = 720
# 선호좌석이 비어있던 시간
used_time = sum(P_occupied[540:1260])
print(total_time - used_time)
```