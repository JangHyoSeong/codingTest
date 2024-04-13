N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 사전순 출력을 위해 정렬
numbers.sort()

# 현재 수열에서 어떤 숫자를 사용하고 있는지 저장할 used 리스트
used = [False] * N

# 하나의 수열을 담을 result 리스트
result = []

def permutation(idx):
    # 순열을 만드는 재귀함수

    # M개의 숫자를 모두 골랐다면
    if idx == M:
        # 출력
        print(' '.join(map(str, result)))
        return
    
    # 숫자를 순회하면서
    for i in range(N):
        # 넣은 숫자가 아니라면
        if not used[i]:

            # 숫자를 넣었다고 표시한 뒤
            used[i] = True
            # result에 삽입
            result.append(numbers[i])

            # 재귀 호출
            permutation(idx+1)

            # 백트래킹
            used[i] = False
            
            # 사용한 숫자는 result에서 없애줌
            result.pop()

# 재귀함수는 스택의 형태로 실행되기에 사전순으로 출력이 됨
permutation(0)