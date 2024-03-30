from itertools import combinations

# 입력 받음
N = int(input())
intensity = [list(map(int, input().split())) for _ in range(N)]

# 원소의 길이가 N/2인 모든 조합을 생성
# 이렇게 하면 일의 조합을 생성할 수 있음
comb = list(combinations(range(0, N), N//2))

# 아침, 점심 업무강도 차이의 최소값을 정의 (임의의 큰 값)
min_gap = 21e8

# 주어진 조합의 길이를 출력
# 그냥 combinations 객체면 길이를 구할 수 없어서 앞에서 리스트로 바꾸어줌
# 만약 업무가 4개라면 (0, 1), (2, 3) 이런 식의 쌍으로 나와야함
# 이 때 comb를 출력해보면 다음과 같음
# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# 따라서 comb의 인덱스의 절반을 기준으로 대칭한다면 아침 점심 쌍으로 나눌 수 있음
comb_len = len(comb)

for i in range(comb_len // 2):
    # 현재 조합에서 사용할 업무 강도 합계
    sum_1 = 0
    sum_2 = 0

    # 현재 조합의 길이만큼 2중 순회
    for j in range(N//2):
        for k in range(N//2):
            # 업무 강도를 더해줌
            sum_1 += intensity[comb[i][j]][comb[i][k]]
            sum_2 += intensity[comb[comb_len-1-i][j]][comb[comb_len-1-i][k]]
    
    # 현재의 차이가 최소값보다 작다면 갱신
    temp_gap = abs(sum_2 - sum_1)
    if min_gap > temp_gap:
        min_gap = temp_gap

print(min_gap)