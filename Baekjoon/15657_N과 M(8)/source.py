N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 숫자를 오름차순으로 정렬
numbers.sort()

# 숫자를 담을 리스트
result = []

def select(idx, M):

    # 마지막 숫자까지 모두 골랐다면 출력후 종료
    if idx == M:
        print(' '.join(map(str, result)))
        return
    
    # numbers를 순회하면서
    for i in range(N):
        
        # idx가 0이 아닐 때 (리스트에 값이 있다면)
        if idx > 0:
            # 리스트의 마지막 값보다 크거나 같은 수만 연산
            if result[idx-1] <= numbers[i]:

                # 값을 삽입하고
                result.append(numbers[i])

                # 다음 인덱스로 이동
                select(idx+1, M)

                # 연산이 끝났다면 pop
                result.pop()
        
        # idx가 0이라면 (리스트에 아무런 값이 없다면)
        else:
            # 일단 현재 숫자를 삽입, 연산, pop
            result.append(numbers[i])
            select(idx+1, M)
            result.pop()

select(0, M)