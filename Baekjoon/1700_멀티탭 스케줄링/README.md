# [1700] 멀티탭 스케줄링

### **난이도**
골드 1
## **📝문제**
기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기
키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.
### **입력**
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.
### **출력**
하나씩 플러그를 빼는 최소의 횟수를 출력하시오.
### **예제입출력**

**예제 입력1**

```
2 7
2 3 2 3 1 2 7
```

**예제 출력1**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
used = [False] * (K+1)
now = []

for i in range(K):
    if len(now) < N:
        if not used[arr[i]]:
            now.append(arr[i])
            used[arr[i]] = True

    else:
        if used[arr[i]]:
            continue
        
        last_used = -1
        device_to_unplug = -1
        for num in now:
            if num not in arr[i:]:
                device_to_unplug = num
                break
        
            else:
                next_use = arr[i:].index(num)
                if next_use > last_used:
                    last_used = next_use
                    device_to_unplug = num

        now.remove(device_to_unplug)
        now.append(arr[i])
        used[device_to_unplug] = False
        used[arr[i]] = True
        count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|36|Python3|848
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys


input = sys.stdin.readline

n, k = map(int, input().split())

order = list(map(int, input().split()))
count = dict()

mt = set()
answer = 0

for i, cur in enumerate(order):
    if cur in mt or len(mt) < n:
        mt.add(cur)
    else:
        visited = set()
        candidate = -1
        for nxt in order[i + 1:]:
            if nxt in mt and nxt not in visited:
                visited.add(nxt)
                candidate = nxt
        for _ in mt:
            if _ not in visited:
                mt.remove(_)
                break
        else:
            mt.remove(candidate)
        mt.add(cur)

        answer += 1

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
aa248424|31120|28|Python3|652
#### **📝해설**

```python
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 플러그 뽑은 횟수
count = 0

# 현재 사용하고있는 기기
used = [False] * (K+1)

# 현재 사용하고 있는 기기
now = []

# 스케줄링을 확인하면서
for i in range(K):

    # 아직 플러그가 다 꼽히지 않았다면
    if len(now) < N:

        # 사용하고 있지 않은 기기라면
        if not used[arr[i]]:

            # 플러그를 꼽음
            now.append(arr[i])
            used[arr[i]] = True

    # 플러그가 다 꼽혀있다면
    else:

        # 만약 이미 꼽혀있는 기기라면 넘어감
        if used[arr[i]]:
            continue
        
        # 
        last_used = -1

        # 뽑을 기기의 번호
        device_to_unplug = -1

        # 현재 플러그에 꼽혀있는 기기를 순회하면서
        for num in now:

            # 만약 이 뒤에 사용하지 않는다면 이걸뽑음
            if num not in arr[i:]:

                # 뽑을 기기의 번호를 이걸로 갱신
                device_to_unplug = num
                break
            
            # 만약 기기들을 이 뒤에 모두 사용한다면
            else:
                # 다음번 사용시 인덱스
                next_use = arr[i:].index(num)

                # 만약 기존보다 더 늦게 사용한다면
                if next_use > last_used:

                    # 갱신
                    last_used = next_use
                    device_to_unplug = num

        # 플러그에서 꽂고 뽑는 로직
        now.remove(device_to_unplug)
        now.append(arr[i])
        used[device_to_unplug] = False
        used[arr[i]] = True
        count += 1

# 출력
print(count)
```