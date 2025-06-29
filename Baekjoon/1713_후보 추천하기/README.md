# [1713] 후보 추천하기

### **난이도**
실버 1
## **📝문제**
월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
5. 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 사진틀의 개수 N이 주어진다. (1 ≤ N ≤ 20) 둘째 줄에는 전체 학생의 총 추천 횟수가 주어지고, 셋째 줄에는 추천받은 학생을 나타내는 번호가 빈 칸을 사이에 두고 추천받은 순서대로 주어진다. 총 추천 횟수는 1,000번 이하이며 학생을 나타내는 번호는 1부터 100까지의 자연수이다.
### **출력**
사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력한다.
### **예제입출력**

**예제 입력1**

```
3
9
2 1 4 3 5 6 2 7 2
```

**예제 출력1**

```
2 6 7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
M = int(input())
arr = list(map(int, input().split()))

frame = dict()

for t, student in enumerate(arr):
    if student in frame:
        frame[student][0] += 1
    else:
        if len(frame) == N:
            to_remove = min(frame.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del frame[to_remove]
        frame[student] = [1, t]

print(' '.join(map(str, sorted(frame.keys()))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|410
#### **📝해설**

**알고리즘**
```
1. 구현
2. 집합과 맵
```

### **다른 풀이**

```python
def solution():
    n = int(input()) # 액자 수  1 <= n <= 20
    candidate = int(input()) # 전체 학생의 추천 수 <= 1000
    vote = list(map(int, input().split())) # 추천한 후보 1 <= x <= 100
    result = []
    cnt = []

    for i in vote:
        if i in result:
            cnt[result.index(i)] += 1
        else:
            if len(result) >= n:
                idx = cnt.index(min(cnt))
                del result[idx]
                del cnt[idx]
            result.append(i)
            cnt.append(1)

    result.sort()
    print(' '.join(map(str, result)))

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sfeorthdln92|31120|32|Python3|591
#### **📝해설**

```python
N = int(input())
M = int(input())
arr = list(map(int, input().split()))

# 현재 액자에 어떤 학생이 걸려있는지 저장할 딕셔너리
# key : 학생 번호, value : [추천 수, 게시 시간]
frame = dict()

# 추천 목록을 검사하면서
for t, student in enumerate(arr):

    # 이미 액자에 존재한다면 추천수를 하나 늘림
    if student in frame:
        frame[student][0] += 1
    
    # 액자에 존재하지 않다면
    else:

        # 그리고 액자가 가득 차있다면
        if len(frame) == N:
            # 추천수가 적은 숫자대로, 그리고 가장 오래된 순서 기준으로 최소값을 제거
            to_remove = min(frame.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del frame[to_remove]
        
        # 액자에 추가
        frame[student] = [1, t]

# 출력
print(' '.join(map(str, sorted(frame.keys()))))
```