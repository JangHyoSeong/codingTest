# [1940] 주몽

### **난이도**
실버 4
## **📝문제**
주몽은 철기군을 양성하기 위한 프로젝트에 나섰다. 그래서 야철대장을 통해 철기군이 입을 갑옷을 만들게 하였다. 야철대장은 주몽의 명에 따르기 위하여 연구에 착수하던 중 아래와 같은 사실을 발견하게 되었다.

갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다. 야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다. 이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다. 그리고 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 그리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 갑옷을 만들 수 있는 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
9
2 7 4 1 5 3
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

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
front, rear = 0, N-1

count = 0
while front < rear:
    temp_sum = arr[front] + arr[rear]

    if temp_sum == M:
        count += 1
        front += 1
        rear -= 1
    
    elif temp_sum < M:
        front += 1
    
    else:
        rear -= 1

print(count)    
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|44|Python3|428
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 정렬
arr.sort()

# 투포인터 인덱스 설정
front, rear = 0, N-1

count = 0

# 포인터가 만나기 전까지
while front < rear:

    # 합
    temp_sum = arr[front] + arr[rear]

    # M 이라면 count ++
    if temp_sum == M:
        count += 1

        # 인덱스를 하나씩 옮김
        front += 1
        rear -= 1
    
    # M보다 작다면 더 커져야 하니까 front를 증가
    elif temp_sum < M:
        front += 1
    
    # M보다 크다면 작아져야 하니까 rear를 감소
    else:
        rear -= 1

print(count)    
```