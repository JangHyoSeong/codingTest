N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 입력받은 리스트를 위치 기준으로 오름차순 정렬
arr.sort(key=lambda x: x[0])

# 허용 가능한 최대의 거리를 저장할 변수
# 예를 들어 6위치가 감염, 10위치가 정상일 때, 감염 거리는 무조건 3이하여야 한다.
# 그런데 12위치가 감염, 14위치가 정상일 때, 감염 거리는 2 이하여야 하고, 이 값을 계속 순회하면서 갱신할 것이다
min_gap = 1000000
temp_gap = 0
# 0 부터 N-2까지 순회 (마지막 하나를 제외함)
# -> 방향으로 감염 거리의 최대를 찾는 코드
for i in range(N-1):

    # 현재 감염되지 않았다면
    if arr[i][1] == 0:

        # 다음 위치가 감염이라면
        if arr[i+1][1] == 1:
            # 현재 감염 거리를 구함
            temp_gap = arr[i+1][0] - arr[i][0]

            # 이 값을 최대 거리와 비교해서, 작은 값으로 갱신시켜줌
            min_gap = min(min_gap, temp_gap)

# <- 방향으로도 똑같이 수행
for i in range(N-1, 0, -1):
    if arr[i][1] == 0:
        if arr[i-1][1] == 1:
            temp_gap = arr[i][0] - arr[i-1][0]
            min_gap = min(min_gap, temp_gap)

# -1을 해주면 R이 나옴
min_gap -= 1

# 최소 시작 감염자 수를 구하기 위한 count
count = 0

# 마지막 값을 빼고 순회하면서
for i in range(N-1):

    # 현재 위치가 감염자라면 count 증가
    if arr[i][1] == 1:
        count += 1

        # 근데 다음 위치가 전염 가능한 위치라면 count 감소 -> 그대로
        if arr[i+1][1] == 1 and arr[i+1][0] - arr[i][0] <= min_gap:
            count -= 1

# 마지막 값은 순회하지 않았기에, 감염자라면 숫자 증가
if arr[N-1][1] == 1:count+=1

# 출력
print(count)