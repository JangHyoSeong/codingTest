# [2447] 별 찍기 - 10

### **난이도**
골드 5
## **📝문제**
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

```
***
* *
***
```
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
### **입력**
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.
### **출력**
첫째 줄부터 N번째 줄까지 별을 출력한다.
### **예제입출력**

**예제 입력1**

```
27
```

**예제 출력1**

```
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

def star(n):
    if n == 1:
        return ['*']
    
    small_star = star(n//3)
    pattern = []

    for line in small_star:
        pattern.append(line * 3)

    for line in small_star:
        pattern.append(line + ' ' * (n//3) + line)

    for line in small_star:
        pattern.append(line * 3)

    return pattern

print('\n'.join(star(N)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|41760|48|Python3|367
#### **📝해설**

**알고리즘**
```
1. 재귀
2. 분할 정복
```

### **다른 풀이**

```python
import sys

def starPattern(n):
    init=["***","* *","***"]
    
    if n==3:
        return init
    a_pattern=list()
    star=starPattern(n//3)
    b_pattern=list()
    
    for s in star:
        a_pattern.append(s*3)
   
    for s in star:
       b_pattern.append(s+' '*(n//3)+s)

    
    return a_pattern+b_pattern+a_pattern

n=int(sys.stdin.readline())
print('\n'.join(starPattern(n)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
konghi|40468|40|Python3|398
#### **📝해설**

```python
N = int(input())

def star(n):
    # 별찍기 재귀함수

    # n==1인 경우 *을 리턴
    if n == 1:
        return ['*']
    
    # N > 1인 경우 3으로 나눔
    small_star = star(n//3)
    pattern = []

    # 맨 위는 * 3
    for line in small_star:
        pattern.append(line * 3)

    # 중간은 공백을 단계의 개수로 더함
    for line in small_star:
        pattern.append(line + ' ' * (n//3) + line)

    # 맨 아래도 * 3
    for line in small_star:
        pattern.append(line * 3)

    return pattern

print('\n'.join(star(N)))
```