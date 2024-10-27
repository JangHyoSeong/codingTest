# 유니온-파인드(Union-Find) 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# 입력 처리
N, M = map(int, input().split())
schools = ['0'] + input().split()  # 학교 정보, 남초(M) 여초(W)

edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if schools[u] != schools[v]:  # 남초-여초 학교 간 연결만 허용
        edges.append((d, u, v))

# 크루스칼 알고리즘을 사용하여 최소 신장 트리(MST) 구성
edges.sort()  # 거리를 기준으로 오름차순 정렬
parent = [i for i in range(N + 1)]  # 유니온-파인드용 부모 배열
rank = [0] * (N + 1)

mst_weight = 0
edge_count = 0

for edge in edges:
    weight, u, v = edge
    if find(parent, u) != find(parent, v):  # 사이클이 생기지 않도록 체크
        union(parent, rank, u, v)
        mst_weight += weight
        edge_count += 1
        if edge_count == N - 1:  # N-1개의 간선을 선택하면 MST 완성
            break

# 결과 출력
if edge_count == N - 1:
    print(mst_weight)
else:
    print(-1)
