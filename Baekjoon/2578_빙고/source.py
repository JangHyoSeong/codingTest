def bingoCheck(check):
    
    bingo = 0
    for i in range(5):
        if sum(check[i]) == 5:
            bingo += 1


    for i in range(5):
        temp = 0
        for j in range(5):
            temp += check[j][i]
        if temp == 5:
            bingo += 1
    temp = 0
    temp2 = 0
    for i in range(5):
        temp += check[i][i]
        temp2 += check[i][4-i]
    if temp == 5:
        bingo += 1
    if temp2 == 5:
        bingo += 1

    return bingo
    
board = [list(map(int, input().split())) for _ in range(5)]

bingo = [list(map(int, input().split())) for _ in range(5)]

bingo_list = []

for i in range(5):
    for j in range(5):
        bingo_list.append(bingo[i][j])

check = [[0] * 5 for _ in range(5)]

count = 0
bingo = 0

for i in range(25):
    count += 1
    number = bingo_list[i]

    for j in range(5):
        if number in board[j]:
            check[j][board[j].index(number)] = 1
            break
    
    if bingoCheck(check) >= 3:
        break
        
print(count)