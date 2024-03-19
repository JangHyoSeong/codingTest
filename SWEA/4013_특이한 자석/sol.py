import sys
from collections import deque
sys.stdin = open('input.txt')

def checkRotate(target_magnet, dir):
    # 현재 자석의 회전을 수행하고, 양 옆의 자석이 회전 가능한지 판별하는 함수
    # 회전 가능하다면 재귀적으로 호출함

    # 현재 자석을 방문했으니 True로 바꿈
    flag[target_magnet] = True

    # 2~3번 자석까지 확인하기 위해서 <3으로 범위를 둠
    if target_magnet < 3:
        # 맞닿은 부분이 서로 다른 숫자이고, 방문한적 없다면 그 자석을 방문
        if magnet[target_magnet][2] != magnet[target_magnet+1][6] and not flag[target_magnet+1]:
            checkRotate(target_magnet + 1, -1 * dir)
    
    # 0~1번 자석까지 확인하기 위해서 >0으로 범위를 둠
    if target_magnet > 0:
        # 맞닿은 부분이 서로 다른 숫자이고, 방문한적 없다면 그 자석을 방문
        if magnet[target_magnet][6] != magnet[target_magnet-1][2] and not flag[target_magnet-1]:
            checkRotate(target_magnet - 1, -1 * dir)

    # 회전 수행
    rotate(magnet[target_magnet], dir)


def rotate(target_magnet, dir):
    # 방향에 따라서 회전을 수행
    if dir == 1:
        target_magnet.appendleft(target_magnet.pop())
    else:
        target_magnet.append(target_magnet.popleft())
        


T = int(input())

for testcase in range(1, T+1):
    K = int(input())
    magnet = [deque(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(K)]

    score = 0

    for i in range(K):
        # 인덱스를 편하게 확인하기 위해서 자석에 -1을 해줌
        target_magnet, dir = rotation[i][0] - 1, rotation[i][1]
        
        # 어느 자석을 돌렸는지 확인하는 flag
        flag = [False] * 4
        
        # 자석 돌리기 시작
        checkRotate(target_magnet, dir)

    # 점수 계산
    for i in range(4):
        if magnet[i][0] == 1:
            score += magnet[i][0] * 2**i

    print(f'#{testcase} {score}')