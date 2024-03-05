import sys
from collections import deque
sys.stdin = open('input.txt')


def countHouse(x, y, length, N):
    # 범위 내의 집의 개수를 세는 함수
    count = 0
    length -= 1

    # 2 * length 범위 만큼의 사각형이 조사 범위
    for i in range(x - length, x + length + 1):
        for j in range(y - length, y + length + 1):

            # 다이아몬드 크기 내부라면
            if abs(x - i) + abs(y - j) <= length:
                # 또한 인덱스를 벗어나지 않고, 그 곳이 집이라면 카운트증가
                if 0<= i < N and 0 <= j < N and arr[i][j]:
                    count += 1
    
    return count


T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0

    # 배열을 모두 조사하면서
    for i in range(N):
        for j in range(N):
            # 범위를 1부터 N+1까지 모두 계산함 
            for k in range(1, N+2):
                # 비용
                cost = k*k + (k-1)*(k-1)
                # 범위 내 집의 개수
                count = countHouse(i, j, k, N)
                # 손해가 아니고, max_count보다 크다면 갱신
                if cost <= count * M and max_count < count:
                    max_count = count

    print(f'#{testcase} {max_count}')
                    