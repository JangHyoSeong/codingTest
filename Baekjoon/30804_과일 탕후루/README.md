# [30804] 과일 탕후루

### **난이도**
실버 2
## **📝문제**
은하는 긴 막대에 
$N$개의 과일이 꽂혀있는 과일 탕후루를 만들었습니다. 과일의 각 종류에는 
$1$부터 
$9$까지의 번호가 붙어있고, 앞쪽부터 차례로 
$S_1, S_2, \cdots, S_N$번 과일이 꽂혀있습니다. 과일 탕후루를 다 만든 은하가 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었습니다.

탕후루를 다시 만들 시간이 없었던 은하는, 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다. 앞에서 
$a$개, 뒤에서 
$b$개의 과일을 빼면 
$S_{a+1}, S_{a+2}, \cdots, S_{N-b-1}, S_{N-b}$번 과일, 총 
$N-(a+b)$개가 꽂혀있는 탕후루가 됩니다. 
$(0 \le a, b;$ 
$a+b < N)$ 

이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.
### **입력**
첫 줄에 과일의 개수 
$N$이 주어집니다. 
$(1 \le N \le 200\,000)$ 

둘째 줄에 탕후루에 꽂힌 과일을 의미하는 
$N$개의 정수 
$S_1, \cdots, S_N$이 공백으로 구분되어 주어집니다. 
$(1 \le S_i \le 9)$ 
### **출력**
문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.
### **예제입출력**

**예제 입력1**

```
5
5 1 1 2 1
```

**예제 출력1**

```
4
```

**예제 입력2**

```
3
1 1 1
```

**예제 출력2**

```
3
```

**예제 입력3**

```
9
1 2 3 4 5 6 7 8 9
```

**예제 출력3**

```
2
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
fruits = list(map(int, input().split()))

count_arr = [0] * 10
front = 0
max_length = 0
unique_count = 0

for rear in range(N):
    if count_arr[fruits[rear]] == 0:
        unique_count += 1
    count_arr[fruits[rear]] += 1

    while unique_count > 2:
        count_arr[fruits[front]] -= 1
        if count_arr[fruits[front]] == 0:
            unique_count -= 1
        front += 1
    
    current_length = rear - front + 1
    max_length = max(max_length, current_length)

print(max_length)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34600|192|Python3|509
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    S = tuple(map(int, input().split()))
    res = i = 0
    cnt_list = [0]*10
    current = set()
    for j in range(N):
        cnt_list[S[j]] += 1
        current.add(S[j])
        if len(current) > 2:
            while 1:
                cnt_list[S[i]] -= 1
                if cnt_list[S[i]] == 0:
                    current.remove(S[i])
                    i += 1
                    break
                i += 1
        if j-i+1 > res:
            res = j-i+1
    print(res)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|34480|120|Python3|570
#### **📝해설**

```python
N = int(input())
fruits = list(map(int, input().split()))

# 어떤 숫자가 몇 개 있는지 세는 카운터배열
count_arr = [0] * 10

# 앞부분부터 시작하는 인덱스
front = 0

# 최대 크기를 저장할 변수
max_length = 0

# 과일의 종류가 몇개인지 셀 변수
unique_count = 0


# 뒤에서 부터 순회하면서
for rear in range(N):

    # 만약 뒤에서부터 셌을 때 없는 과일이라면 과일의 종류 += 1
    if count_arr[fruits[rear]] == 0:
        unique_count += 1
    count_arr[fruits[rear]] += 1

    while unique_count > 2:
        count_arr[fruits[front]] -= 1
        if count_arr[fruits[front]] == 0:
            unique_count -= 1
        front += 1
    
    current_length = rear - front + 1
    max_length = max(max_length, current_length)

print(max_length)
```