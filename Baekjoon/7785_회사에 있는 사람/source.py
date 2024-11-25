N = int(input())

logs = {}
for _ in range(N):
    people, enter = list(input().split())

    if enter == 'enter':
        logs[people] = True
    else:
        logs[people] = False

result = []
for log in logs:
    if logs[log]:
        result.append(log)

result.sort(reverse=True)

for name in result:
    print(name)