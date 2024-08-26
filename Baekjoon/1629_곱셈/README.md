# [1629] 곱셈

### **난이도**
실버 1
## **📝문제**
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.
### **출력**
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
10 11 12
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
a, b, c = map(int, input().split())

def devide(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = devide(a, b // 2, c)
        return (half * half) % c
    else:
        half = devide(a, (b-1) // 2, c)
        return (half * half * a) % c

print(devide(a, b, c))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|108080|88|PyPy3|290
#### **📝해설**

**알고리즘**
```
1. 분할 정복
```
#### **📝해설**

```python
a, b, c = map(int, input().split())

def devide(a, b, c):
    # b == 0인 경우 1
    if b == 0:
        return 1

    # b가 짝수인 경우
    elif b % 2 == 0:
        # 반으로 나눈 후 계산
        half = devide(a, b // 2, c)
        return (half * half) % c
    # b가 홀수인 경우
    else:
        # 반으로 나눈 후 a를 한번 더 곱해서 계산
        half = devide(a, (b-1) // 2, c)
        return (half * half * a) % c

print(devide(a, b, c))
```