# [9324] 진짜 메시지

### **난이도**
실버 4
## **📝문제**
스파이들은 사령부와 통신하기 위해서 SMTP(비밀 메시지 전송 프로토콜)를 사용해 비밀 회선으로 전자 메시지를 보낸다. 메시지가 적들에 의해 조작되어 보내진 것이 아닌 진짜 메시지라는 것을 표시하기 위해 모든 메시지는 회선에 노이즈가 있었거나 발신 측에서 손을 떨면서 메시지를 보낸 것처럼 변형되는데, 이 변형 알고리즘은 메시지를 가로채는 자들이 우연히 변형 규칙을 흉내 낼 수 없을 정도로 정교하다. 또한 요원들의 머리에 총구가 겨눠져 강제로 메시지를 말한 경우 간단히 실수를 의도적으로 넣어 이 메시지가 강제로 쓰인 메시지라는 것을 알려줄 수 있다.

알고리즘대로 정확하게 변형된 메시지는 각 문자가 세 번째 등장할 때 한 번 더 문자가 삽입된다. 예를 들면 요원이 "HELLOTHEREWELLBEFINE" 라는 메시지를 보내고 싶어 했다면 "HELLOTHEREEWELLLBEFINEE" 는 정확한 변형이다. 몇 년 동안 이 메시지들의 진짜 여부는 고도로 훈련된 원숭이들이 판별해내었다. 그러나 사령부에 도착하는 메시지들의 양이 많이 늘어나면서 이 작업을 자동으로 처리해주는 프로그램을 고안하기로 하였다.
### **입력**
첫째 줄에 100 이하의 테스트 케이스의 개수가 주어진다. 그리고 각 테스트 케이스마다

대문자로만 이루어진 10만자 이하의 문자열 M이 한 줄에 주어진다. 이 문자열은 검사해야할 메시지다.
### **출력**
테스트 케이스마다

메시지 M이 진짜 메시지면 “OK”를, 가짜 메시지면 “FAKE”를 한 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
3
BAPC
AABA
ABCABCBBAAACC
```

**예제 출력1**

```
3
BAPC
AABA
ABCABCBBAAACC
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    message = sys.stdin.readline().rstrip()
    count_char = [0] * 26

    i = 0
    while i < len(message):
        c = message[i]
        alphabet = ord(c) - ord("A")
        count_char[alphabet] += 1

        if count_char[alphabet] == 3:
            if i+1 < len(message):
                if message[i+1] != message[i]:
                    print("FAKE")
                    break
                else:
                    count_char[alphabet] = 0
                    i += 1
            else:   
                print("FAKE")
                break
        i += 1
    else:
        print("OK")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111008|156|PyPy3|673
#### **📝해설**

**알고리즘**
```
1. 문자열
```

#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    # 입력받기
    message = sys.stdin.readline().rstrip()
    
    # 각 알파벳이 등장한 횟수를 리스트로 저장
    count_char = [0] * 26

    # 문자열을 순회하기 위한 인덱스
    i = 0

    # 문자열을 검사
    while i < len(message):
        c = message[i]
        alphabet = ord(c) - ord("A")
        count_char[alphabet] += 1

        # 만약 한 알파벳이 세번 등장했다면
        if count_char[alphabet] == 3:

            # 인덱스를 벗어나지 않는지 먼저 검사
            if i+1 < len(message):

                # 세번 등장했을 때, 다음 글자와 동일하지 않다면 가짜
                if message[i+1] != message[i]:
                    print("FAKE")
                    break
                # 동일하다면 갯수를 초기화하고 건너뜀
                else:
                    count_char[alphabet] = 0
                    i += 1
            # 인덱스를 벗어난다면 가짜
            else:   
                print("FAKE")
                break
        i += 1
    # 가짜 판정이 나지 않았다면 OK
    else:
        print("OK")
```