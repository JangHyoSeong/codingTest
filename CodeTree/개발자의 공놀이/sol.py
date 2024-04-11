def DFS(n):
    # DFS. 방문 가능한 곳을 방문하고 visited를 True로 바꿈
    new = out[n]
    if visited[new]:
        return
    visited[new] = True
    DFS(new)

N = int(input())
numbers = list(map(int, input().split()))

# 맨 왼쪽과 오른쪽 계산을 편하게 하기 위해 더미 추가, 정렬
numbers = [-1000] + sorted(numbers) + [2000]

# 현재 인덱스에서 어느 인덱스로 공을 넘겨줘야 하는지 저장
out = [-1] * (N+2)

# 현재 인덱스를 향하고 있는 간선의 개수를 저장
in_degree = [0] * (N+2)

# 입력받은 리스트를 순회하면서 간선 정보를 만들어줌
for i in range(1, N+1):
    if numbers[i] - numbers[i-1] <= numbers[i+1] - numbers[i]:
        out[i] = i-1
        in_degree[i-1] += 1
    elif  numbers[i] - numbers[i-1] > numbers[i+1] - numbers[i]:
        out[i] = i+1
        in_degree[i+1] += 1

# 방문 여부 저장 리스트
visited = [False] * (N+2)

# 사이클이 몇개인지 세는 count (결과값)
count = 0

# 현재 자신에게 향하는 간선이 0개인 인덱스를 저장할 리스트
degree_0 = []

# 자신에게 향하는 간선이 0개인 인덱스들을 degree_0 리스트에 저장
for i in range(1, N+1):
    if in_degree[i] == 0:
        degree_0.append(i)

print(out)
# degree_0 리스트를 순회하면서 그 인덱스를 시작점으로 공을 전달
# 자신에게 향하는 공이 없다면 무조건 던지는 것으로 시작해야하기 때문
for i in range(len(degree_0)):
    num = degree_0[i]
    visited[num] = True
    count += 1
    DFS(num)

# 다시 한번 리스트를 순회하면서, 방문하지 않은 곳을 방문
# DFS를 통해 사이클의 개수를 세어줌
for i in range(1, N+1):
    if visited[i]:
        continue

    visited[i] = True
    count += 1
    DFS(i)

'''
이해를 돕기 위한 케이스와 in_degree 리스트
input은 보기편하게 정렬된 상태
input
60
[30, 35, 83, 122, 129, 140, 144, 184, 194, 228, 229, 236, 238, 276, 351, 366, 370, 396, 405, 408, 429, 433, 
438, 444, 465, 471, 475, 489, 491, 492, 500, 501, 530, 539, 543, 552, 591, 607, 614, 645, 670, 689, 726, 744, 765, 773, 777, 787, 819, 841, 842, 859, 860, 905, 915, 918, 929, 937, 955, 988]

in_degree 리스트 (맨 앞, 맨 뒤 더미값 주의)
[0, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 2, 1, 0, 2, 1, 1, 2, 1, 0, 0, 2, 1, 0, 2, 1, 
1, 1, 0, 2, 2, 0, 0, 2, 1, 0, 2, 1, 1, 1, 0, 2, 2, 0, 0, 2, 1, 1, 1, 0, 2, 1, 1, 2, 1, 0, 0]

0 : 자신이 받는 공이 하나도 없음 -> 자신을 시작으로 공을 던져야함
1 : 자신이 받는 공이 하나
-> 처음 0에서부터 시작한 사이클에 포함된다면 처음 for i in range(len(degree_0)):으로 방문처리
-> 0에서 시작한 사이클에 포함되지 않는다면 -> 뒤에 한번 더 순회할 때 처리

2 : 자신이 받는 공이 2개
-> 0에서 시작한 사이클에서 무조건 방문
'''
print(count)