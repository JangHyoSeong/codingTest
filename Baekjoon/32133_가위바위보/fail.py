N, M, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]

winner = N
losser = 0
win = [True] * N
result = []
round = 0

while winner > K:
    if round == M:
        print(-1)
        break
    round += 1
    rock, scissor, paper = [], [], []
    
    for i in range(N):
        if win[i]:
            if arr[i][round-1] == 'R':
                rock.append(i)
            elif arr[i][round-1] == 'S':
                scissor.append(i)
            else:
                paper.append(i)

    rock_len, scissor_len, paper_len = len(rock), len(scissor), len(paper)
    
    max_len = max(rock_len, scissor_len, paper_len)
    if rock_len == max_len:
        result.append('P')
        winner -= max_len
        losser += max_len
        for temp in rock:
            win[temp] = False

    elif scissor_len == max_len:
        result.append('R')
        winner -= max_len
        losser += max_len
        for temp in scissor:
            win[temp] = False

    elif paper_len == max_len:
        result.append('S')
        winner -= max_len
        losser += max_len
        for temp in paper:
            win[temp] = False

    if losser == N:
        print(-1)
        break

else:
    print(round)
    print("".join(map(str, result)))