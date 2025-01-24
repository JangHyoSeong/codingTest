from collections import deque

N, M, K = map(int, input().split())
nutrient_input = [list(map(int, input().split())) for _ in range(N)]
nutrient = [[5] * N for _ in range(N)]
tree_table = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, input().split())
    tree_table[r-1][c-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    dead_trees = []
    for i in range(N):
        for j in range(N):
            if tree_table[i][j]:
                new_trees = deque()
                dead_sum = 0

                while tree_table[i][j]:
                    age = tree_table[i][j].popleft()
                    if nutrient[i][j] >= age:
                        nutrient[i][j] -= age
                        new_trees.append(age+1)

                    else:
                        dead_sum += age // 2

                tree_table[i][j] = new_trees
                nutrient[i][j] += dead_sum

    for i in range(N):
        for j in range(N):
            for age in tree_table[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree_table[ni][nj].appendleft(1)

    
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += nutrient_input[i][j]

print(sum(len(tree_table[i][j]) for i in range(N) for j in range(N)))