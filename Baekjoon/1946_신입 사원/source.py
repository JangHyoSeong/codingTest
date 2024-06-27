T = int(input())

for testcase in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]

    scores.sort()

    count = 1
    min_interview_score = scores[0][1]

    for i in range(1, N):
        if scores[i][1] < min_interview_score:
            count += 1
            min_interview_score = scores[i][1]

    print(count)