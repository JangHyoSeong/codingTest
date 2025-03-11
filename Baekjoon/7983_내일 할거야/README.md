# [7983] 내일 할거야

### **난이도**
골드 5
## **📝문제**
아 과제 하기 싫다. 아무 것도 안 하고 싶다. 더 적극적이고 격렬하게 아무 것도 안 하고 싶다.

있잖아. 내가 아까 책상에다가 n개의 과제 목록을 적어놨어. 각각의 과제 i는 di 일이 걸리고, 오늘로부터 ti 일 안에 끝내야 해. 그러니까 오늘이 0일이면, ti일이 끝나기 전에 제출이야. 과제는 한번 시작하면 쉬지 않고 계속해야 해. 안 그러면 머리 아파 지거든.

근데 있잖아. 내가 지금 너무, 너무 아무 것도 안 하고 싶어. 그래서 오늘은 아무 것도 안 할 거야. 더 중요한 게 뭔지 알아? 사실 나 내일도, 모레도, 아무 것도 안 하고 싶어. 한 며칠 동안은 계속 아무 것도 안하려고. 아. 과제가 있을 때 내가 내일부터 연속으로 최대 며칠동안 놀 수 있는지 궁금하다. 궁금하긴 한데, 난 아무 것도 안 하고 싶어.

좋은 생각이 났다. 너희가 이걸 대신 구해주면, 내가 너희의 맞은 문제 수를 하나 올려줄게.
### **입력**
첫째 줄에는 과제의 개수인 정수 n (1 ≤ n ≤ 106)이 주어진다.

이후 n개의 줄에 각각의 과제를 나타내는 두 정수 di, ti (1 ≤ di, ti ≤ 109)가 순서대로 주어진다. 오늘은 0일이다.

모든 입력에 대해, 오늘 아무 것도 안 해도 과제를 마무리 할 수 있는 방법이 존재함이 보장된다.
### **출력**
내일(1일)부터 연속으로 최대 며칠 동안 놀 수 있는지를 출력한다. 가령, 답이 0이면, 내일 과제를 해야 하며, 1 이면, 모레에 과제를 해야 한다.
### **예제입출력**

**예제 입력1**

```
3
2 8
1 13
3 10
```

**예제 출력1**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
homeworks = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

homeworks.sort(key= lambda x : -x[1])

answer = homeworks[0][1]

for d, t in homeworks:
    answer = min(answer, t) - d

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|269072|2072|PyPy3|272
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    tasks = []
    for _ in range(n):
        d, t = map(int, input().split())
        tasks.append((d, t))
    tasks.sort(key=lambda x: x[1], reverse=True)
    res = tasks[0][1]
    for d, t in tasks:
        if t < res:
            res = t
        res -= d
    print(res)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|176320|1712|Python3|362
#### **📝해설**

```python
import sys

# 입력받기
N = int(sys.stdin.readline().rstrip())
homeworks = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 과제를 마감일 기준으로 내림차순 정렬
homeworks.sort(key= lambda x : -x[1])

# 쉴 수 있는 날을 큰 값으로 설정
answer = homeworks[0][1]

# 과제를 마감일 내림차순 기준으로 순회하면서
for d, t in homeworks:

    # 최대로 쉴 수 있는 날을 갱신
    answer = min(answer, t) - d

print(answer)
```