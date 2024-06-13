def floyd_warshall(n, edges):
    # 거리 행렬 초기화 (무한대로 초기화)
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    
    # 자기 자신으로의 거리는 0으로 설정
    for i in range(n):
        dist[i][i] = 0
    
    # 직접 연결된 노드의 거리는 1로 설정
    for u, v in edges:
        dist[u-1][v-1] = 1
        dist[v-1][u-1] = 1
    
    # 플로이드-워셜 알고리즘 수행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_person_with_min_kevin_bacon_number(n, dist):
    min_bacon_number = float('inf')
    person = -1
    
    # 각 유저의 케빈 베이컨 수 계산
    for i in range(n):
        bacon_number = sum(dist[i])
        if bacon_number < min_bacon_number:
            min_bacon_number = bacon_number
            person = i + 1
        elif bacon_number == min_bacon_number and i + 1 < person:
            person = i + 1
    
    return person

# 입력 받기
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 플로이드-워셜 알고리즘을 사용하여 거리 행렬 계산
dist = floyd_warshall(n, edges)

# 케빈 베이컨 수가 가장 작은 사람 찾기
result = find_person_with_min_kevin_bacon_number(n, dist)

# 결과 출력
print(result)