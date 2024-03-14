def solution(commands):
    answer = []
    table = [[None] * 51 for _ in range(51)]
    merge = {}

    for i in range(1, 51):
        for j in range(1, 51):
            merge[(i, j)] = {(i, j)}


    for command in commands:
        cmd = list(command.split())
        
        if cmd[0] == 'UPDATE':

            if len(cmd) == 4:
                x, y = int(cmd[1]), int(cmd[2])
                for merge_x, merge_y in merge[(x, y)]:
                    table[merge_x][merge_y] = cmd[3]

            else:
                for i in range(1, 51):
                    for j in range(1, 51):
                        for merge_x, merge_y in merge[(i, j)]:
                            if table[merge_x][merge_y] == cmd[1]:
                                table[merge_x][merge_y] = cmd[2]

        elif cmd[0] == 'MERGE':
            x1, y1, x2, y2 = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])

            new_merge = merge[(x1, y1)] | merge[(x2, y2)]

            for merge_x, merge_y in new_merge:
                merge[(merge_x, merge_y)] = new_merge

            value = table[x1][y1] if table[x1][y1] is not None else table[x2][y2]
            for merge_x, merge_y in new_merge:
                table[merge_x][merge_y] = value

        elif cmd[0] == 'UNMERGE':
            x, y = int(cmd[1]), int(cmd[2])
            temp_value = table[x][y]
            
            for merge_x, merge_y in list(merge[(x, y)]):
                table[merge_x][merge_y] = None
                merge[(merge_x, merge_y)] -= {(x, y)}

            merge[(x, y)] = {(x, y)}
            table[x][y] = temp_value

        else:
            x, y = int(cmd[1]), int(cmd[2])
            if table[x][y] is None:
                answer.append('EMPTY')
            else:
                answer.append(table[x][y])
                
    return answer

commands= ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]
print(solution(commands))