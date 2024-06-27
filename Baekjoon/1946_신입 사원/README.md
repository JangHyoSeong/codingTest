# [1946] 신입 사원

### **난이도**
실버 1
## **📝문제**
언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.
### **출력**
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.
### **예제입출력**

**예제 입력1**

```
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
```

**예제 출력1**

```
4
3
```

### **출처**
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2006 D번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

for testcase in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]

    scores.sort()

    count = 1
    min_interview_score = scores[0][1]

    for i in range(1, N):
        if scores[i][1] < min_interview_score:
            count += 1
            min_interview_score = scores[i][1]

    print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|215396|4556|PyPy3|364
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline
T = int(input())

for j in range(T):
    N = int(input())
    
    arr = [0] * N
    for i in range(N):
        x, y = map(int, input().split()) # x, y: 점수 1, 점수 2
        arr[x - 1] = y
    
    num = 1 # 1등 포함하고 시작
    y1 = arr[0] # 직전 선발자 등수
    for i in range(1, N):
        y2 = arr[i]
        if y1 > y2:
            num += 1 
            y1 = y2

    print(num)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sjw0592|126484|740|PyPy3|443
#### **📝해설**

```python
T = int(input())

for testcase in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]

    # 점수를 정렬
    scores.sort()

    # 점수가 가장 큰 사람을 일단 합격
    count = 1

    # 그 후, 최소 면접 점수를 가진 사람을 첫번째 사람으로 일단 초기화
    min_interview_score = scores[0][1]

    # 첫번째를 제외하며 순회
    for i in range(1, N):

        # 만약 현재 점수가 최소점수보다 낮다면
        if scores[i][1] < min_interview_score:
            # 합격자가 한명 늘어남
            count += 1

            # 최소 점수를 갱신
            min_interview_score = scores[i][1]

    print(count)
```