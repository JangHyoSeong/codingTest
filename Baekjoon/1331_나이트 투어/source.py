chess = [[0 for i in range(6)] for i in range(6)]
move = []

def calc(a):
    if a[0] == 'A':
        width = 0
    elif a[0] == 'B':
        width = 1
    elif a[0] == 'C':
        width = 2
    elif a[0] == 'D':
        width = 3
    elif a[0] == 'E':
        width = 4
    elif a[0] == 'F':
        width = 5

    height = int(a[1]) - 1

    return width, height
    

for i in range(36):
    move.append(str(input()))
    width, height = calc(move[i])

    chess[width][height] += 1

flag = 1
for i in range(1, len(move)):
    width_1, height_1 = calc(move[i-1])
    width_2, height_2 = calc(move[i])

    if abs(width_1 - width_2) == 2 and abs(height_1 - height_2) == 1:
        pass
    elif abs(width_1 - width_2) == 1 and abs(height_1 - height_2) == 2:
        pass
    else:
        flag = 0

start_width, start_height = calc(move[0])
end_width, end_height = calc(move[35])

if abs(start_width - end_width) == 2 and abs(start_height - end_height) == 1:
    pass
elif abs(start_width - end_width) == 1 and abs(start_height - end_height) == 2:
    pass
else:
    flag = 0

for i in chess:
    for j in i:
        if j >= 2:
            flag = 0
            break

if flag == 1:
    print('Valid')
else:
    print('Invalid')
