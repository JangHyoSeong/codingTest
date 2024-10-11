# [9024] 두 수의 합

### **난이도**
골드 5
## **📝문제**
여러 개의 서로 다른 정수 S = {a1, a2, …, an} 와 또 다른 정수 K 가 주어졌을 때, S 에 속하는 서로 다른 두 개의 정수의 합이 K 에 가장 가까운 두 정수를 구하시오. 예를 들어, 10 개의 정수

S = { -7, 9, 2, -4, 12, 1, 5, -3, -2, 0}

가 주어졌을 때, K = 8 에 그 합이 가장 가까운 두 정수는 {12, -4} 이다. 또한 K = 4 에 그 합이 가장 가까운 두 정수는 {-7, 12}, {9, -4}, {5, -2}, {5, 0}, {1, 2} 등의 다섯 종류가 있다.

여러 개의 서로 다른 정수가 주어졌을 때, 주어진 정수들 중에서 서로 다른 두 정수의 합이 주어진 또 다른 정수에 가장 가까운 두 정수의 조합의 수를 계산하는 프로그램을 작성하시오.
### **입력**
프로그램은 표준입력으로 입력을 받는다. 프로그램 입력은 t 개의 테스트 케이스로 구성된다. 입력의 첫 번째 줄에 테스트 케이스의 개수를 나타내는 정수 t 가 주어진다. 두 번째 줄부터 두 줄에 한 개의 테스트 케이스에 해당하는 데이터가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 두 개의 정수 n 과 K (2 ≤ n ≤ 1,000,000, -108 ≤ K ≤ 108 )가 한 개의 공백을 사이에 두고 입력된다. 두 번째 줄에는 n 개의 정수가 하나의 공백을 사이에 두고 주어지며, 각 정수의 최댓값은 108 이고, 최솟값은 -108 이다. 잘못된 데이터가 입력되는 경우는 없다.
### **출력**
출력은 표준출력(standard output)을 사용한다. 입력되는 테스트 케이스의 순서대로 다음 줄에 이어서 각 테스트 케이스의 결과를 출력한다. 각 테스트 케이스의 출력되는 첫 줄에 입력으로 주어진 n 개의 정수들 중에서 서로 다른 두 정수의 합이 주어진 또 다른 정수 K 에 가장 가까운 두 정수의 조합의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
10 8
-7 9 2 -4 12 1 5 -3 -2 0
10 4
-7 9 2 -4 12 1 5 -3 -2 0
4 20
1 7 3 5
5 10
3 9 7 1 5
```

**예제 출력1**

```
1
5
1
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

for testcase in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    count = 0
    min_gap = float('inf')
    front, rear = 0, n-1

    while front < rear:
        sum = arr[front] + arr[rear]
        if abs(k-sum) == min_gap:
            count += 1
        
        elif abs(sum - k) < min_gap:
            min_gap = abs(sum - k)
            count = 1

        if sum == k:
            front += 1
            rear -= 1

        elif sum > k:
            rear -= 1
        else:
            front += 1

    print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|331856|940|PyPy3|593
#### **📝해설**

**알고리즘**
```
1. 투 포인터
2. 이분탐색
```

### **다른 풀이**

```python
import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    """
    n : 서로다른 정수의 개수 
    k : 목표값 
    n_list : 서로다른 정수가 주어지는 리스트 
    left : 왼쪽 포인터 
    right : 오른쪽 포인터 
    app : 근사값(approximation)
    min_error : 오차가 최소인 경우 
    min_error_count : 오차가 최소인 경우의 수
    """

    n, k = map(int, sys.stdin.readline().split())
    n_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

    left = 0
    right = len(n_list) - 1

    min_error = -1
    min_error_count = 0

    while left < right:

        lr = n_list[left] + n_list[right]
        error = abs(k - lr)

        if min_error != -1:
            if error < min_error:
                min_error = error
                min_error_count = 1
            elif error == min_error:
                min_error_count += 1
        else:
            min_error = error
            min_error_count = 1

        # 근사값이 k보다 큰 경우
        if lr > k:
            right -= 1
        # 근사값이 k보다 작은 경우
        else:
            left += 1

    print(min_error_count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
empty6004|339324|928|PyPy3|1204
#### **📝해설**

```python
T = int(input())

for testcase in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # 숫자들을 정렬
    arr.sort()

    # 정답으로 사용할 횟수 카운트 변수
    count = 0

    # 최소 차이를 구할 변수
    min_gap = float('inf')

    # 맨앞, 맨뒤의 인덱스
    front, rear = 0, n-1


    # 앞이 뒤에 겹치기 전까지
    while front < rear:
        # 이번 케이스에서 두 수의 핪
        sum = arr[front] + arr[rear]

        # 만약 최소 차이랑 이번의 차이가 같다면 count++
        if abs(k-sum) == min_gap:
            count += 1
        
        # 최소 차이가 갱신 가능하다면 갱신
        elif abs(sum - k) < min_gap:
            min_gap = abs(sum - k)
            count = 1

        # 차이가 0이라면 앞 뒤 모두 갱신
        if sum == k:
            front += 1
            rear -= 1

        elif sum > k:
            rear -= 1
        else:
            front += 1

    print(count)
```

### **🔖정리**

1. 배운점