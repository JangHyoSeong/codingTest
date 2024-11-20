# [2470] 두 용액

### **난이도**
골드 5
## **📝문제**
KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
### **출력**
첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
-2 4 -99 -1 98
```

**예제 출력1**

```
-99 98
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

arr.sort()
front, rear = 0, N-1

min_gap = 21e8
x, y = 0, N-1
while front < rear:
    new_gap = arr[front] + arr[rear]

    if min_gap > abs(new_gap):
        min_gap = abs(new_gap)
        x, y = front, rear

    if new_gap == 0:
        x, y = front, rear
        break

    elif new_gap > 0:
        rear -= 1
    
    else:
        front += 1


print(arr[x], arr[y])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124060|124|PyPy3|426
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
def sol(arr):
    s = 0
    e = len(arr) - 1
    mini = float('inf')
    nearest = [0] * 2

    while s != e:
        a = arr[s] + arr[e]
        b = -a if a < 0 else a

        if b < mini:
            mini = b
            nearest[0], nearest[1] = s, e
        
        if a < 0:
            s += 1
        else:
            e -= 1

    return arr[nearest[0]], arr[nearest[1]]


input()
arr = sorted(map(int, input().split()))

print(*sol(arr))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
power16one5|42036|72|Python3|446
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# 정렬
arr.sort()

# 투포인터 사용
front, rear = 0, N-1

# 최소 차이 초기화
min_gap = 21e8

# 최소 차이 일 때 인덱스
x, y = 0, N-1

# 투포인터 탐색
while front < rear:

  # 현재 차이
    new_gap = arr[front] + arr[rear]

  # 최소 차이가 갱신 가능하다면 갱신
    if min_gap > abs(new_gap):
        min_gap = abs(new_gap)
        x, y = front, rear

  # 만약 차이가 0이라면 탐색종료
    if new_gap == 0:
        x, y = front, rear
        break

  # 현재 0보다 크다면 rear를 줄임
    elif new_gap > 0:
        rear -= 1
  
  # 현재 0보다 작다면 front를 키움
    else:
        front += 1


print(arr[x], arr[y])
```