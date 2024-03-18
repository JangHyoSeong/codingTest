N = int(input())
numbers = list(map(int, input().split()))

# 현재 위치까지 증가하는 부분수열의 길이를 나타낼 리스트
arr = [1] * N

# i는 0에서 리스트의 끝까지 순회
for i in range(N):

    # j는 0에서 i까지 순회
    for j in range(0, i):

        # i번째 까지의 numbers를 모두 순회하면서, numbers[i]가 numbers[j]보다 크다면
        if numbers[i] > numbers[j]:
            #arr[i]를 갱신
            arr[i] = max(arr[j]+1, arr[i])

        '''
        기존에 구해놨던 최대 길이에서 현재 상태만큼 더하는 방식
        -> 다이나믹 프로그래밍
        '''        
print(max(arr))