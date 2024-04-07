from itertools import combinations

# 입력 받음
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 좌표를 튜플의 형태로 리스트에 저장해둠
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 모든 치킨집 중 M개로 치킨집을 구성하는 조합을 생성
comb_chicken = list(combinations(chicken, M))

# 치킨거리의 최소값이 될 변수
min_chicken_range = 21e8

# M개의 치킨집을 고른 조합을 case로 두고 순회
for case in comb_chicken:
    # 이 경우에서의 치킨 거리
    temp_chicken_range = 0

    # 모든 집마다 가장 가까운 치킨거리를 구할 것
    for one_house in house:
        # 현재 집의 좌표
        h_x, h_y = one_house
        
        # 현재 집의 최소 치킨거리를 저장할 변수
        one_range = 100

        # M개 고른 치킨집 중 모든 치킨집을 순회하며 최소값을 찾음
        for one_chicken in case:

            # 치킨집의 좌표
            c_x, c_y = one_chicken

            # 모든 치킨집의 거리를 구하고, 최소값과 비교하여 최소값을 찾음
            one_range = min(one_range, abs((h_x-c_x)) + abs((h_y - c_y)))
        
        # 한 집에서 최소 치킨거리를 총 마을의 최소치킨거리에 더해줌
        temp_chicken_range += one_range
        
        # 이미 최소값을 넘었다면 이 케이스는 더이상 수행하지 않고 넘어감
        if temp_chicken_range > min_chicken_range:
            break
    
    # 최소 치킨거리를 갱신시켜줌
    min_chicken_range = min(min_chicken_range, temp_chicken_range)

print(min_chicken_range)