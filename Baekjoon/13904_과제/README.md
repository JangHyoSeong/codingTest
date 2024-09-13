# [13904] 과제

### **난이도**
골드 3
## **📝문제**
웅찬이는 과제가 많다. 하루에 한 과제를 끝낼 수 있는데, 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있다. 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.

웅찬이는 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다. 웅찬이를 도와 얻을 수 있는 점수의 최댓값을 구하시오.
### **입력**
첫 줄에 정수 N (1 ≤ N ≤ 1,000)이 주어진다.

다음 줄부터 N개의 줄에는 각각 두 정수 d (1 ≤ d ≤ 1,000)와 w (1 ≤ w ≤ 100)가 주어진다. d는 과제 마감일까지 남은 일수를 의미하며, w는 과제의 점수를 의미한다.
### **출력**
얻을 수 있는 점수의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
4 60
4 40
1 20
2 50
3 30
4 10
6 5
```

**예제 출력1**

```
185
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x : (-x[1], x[0]))

homeworks = [0] * (1001)

for i in range(N):
    due_date = arr[i][0]

    while due_date > 0:
        if homeworks[due_date]:
            due_date -= 1
        else:
            homeworks[due_date] = arr[i][1]
            break

print(sum(homeworks))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33188|56|Python3|406
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. 정렬
```

#### **📝해설**

```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 주어진 입력을 과제의 중요도에 따라 정렬
arr.sort(key = lambda x : (-x[1], x[0]))

# 어느 날에 어떤 과제를 수행할지 저장할 리스트
homeworks = [0] * (1001)

# 과제를 순회하면서
for i in range(N):

    # 현재 과제의 기한을 변수로 저장
    due_date = arr[i][0]

    # 현재 과제의 기한을 뒤에서부터 줄여나가면서
    while due_date > 0:

      # 만약 현재 날에 해야할 과제가 이미 있다면
        if homeworks[due_date]:
            # 더 빠른 날을 탐색
            due_date -= 1

        # 만약 현재 날에 해야할 과제가 없다면
        else:
          # 이 날에 그 과제를 함
            homeworks[due_date] = arr[i][1]
            break

# 다 더한 결과값을 출력
print(sum(homeworks))
```