# 문제 제목
두 원 사이의 정수 쌍
## **📝문제 설명**
x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개 주어집니다. 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 return하도록 solution 함수를 완성해주세요.  
※ 각 원 위의 점도 포함하여 셉니다.
### **⚠제한사항**
1 ≤ r1 < r2 ≤ 1,000,000
### **입출력 예**
|r1|r2|result|
|:--:|:--:|:--:|
|2|3|20|
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**

### **🧾나의 풀이**

```python
from math import sqrt, ceil

def solution(r1, r2):
    answer = 0

    for i in range(1, r2):
        big = int(sqrt(r2**2 - i**2))

        if i < r1:
            small = ceil(sqrt(r1**2 - i**2))
            
        else:
            small = 0

        answer += big - small + 1
    
    answer += 1
    return answer * 4
```

#### **📝해설**
- 처음에는 BFS, 그리고 반복문으로 풀려고 했다
- 하지만 그러면 시간제한에 걸리게 되어서, 수학적 계산을 통해 계산하기로 했다
- 특히 원을 사분면 기준으로 4분의 1등분 하여 한 쪽 사분면만 개수를 구한 뒤 *4를 하였다

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181187)**<br/>