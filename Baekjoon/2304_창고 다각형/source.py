N = int(input())

pillars = [list(map(int, input().split())) for _ in range(N)]

status = True

pillars.sort(key= lambda x: x[0])
max_height = 0
for i in range(N):
    if max_height < pillars[i][1]:
        max_height = pillars[i][1]
        max_idx = i

size = 0
temp_max_height = pillars[0][1]
for i in range(max_idx):

    if temp_max_height < pillars[i][1]:
        temp_max_height = pillars[i][1]

    size += temp_max_height * (pillars[i+1][0] - pillars[i][0])

temp_max_height = pillars[-1][1]
for i in range(N-1, max_idx, -1):
    if temp_max_height < pillars[i][1]:
        temp_max_height = pillars[i][1]

    size += temp_max_height * (pillars[i][0] - pillars[i-1][0])

size += max_height

print(size)