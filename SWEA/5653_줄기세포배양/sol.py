import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    height, width, total_time = map(int, input().split())
    cells = []
    for i in range(2*total_time + height):
        cells_temp = [[0 , 0] for _ in range((2*total_time + width))]
        cells.append(cells_temp)

    input_cells = [list(map(int, input().split())) for _ in range(height)]
    for i in range(total_time, total_time + height):
        for j in range(total_time, total_time + width):
            # 첫 번째 값은 세포의 숫자(고정), 두 번째 값은 현재 상태(활성, 비활성, 죽음)
            cells[i][j] = [input_cells[i-total_time][j-total_time], input_cells[i-total_time][j-total_time]]


    stack = [[] * 10]
    height = len(cells)
    width = len(cells[0])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
        
    for time in range(total_time):

        stack = [[] for _ in range(11)]

        for i in range(height):
            for j in range(width):

                if cells[i][j][0] != 0:

                    # 비활성상태
                    if cells[i][j][1] > 0:
                        cells[i][j][1] -= 1

                    # 죽은 상태
                    elif cells[i][j][1] <= -cells[i][j][0]:
                        continue

                    # 활성 상태
                    else:
                        cells[i][j][1] -= 1
                        stack[cells[i][j][0]].append([i, j])

        # 스택을 순회하면서 세포를 옮김
        for priority in range(10, 0, -1):
            while stack[priority]:
                x, y = stack[priority].pop()

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    if cells[new_x][new_y][0] == 0:
                        cells[new_x][new_y] = [priority, priority]

    count = 0
    for i in range(height):
        for j in range(width):
            if cells[i][j][0] != 0 and cells[i][j][1] > -cells[i][j][0]:
                count += 1

    print(f'#{testcase} {count}')