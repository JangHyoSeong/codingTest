N, M = map(int, input().split())

arr_A = [list(map(int, input())) for _ in range(N)]
arr_B = [list(map(int, input())) for _ in range(N)]


count = 0

# 문제 조건상 항상 9개를 뒤집어야함. 
# 따라서 범위를 벗어나지 않기 위해 마지막 2칸은 순회하지 않음
for i in range(N-2):
    for j in range(M-2):
        # 두 행렬중 다른 곳을 발견하면
        if arr_A[i][j] != arr_B[i][j]:
            # 뒤집는 횟수 추가
            count += 1
            # 현재 칸을 왼쪽 위로 두고, 9칸을 뒤집음
            for k in range(3):
                for l in range(3):
                    arr_A[i+k][j+l] = (arr_A[i+k][j+l] + 1) % 2
                    
# 한 번 순회하면서, 뒤집지 못한 칸이 있다면 뒤집어서 만들 수 없음
# 만들지 못하는 경우라면 flag = False, -1출력
flag = True
for i in range(N):
    for j in range(M):
        if arr_A[i][j] != arr_B[i][j]:
            flag = False
        
        if not flag:
            break
    if not flag:
        break
    
if flag:
    print(count)
else:
    print(-1)
    
'''
같은 곳을 두 번 뒤집는다면 결국 처음 상태로 돌아오기 때문에 그럴 필요가 없음  
따라서 주어진 행렬을 한 번만 순회하면서 숫자가 다른 부분이 나온다면 바로 뒤집음  
'''