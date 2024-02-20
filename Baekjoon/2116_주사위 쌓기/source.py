num = int(input())
dices = [list(map(int, input().split())) for _ in range(num)]
result = [0] * 6
pair = [5, 3, 4, 1, 2, 0]


for start in range(1, 7):
    bottom = start
    bottom_idx = dices[0].index(bottom)
    top = dices[0][pair[bottom_idx]]
    top_idx = pair[bottom_idx]


    temp_dice = dices[0][:6]
    temp_dice[top_idx] = -1
    temp_dice[bottom_idx] = -1
    result[start-1] += max(temp_dice)
    for i in range(1, num):

        bottom = top
        bottom_idx = dices[i].index(bottom)
    
        top_idx = pair[bottom_idx]
        top = dices[i][top_idx]

        temp_dice = dices[i][:6]
        temp_dice[top_idx] = -1
        temp_dice[bottom_idx] = -1
        result[start-1] += max(temp_dice)

print(max(result))