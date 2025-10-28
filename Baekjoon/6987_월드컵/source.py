answer = []
matches = []
for i in range(6):
    for j in range(i+1, 6):
        matches.append((i, j))

def dfs(idx):
    global possible

    if possible:
        return
    
    if idx == 15:
        for team in result:
            if any(x != 0 for x in team):
                return
        
        possible = True
        return
    
    a, b = matches[idx]

    # a 승, b 패
    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        dfs(idx + 1)
        result[a][0] += 1
        result[b][2] += 1

    # a 무, b 무
    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        dfs(idx + 1)
        result[a][1] += 1
        result[b][1] += 1

    # a 패, b 승
    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        dfs(idx + 1)
        result[a][2] += 1
        result[b][0] += 1

for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i*3 : (i+1)*3] for i in range(6)]

    possible = False

    if sum(sum(team) for team in result) != 30:
        answer.append(0)
    else:
        dfs(0)
        answer.append(1 if possible else 0)
    
print(*answer)