T = int(input())

def origami(paper, N):

    if N == 1:
        return 0
    if N == 3:
        if paper[0] + paper[2] == 1:
            return 0
        else:
            return 1
    
    left_half = paper[:(N-1)//2]
    right_half = paper[(N+1)//2:]

    for i in range((N-1)//2):
        if paper[i] + paper[N-1-i] == 1:
            result = 0
        else:
            result = 1
            break


    return origami(left_half, (N-1)//2) + origami(right_half, (N-1)//2) + result


for testcase in range(1, T+1):
    in_out = list(map(int, list(input())))

    paper_length = len(in_out)
    result = origami(in_out, paper_length)

    if result == 0:
        print('YES')
    else:
        print('NO')

