N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1일차 부터 시작하기에 인덱스를 맞추기 위해 (N+1)개로 설정
income = [0] * (N+1)

# 일을 순회하면서
for i in range(N):
    
    # 만약 이번 일을 했을 때 인덱스를 벗어나지 않는다면
    if i + arr[i][0] <= N:

        # 일이 끝난 날을 기준으로, 일을 했을 때와 일을 하지 않았을 때를 비교해서 더 큰값을 할당
        income[i + arr[i][0]] = max(income[i + arr[i][0]], income[i] + arr[i][1])

    # 기존의 값을 계속해서 누적시켜줌
    income[i+1] = max(income[i+1], income[i])

print(income[-1])