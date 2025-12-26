N, M, K = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]

answer = 0
for line in table:
    count = 0
    for i in range(M):
        if line[i] == 0:
            count += 1
        else:
            if count >= K:
                answer += count - K + 1
            count = 0
    
    if count >= K:
        answer += count - K + 1

print(answer)