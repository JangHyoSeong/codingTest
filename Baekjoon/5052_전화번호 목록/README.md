# [5052] 전화번호 목록

### **난이도**
골드 4
## **📝문제**
전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.

전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

- 긴급전화: 911
- 상근: 97 625 999
- 선영: 91 12 54 26  
이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다.
### **입력**
첫째 줄에 테스트 케이스의 개수 t가 주어진다. (1 ≤ t ≤ 50) 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. (1 ≤ n ≤ 10000) 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다. 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.
### **출력**
각 테스트 케이스에 대해서, 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.
### **예제입출력**

**예제 입력1**

```
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
```

**예제 출력1**

```
NO
YES
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
    numbers.sort()
    flag = True
    for i in range(N-1):
        if numbers[i+1].startswith(numbers[i]):
            flag = False
            break

    print("YES" if flag else "NO")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|136|Python3|371
#### **📝해설**

**알고리즘**
```
1. 정렬
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def check(pn_list):
    # 사전 순으로 정렬하게 되면 접두어가 되는 전화번호는 항상 인접하게 위치 ->  바로 다음 번호만 확인하면 됨
    pn_list.sort()
    # 문자열 길이로 정렬할 필요없음 
    # pn_list.sort(key = lambda x: len(x))
    for i in range(len(pn_list)-1):
        if pn_list[i] == pn_list[i+1][:len(pn_list[i])]:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    pn_list = [ input().rstrip() for _ in range(n) ]
    
    print(check(pn_list))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dydrbs159|32140|120|Python3|598
#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
    # 전화번호를 정렬. 문자열을 정렬했으니, 만약 접두어가 같다면 붙어있게됨
    numbers.sort()
    flag = True
    for i in range(N-1):
        if numbers[i+1].startswith(numbers[i]):
            flag = False
            break

    print("YES" if flag else "NO")

```