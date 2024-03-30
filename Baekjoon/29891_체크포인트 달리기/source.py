N, K = map(int, input().split())

# 양수와 음수를 각각 담음
checkpoints_plus = []
checkpoints_minus = []

# 숫자를 입력받으면서 양수면 양수 리스트, 음수면 음수 리스트에 삽입
for i in range(N):
    temp_num = int(input())
    if temp_num > 0:
        checkpoints_plus.append(temp_num)
    else:
        checkpoints_minus.append(temp_num)

# 이동 거리
move_range = 0

# 각 리스트를 정렬함 (절대값으로 큰 수가 앞에 가게)
checkpoints_minus.sort()
checkpoints_plus.sort(reverse=True)

# 각 리스트의 길이를 변수에 저장
minus_len = len(checkpoints_minus)
plus_len = N - minus_len

# 가장 멀리있는 체크포인트에 방문하고, K개 만큼 인덱스를 증가
idx = 0
while idx < minus_len:
    move_range += abs(checkpoints_minus[idx])
    idx += K

# 양수도 동일한 연산 진행  
idx = 0
while idx < plus_len:
    move_range += checkpoints_plus[idx]
    idx += K

# 왕복이므로 * 2
print(move_range * 2)