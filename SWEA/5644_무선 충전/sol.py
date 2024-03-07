import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    time, num = map(int, input().split())
    a_move = [0] + list(map(int, input().split()))
    b_move = [0] + list(map(int, input().split()))

    bc = [list(map(int, input().split())) for _ in range(num)]
    
    direction = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    
    result = 0
    a_position = [1, 1]
    b_position = [10, 10]

    for second in range(time+1):

        a_position[0] += direction[a_move[second]][0]
        a_position[1] += direction[a_move[second]][1]
        b_position[0] += direction[b_move[second]][0]
        b_position[1] += direction[b_move[second]][1]
        
        a_list = []
        b_list = []
        a_max_idx = 0
        b_max_idx = 0
        
        for i in range(num):

            if abs(a_position[0] - bc[i][0]) + abs(a_position[1] - bc[i][1]) <= bc[i][2]:
                a_list.append([bc[i][3], i])
                

            if abs(b_position[0] - bc[i][0]) + abs(b_position[1] - bc[i][1]) <= bc[i][2]:
                b_list.append([bc[i][3], i])

        a_len = len(a_list)
        b_len = len(b_list)
        a_list.sort(key=lambda x : x[0], reverse=True)
        b_list.sort(key=lambda x : x[0], reverse=True)

        if a_len != 0 and b_len == 0:
            result += a_list[0][0]

        elif a_len == 0 and b_len != 0:
            result += b_list[0][0]

        elif a_len >= 1 and b_len >= 1:

            if a_list[0][1] == b_list[0][1]:
                result += a_list[0][0]
                if a_len > 1 and b_len > 1:
                    result += max(a_list[1][0], b_list[1][0])
                else:
                    if a_len == 1 and b_len > 1:
                        result += b_list[1][0]
                    elif a_len > 1 and b_len == 1:
                        result += a_list[1][0]
            else:
                result += a_list[0][0] + b_list[0][0]


    print(f'#{testcase} {result}')