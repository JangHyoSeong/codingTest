N, K = map(int, input().split())
kits = list(map(int, input().split()))

# 현재 순열에 포함 여부를 나타낼 리스트
used = [False] * N

# 조건을 만족하는 경우의 수를 구할 변수
count = 0

# 현재 만들어지고 있는 순열
routine = []

def workout(i, muscle):
    # count를 전역변수로 선언
    global count
    
    # 만약 순열에서 N개의 수를 모두 골랐다면
    if i == N:
        # 현재 근력을 계산
        muscle = muscle - K + routine[-1]
        # 500을 넘지 못한다면 그냥 종료
        if muscle < 500:
            return
        
        # 500 이상이라면 count증가후 종료
        count += 1
        return
    
    # 아직 N개의 수를 모두 고르기 전이라면
    # N번 반복하면서, 아직 사용되지 않은 모든 숫자의 경우의수를 계산
    for j in range(N):
        # 아직 순열에 사용되지 않았다면
        if not used[j]:
            # 사용 처리
            used[j] = True
            # 순열에 숫자 삽입
            routine.append(kits[j])
            # 새로운 근력 계산
            new_muscle = muscle-K+routine[i]
            # 이번 숫자로 인해 500을 넘지 못한다면 리턴
            if new_muscle < 500:
                # 백트래킹. 원래대로 값을 돌려줌
                used[j] = False
                routine.pop()
                continue
            
            # 500을 넘었다면 다음 숫자를 고르러 진행
            workout(i+1, new_muscle)
            # 백트래킹. 원래대로 돌려줌
            used[j] = False
            routine.pop()
    
workout(0, 500)
print(count)