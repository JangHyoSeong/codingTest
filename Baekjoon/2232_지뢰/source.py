N = int(input())

mine = [0]

# 지뢰를 입력받고 맨 앞, 맨 뒤에 더미 추가
for i in range(N):
    mine.append(int(input()))

mine.append(0)

# 현재 지뢰값이 앞의 지뢰보다 크거나 같고,
# 뒤의 지뢰보다 크거나 같으면 터트려야 할 지뢰
# 이를 통해 모든 지뢰를 터트릴 수 있음
for i in range(1, N+1):
    if mine[i] >= mine[i-1] and mine[i] >= mine[i+1]:
        print(i)