# 문제 제목
가장 큰 수

## **📝문제 설명**
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
### **⚠제한사항**
- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
### **입출력 예**

|numbers |	return|
|:---:|:---:|
|[6, 10, 2]	|"6210"|
|[3, 30, 34, 5, 9]	|"9534330"|
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**
처음에는 자릿수마다 비교하여 가중치가 큰 수를 앞으로 보내려고 했다.
하지만 이런 방식으로는 구현이 너무 힘들었고
숫자 정렬의 규칙을 발견하여 새롭게 코드를 구성했다
### **🧾나의 풀이**

```python
def solution(numbers):
    answer = ''
    N = len(numbers)
    numbers = list(map(str, numbers))
    new_numbers = []

    for i in range(N):
        new_numbers.append([i, numbers[i]*4])
    
    new_numbers.sort(key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer += numbers[new_numbers[i][0]]


    if answer[0] == '0':
        answer = '0'

    return answer
```

#### **📝해설**

```python
def solution(numbers):
    answer = ''
    N = len(numbers)
    # 숫자를 문자열 리스트로 바꿈
    numbers = list(map(str, numbers))
    new_numbers = []

    # 숫자를 반복하여 나열하고, 이를 4의자리까지 비교하면 어느 값이 더 앞으로 갈지 정할 수 있음. 그렇게 하기 위해서 정렬을 위한 인덱스와 숫자를 새로 리스트에 저장
    for i in range(N):
        new_numbers.append([i, numbers[i]*4])
    
    # 새로 저장한 리스트를 정렬
    new_numbers.sort(key=lambda x: x[1], reverse=True)

    # 원본 인덱스에 접근하기 위해 다음과 같은 반복
    for i in range(N):
        answer += numbers[new_numbers[i][0]]


    # edge case, 0인 경우는 0이 여러개 출력되면 안됨
    if answer[0] == '0':
        answer = '0'

    return answer
```

#### **😅개선점**

1. 조금 불필요한 연산이 있어서 더욱 간결하게 줄일 수 있을 것 같다.

### **다른 풀이**

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
```
## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42746)**<br/>