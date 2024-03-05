# 문제 제목
택배 배달과 수거
## **📝문제 설명**
당신은 일렬로 나열된 n개의 집에 택배를 배달하려 합니다. 배달할 물건은 모두 크기가 같은 재활용 택배 상자에 담아 배달하며, 배달을 다니면서 빈 재활용 택배 상자들을 수거하려 합니다.
배달할 택배들은 모두 재활용 택배 상자에 담겨서 물류창고에 보관되어 있고, i번째 집은 물류창고에서 거리 i만큼 떨어져 있습니다. 또한 i번째 집은 j번째 집과 거리 j - i만큼 떨어져 있습니다. (1 ≤ i ≤ j ≤ n)
트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있습니다. 트럭은 배달할 재활용 택배 상자들을 실어 물류창고에서 출발해 각 집에 배달하면서, 빈 재활용 택배 상자들을 수거해 물류창고에 내립니다. 각 집마다 배달할 재활용 택배 상자의 개수와 수거할 빈 재활용 택배 상자의 개수를 알고 있을 때, 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 구하려 합니다. 각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있습니다.


트럭에 실을 수 있는 재활용 택배 상자의 최대 개수를 나타내는 정수 cap, 배달할 집의 개수를 나타내는 정수 n, 각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열 deliveries와 각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열 pickups가 매개변수로 주어집니다. 이때, 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 return 하도록 solution 함수를 완성해 주세요.
### **⚠제한사항**
- 1 ≤ cap ≤ 50
- 1 ≤ n ≤ 100,000
- deliveries의 길이 = pickups의 길이 = n
  - deliveries[i]는 i+1번째 집에 배달할 재활용 택배 상자의 개수를 나타냅니다.
  - pickups[i]는 i+1번째 집에서 수거할 빈 재활용 택배 상자의 개수를 나타냅니다.
  - 0 ≤ deliveries의 원소 ≤ 50
  - 0 ≤ pickups의 원소 ≤ 50
- 트럭의 초기 위치는 물류창고입니다.
### **입출력 예**
|cap |n |deliveries |pickups | result|
|:---:|:---:|:---:|:---:|:---:|
|4	|5	|[1, 0, 3, 1, 2]	|[0, 3, 0, 4, 0]	|16|
|2	|7	|[1, 0, 2, 0, 1, 0, 2]|	[0, 2, 0, 1, 0, 2, 0]	|30|
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def solution(cap, n, deliveries, pickups):
    answer = 0

    last = n-1
    go_last = last
    come_last = last

    if deliveries.count(0) == n and pickups.count(0) == n:
        return 0

    while last >= 0:

        last = max(go_last, come_last)
        go = cap
        come = cap
        answer += 2 * (last + 1)


        while deliveries[go_last] < go and go_last >= 0:
            go -= deliveries[go_last]
            deliveries[go_last] = 0
            go_last -= 1

        if deliveries[go_last] > go and go_last >= 0:
            deliveries[go_last] -= go
            go = 0

        while deliveries[go_last] == go and go_last >= 0:
            deliveries[go_last] = 0
            go = 0
            go_last -= 1

        while pickups[come_last] < come and come_last >= 0:
            come -= pickups[come_last]
            pickups[come_last] = 0
            come_last -= 1

        if pickups[come_last] > come and come_last >= 0:
            pickups[come_last] -= come
            come = 0

        while pickups[come_last] == come and come_last >= 0:
            pickups[come_last] = 0
            come = 0
            come_last -= 1

    return answer
```

#### **📝해설**

- 결국 이동은 물건(택배나 수거할 상자)이 가장 멀리 있는 집까지 가야하기에, max(go_last, come_last)를 통해 가장 멀리까지 이동하는 방식으로 진행했다

#### **😅개선점**

1. 예외상황 처리를 더 자연스럽게 할 수 있었을 것 같다

### **다른 풀이**

```python
def solution(cap, n, deliveries, pickups):
    answer = 0
    # 역순으로 누적합
    for i in range(n-2, -1, -1):
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
    k = 0
    for i in range(n-1, -1, -1):
        while deliveries[i] > cap*k or pickups[i] > cap*k:
            answer += (i+1)*2
            k += 1
    return answer
```

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150369)**<br/>