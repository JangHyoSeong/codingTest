N = int(input())

mine = []
for _ in range(N):
    mine.append(int(input()))
    

result = []

for i in range(N):
    mine_max_idx = 0
    boom_list = []
    
    for j in range(N):
        if mine[mine_max_idx] < mine[j]:
            mine_max_idx = j
    
    if mine[mine_max_idx] == -1:
        break
    
    result.append(mine_max_idx+1)
    boom_list.append(mine_max_idx)
    left_idx = mine_max_idx - 1
    right_idx = mine_max_idx + 1
    
    while left_idx >= 0:
        if mine[left_idx] == -1:
            break
        if mine[left_idx] < mine[left_idx+1]:
            boom_list.append(left_idx)
            left_idx -= 1
        else:
            break

    while right_idx < N:
        if mine[right_idx] == -1:
            break
        if mine[right_idx] < mine[right_idx-1]:
            boom_list.append(right_idx)
            right_idx += 1
        else:
            break
    
    
    for idx in boom_list:
        mine[idx] = -1


result.sort()
for idx in result:
    print(idx)