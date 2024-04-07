T = int(input())

for testcase in range(T):
    N = int(input())
    node = []

    # 시작지점, 도착지점 까지 총 N+2개의 노드가 존재한다고 생각
    for i in range (N+2):
        node.append(list(map(int, input().split())))

    # 각 노드에서 갈 수 있는 간선의 정보를 저장할 리스트
    edge = [[] for _ in range(N+2)]

    # 각 노드에서 갈 수 있는 편의점(노드)를 리스트에 저장해줌
    for i in range(N+2):
        for j in range(i, N+2):
            if i == j:
                continue

            if abs(node[i][0] - node[j][0]) + abs(node[i][1] - node[j][1]) <= 1000:
                edge[i] += [j]
                edge[j] += [i]

    # 각 편의점의 방문 여부를 저장
    visited = [False] * (N+2)

    # DFS를 위해 스택 선언. 시작값을 넣어줌
    stack = [0]

    # 시작 위치는 방문 표시
    visited[0] = True

    # 도착 지점에 도착했다면 True로 바꾸어줌
    flag = False

    # DFS 시작
    while stack:
        now = stack.pop()
        
        # N+1번째 노드에 도착했다면 == 목표 지점에 도착했다면 종료
        if now == N+1:
            flag = True
            break

        # 현재 위치에서 갈 수 있는 노드를 전부 방문
        # 방문 처리도 동시에 해줌
        for can_go in edge[now]:
            if not visited[can_go]:
                stack.append(can_go)
                visited[can_go] = True
    
    # flag = True 상태로 종료됐다면 happy, 아니라면 sad
    if flag:
        print('happy')
    else:
        print('sad')