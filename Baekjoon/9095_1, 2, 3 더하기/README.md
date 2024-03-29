# [9095] 1, 2, 3 더하기

### **난이도**
실버 3
## **📝문제**
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
### **출력**
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
4
7
10
```

**예제 출력1**

```
7
44
274
```

### **출처**
ICPC > Regionals > Asia Pacific > Korea > Asia Regional - Taejon 2001 PC번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

for testcase in range(T):
    N = int(input())

    result = [1, 2, 4]
    for i in range(3, N):
        temp = result[i-1] + result[i-2] + result[i-3]
        result.append(temp)

    print(result[N-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|40|Python3|221
#### **📝해설**
N = 4일때를 예를 들자면
N = 1일 때 + 3을 하는 경우
N = 2일 때 + 2를 하는 경우
N = 3일 때 + 1을 하는 경우가 있다
따라서 F(4) = F(3) + F(2) + F(1)이다.

**알고리즘**
```
1. 동적 프로그래밍(점화식)
```
### **🔖정리**

1. 문제를 풀기 전에 확실하게 어떻게 풀지 생각해보고 풀자