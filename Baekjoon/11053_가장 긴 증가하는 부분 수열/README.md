# [11053] 가장 긴 증가하는 부분 수열
### **난이도**
실버 2
## **📝문제**
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
### **입력**
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
### **출력**
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
10 20 10 30 20 50
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
numbers = list(map(int, input().split()))
arr = [1] * N

for i in range(N):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            arr[i] = max(arr[j]+1, arr[i])
        
print(max(arr))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|109240|164|PyPy3|222
#### **📝해설**

**알고리즘**
```
1. 다이나믹 프로그래밍
```

### **다른 풀이**

```python
def sol():
    N = int(input())
    nums = [*map(int,input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:
            stack.append(i)
        else:
            for j,v in enumerate(stack):
                if i <= v:
                    stack[j] = i
                    break
    return len(stack)

print(sol())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
faul2chris|30616|36|Python3|347
#### **📝해설**

```python
N = int(input())
numbers = list(map(int, input().split()))

# 현재 위치까지 증가하는 부분수열의 길이를 나타낼 리스트
arr = [1] * N

# i는 0에서 리스트의 끝까지 순회
for i in range(N):

    # j는 0에서 i까지 순회
    for j in range(0, i):

        # i번째 까지의 numbers를 모두 순회하면서, numbers[i]가 numbers[j]보다 크다면
        if numbers[i] > numbers[j]:
            #arr[i]를 갱신
            arr[i] = max(arr[j]+1, arr[i])

        '''
        기존에 구해놨던 최대 길이에서 현재 상태만큼 더하는 방식
        -> 다이나믹 프로그래밍
        '''        
print(max(arr))
```