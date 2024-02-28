N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

big_width, big_height = 0, 0
small_width, small_height = 0, 0

for i in range(6):
    if arr[i][0] >= 3:
        if big_height < arr[i][1]:
            big_height = arr[i][1]
            height_idx = i
    elif arr[i][0] <= 2:
        if big_width < arr[i][1]:
            big_width = arr[i][1]
            width_idx = i

small_height = abs(arr[(width_idx+1)%6][1] - arr[(width_idx-1)%6][1])
small_width = abs(arr[(height_idx+1)%6][1] - arr[(height_idx-1)%6][1])

size = big_width * big_height - small_height * small_width

print(size * N)