left = list(input())
right = []

commands_num = int(input())


for i in range(commands_num):
    command = input().split()
    
    if command[0] == 'P':
        left.append(command[1])


    elif command[0] == 'L':
        if left != []:
            right.append(left.pop(len(left)-1))
               

    elif command[0] == 'D':
        if right != []:
            left.append(right.pop(len(right)-1))

    elif command[0] == 'B':
        if left != []:
            left.pop(len(left)-1)

left = ''.join(left)
right.reverse()
right = ''.join(right)

print(left + right)