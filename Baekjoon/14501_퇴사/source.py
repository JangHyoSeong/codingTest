limit_day = int(input())

schedule = []

for i in range(limit_day):

    temp = list(map(int, input().split()))
    schedule.append(temp)

result = [0] * (limit_day + 1)

for i in range(limit_day):
    time = schedule[i][0]
    money = schedule[i][1]

    if i + time <= limit_day:
        result[i + time] = max(result[i + time], result[i] + money)

    result[i+1] = max(result[i+1], result[i])

print(result[limit_day])