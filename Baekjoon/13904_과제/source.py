N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x : (-x[1], x[0]))

homeworks = [0] * (1001)

for i in range(N):
    due_date = arr[i][0]

    while due_date > 0:
        if homeworks[due_date]:
            due_date -= 1
        else:
            homeworks[due_date] = arr[i][1]
            break

print(sum(homeworks))