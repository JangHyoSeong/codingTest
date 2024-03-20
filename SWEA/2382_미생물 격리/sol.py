import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M, K = map(int, input().split())
    bacteria = [list(map(int, input().split())) for _ in range(K)]

    for time in range(M):
        # 박테리아가 어느 위치에 존재하는지 담는 딕셔너리
        position = {}

        # 박테리아를 순회하면서
        for i in range(len(bacteria)):

            # 개수가 0인 박테리아는 죽은 박테리아 -> 작업을 수행하지 않음
            if bacteria[i][2] == 0:
                continue

            # 이동
            if bacteria[i][3] == 1:bacteria[i][0] -= 1
            elif bacteria[i][3] == 2:bacteria[i][0] += 1
            elif bacteria[i][3] == 3:bacteria[i][1] -= 1
            elif bacteria[i][3] == 4:bacteria[i][1] += 1
            

            # 이동 방향 바꾸기 및 미생물 감소
            if bacteria[i][0] == 0 or bacteria[i][0] == N-1:
                bacteria[i][2] //= 2
                if bacteria[i][3] == 1:bacteria[i][3] = 2
                else:bacteria[i][3] = 1

            if bacteria[i][1] == 0 or bacteria[i][1] == N-1:
                bacteria[i][2] //= 2
                if bacteria[i][3] == 3 :bacteria[i][3] = 4
                else:bacteria[i][3] = 3

            # 박테리아가 반으로 줄었을때, 0이 된다면 위치를 초기화
            if bacteria[i][2] == 0:
                bacteria[i] = [-1, -1, 0, 0]

            # 현재 박테리아의 위치를 key로 하고, value로 박테리아의 인덱스, 크기를 넣음
            if position.get((bacteria[i][0], bacteria[i][1])) is None:
                position[(bacteria[i][0], bacteria[i][1])] = [(i, bacteria[i][2])]
            else:
                position[(bacteria[i][0], bacteria[i][1])].append((i, bacteria[i][2]))

        
        # 박테리아가 존재하는 위치 딕셔너리를 순회
        for bacteria_position in position:
            # 하나의 위치에 두개 이상 박테리아가 있다면
            if len(position[bacteria_position]) > 1:

                # 현재 위치에서 크기가 가장 큰 박테리아의 크기, 인덱스를 저장
                max_bacteria, max_idx = 0, 0
                # 현재 위치의 총 박테리아 개수를 저장
                total_bacteria = 0

                # 현재 위치의 박테리아를 순회함
                for temp_bacteria in position[bacteria_position]:
                    # 총 개수 더하기
                    total_bacteria += temp_bacteria[1]

                    # 가장 크기가 큰 박테리아 찾기
                    if temp_bacteria[1] > max_bacteria:
                        max_bacteria = temp_bacteria[1]
                        max_idx = temp_bacteria[0]

                # 다시 현재위치의 박테리아를 순회하면서
                for temp_bacteria in position[bacteria_position]:

                    # 가장 큰 박테리아가 아니면 없앰(초기화)
                    if temp_bacteria[0] != max_idx:
                        bacteria[temp_bacteria[0]]= [-1, -1, 0, 0]
                    # 가장 큰 박테리아라면 개수를 모두 더한 값으로 바꿔줌
                    else:
                        bacteria[max_idx][2] = total_bacteria

    # 작업이 끝난 후 박테리아의 총 개수를 출력
    result = 0
    for i in range(K):
        result += bacteria[i][2]

    print(f'#{testcase} {result}')