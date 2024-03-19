import sys
sys.stdin = open('input2.txt')

T = int(input())

for testcase in range(1, T+1):
    N, slide = map(int, input().split())

    cliff = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 가로 방향 탐색
    for i in range(N):
        flag = True

        # 이번 줄에서 활주로를 어디 만들었는지 저장할 리스트
        # 활주로가 있는 위치는 True로 바꾸어줌
        temp_runway = [False] * N

        # j와 j+1을 비교할 것이라서 N-1번 반복
        for j in range(N-1):

            # 한번에 높이차가 2 이상 난다면 활주로 건설 불가능
            if abs(cliff[i][j] - cliff[i][j+1]) >= 2:
                flag = False
                break

            # 다음 위치가 높이가 1 높다면
            if cliff[i][j] - cliff[i][j+1] == 1:
                
                # 인덱스를 벗어난다면 False
                if j + slide >= N:
                    flag = False
                    break

                # 인덱스를 벗어나지 않는다면 활주로의 길이만큼 검사
                for k in range(1, slide+1):
                    # 이미 활주로가 지어졌다면 False
                    if j + k >= N or temp_runway[j+k]:
                        flag = False
                        break

                    # 활주로가 생겨야 할 범위 내에서 또 높이가 바꼈다면 False
                    if cliff[i][j+1] != cliff[i][j+k]:
                        flag = False
                        break
                    else:
                        temp_runway[j+k] = True
            
            # 높이가 1 높은경우는 방향을 바꾸어 똑같은 방식으로 검사
            elif cliff[i][j] - cliff[i][j+1] == -1:
                if j+1 - slide < 0:
                    flag = False
                    break

                for k in range(0, slide):
                    if j - k < 0 or temp_runway[j-k]:
                        flag = False
                        break

                    if cliff[i][j] != cliff[i][j-k]:
                        flag = False
                        break
                    else:
                        temp_runway[j-k] = True

        # 모든 조건을 통과해서 활주로 건설이 가능하다면 cnt 1증가
        if flag:
            cnt += 1

    # 세로 방향 탐색, 똑같은 방식
    for j in range(N):
        flag = True
        temp_runway = [False] * N

        for i in range(N-1):
            if abs(cliff[i][j] - cliff[i+1][j]) >= 2:
                flag = False
                break
            
            if cliff[i][j] - cliff[i+1][j] == 1:
                if i + slide >= N:
                    flag = False
                    break

                for k in range(1, slide+1):
                    if i + k >= N or temp_runway[i+k]:
                        flag = False
                        break

                    if cliff[i+1][j] != cliff[i+k][j]:
                        flag = False
                        break
                    else:
                        temp_runway[i+k] = True

            elif cliff[i][j] - cliff[i+1][j] == -1:
                if i+1 - slide < 0:
                    flag = False
                    break

                for k in range(0, slide):
                    if i - k < 0 or temp_runway[i-k]:
                        flag = False
                        break

                    if cliff[i][j] != cliff[i-k][j]:
                        flag = False
                        break
                    else:
                        temp_runway[i-k] = True

        if flag:
            cnt += 1

    print(f'#{testcase} {cnt}')