# [2343] 기타 레슨

### **난이도**
실버 1
## **📝문제**
강토는 자신의 기타 강의 동영상을 블루레이로 만들어 판매하려고 한다. 블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다. 순서가 뒤바뀌는 경우에는 강의의 흐름이 끊겨, 학생들이 대혼란에 빠질 수 있기 때문이다. 즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.

강토는 이 블루레이가 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다. 오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다. 이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다. 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다. 각 강의의 길이는 10,000분을 넘지 않는다.
### **출력**
첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.
### **예제입출력**

**예제 입력1**

```
9 3
1 2 3 4 5 6 7 8 9
```

**예제 출력1**

```
17
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def minimum_bluray_size(n, m, lessons):
    def can_divide(size):
        count = 1
        total = 0
        for lesson in lessons:
            if total + lesson > size:
                count += 1
                total = lesson
                if count > m:
                    return False
            else:
                total += lesson
        return True
    
    left = max(lessons)
    right = sum(lessons)
    
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

print(minimum_bluray_size(n, m, lessons))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42204|224|Python3|719
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import sys
from bisect import bisect_right

input = sys.stdin.read


def sol2343():
    n, m, *seq = map(int, input().split())
    s, e = max(seq), sum(seq)
    for i in range(n - 1):
        seq[i + 1] += seq[i]
    while s <= e:
        mid = (s + e) // 2
        if simulate(seq, mid, m):
            e = mid - 1
        else:
            s = mid + 1
    return e + 1


def simulate(seq, size, m):
    sub = 0
    for _ in range(m):
        sub = seq[bisect_right(seq, size + sub) - 1]
        if sub == seq[-1]:
            break
    return True if sub == seq[-1] else False


if __name__ == '__main__':
    print(sol2343())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
scala0114|43908|76|Python3|629
#### **📝해설**

```python
def minimum_bluray_size(n, m, lessons):
    def can_divide(size):
        count = 1
        total = 0
        for lesson in lessons:
            # 이번 강의를 더했을때, 정해둔 크기보다 크다면
            if total + lesson > size:
                # 강의의 개수 +1
                count += 1
                # 크기를 늘림
                total = lesson

                # 나눌수없으면 False
                if count > m:
                    return False
            
            # 정해둔 크기보다 작다면 추가
            else:
                total += lesson
        
        # 나눌 수 있음
        return True
    
    # 최소, 최대값을 선언
    left = max(lessons)
    right = sum(lessons)
    

    # 이분탐색
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

print(minimum_bluray_size(n, m, lessons))
```