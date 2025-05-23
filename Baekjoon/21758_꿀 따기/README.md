# [21758] 꿀 따기

### **난이도**
골드 5
## **📝문제**
아래와 같이 좌우로 
$N$개의 장소가 있다.

[이미지](https://upload.acmicpc.net/7eac9e04-f000-482d-9ad5-05cc2363df05/-/preview/)

장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다. 또, 다른 한 장소를 골라서 벌통을 둔다. 아래 그림에서 연한 회색의 장소는 벌이 있는 장소이고 진한 회색의 장소는 벌통이 있는 장소이다.

[이미지](https://upload.acmicpc.net/8ca82402-c379-40cd-902d-9ecc24c35d1f/-/preview/)

두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다. 각 장소에 적힌 숫자는 벌이 지나가면서 꿀을 딸 수 있는 양이다.

두 마리가 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀을 딴다. (벌통이 있는 장소에서도 같다.)
벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
위의 그림과 같이 배치된 경우 두 마리의 벌 모두 
$4 + 1 + 4 + 9 + 9 = 27$의 꿀을 따서, 전체 꿀의 양은 54가 된다.

[이미지](https://upload.acmicpc.net/a9794fde-7a1b-4c4d-82b5-f1b8e7daaa73/-/preview/)

위의 그림과 같이 배치된 경우 왼쪽 장소에서 출발한 벌은 
$9 + 4 + 4 + 9 + 9 = 35$의 꿀을 따고 오른쪽 장소에서 출발한 벌은 
$4 + 9 + 9 = 22$의 꿀을 따므로, 전체 꿀의 양은 
$57$이 된다.

[이미지](https://upload.acmicpc.net/5b264635-fc6b-498a-af76-bbe08197ab32/-/preview/)

위의 그림과 같은 경우는 전체 꿀의 양이 31이 된다.

장소들의 꿀 양을 입력으로 받아 벌들이 딸 수 있는 가능한 최대의 꿀의 양을 계산하는 프로그램을 작성하라.
### **입력**
첫 번째 줄에 장소의 수 
$N$이 주어진다.

다음 줄에 왼쪽부터 각 장소에서 꿀을 딸 수 있는 양이 공백 하나씩을 사이에 두고 주어진다.
### **출력**
첫 번째 줄에 가능한 최대의 꿀의 양을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
9 9 4 1 4 9 9
```

**예제 출력1**

```
57
```

**예제 입력2**

```
7
4 4 9 1 9 4 4
```

**예제 출력2**

```
54
```

**예제 입력3**

```
3
2 5 4
```

**예제 출력3**

```
10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

max_honey = 0

for i in range(2, N):
    max_honey = max(max_honey, (prefix[N] - arr[0] - arr[i - 1]) + (prefix[N] - prefix[i]))
    max_honey = max(max_honey, (prefix[i] - arr[0]) + (prefix[N - 1] - prefix[i - 1]))
    max_honey = max(max_honey, prefix[i - 1] + (prefix[N - 1] - arr[i - 1]))

print(max_honey)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124388|116|PyPy3|499
#### **📝해설**

**알고리즘**
```
1. 누적합
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    n = int(input())
    a = [*map(int, input().split())]
    s, mx = sum(a), 0
    
    right = (s-a[0]-a[1])<<1
    if right > mx: mx = right
    for i in range(2, n-1):
        right += a[i-1]
        right -= a[i]<<1
        if right > mx: mx = right
    
    left = (s-a[-1]-a[-2])<<1
    if left > mx: mx = left
    for i in range(n-3, 0, -1):
        left += a[i+1]
        left -= a[i]<<1
        if left > mx: mx = left
    
    mid = s-a[0]-a[-1]
    for i in range(1, n-1):
        if mid+a[i] > mx: mx = mid+a[i]
    
    print(mx)

if __name__ == "__main__": main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|43248|88|Python3|666
#### **📝해설**

```python
import sys

input = sys.stdin.readline

# 입력
N = int(input())
arr = list(map(int, input().split()))

# 누적합을 미리 구함
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# 최대 꿀
max_honey = 0

# 세가지 케이스를 고려(벌, 벌, 벌통), (벌, 벌통, 벌), (벌통, 벌, 벌)
for i in range(2, N):
    max_honey = max(max_honey, (prefix[N] - arr[0] - arr[i - 1]) + (prefix[N] - prefix[i]))
    max_honey = max(max_honey, (prefix[i] - arr[0]) + (prefix[N - 1] - prefix[i - 1]))
    max_honey = max(max_honey, prefix[i - 1] + (prefix[N - 1] - arr[i - 1]))

print(max_honey)
```