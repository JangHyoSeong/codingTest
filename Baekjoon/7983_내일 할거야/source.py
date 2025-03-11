import sys

N = int(sys.stdin.readline().rstrip())
homeworks = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

homeworks.sort(key= lambda x : -x[1])

answer = homeworks[0][1]

for d, t in homeworks:
    answer = min(answer, t) - d

print(answer)