def calculation(i, N, result, calc):
    # 재귀적으로 호출되며 연산을 진행할 함수
    # min값과 max값을 전역변수로 선언하여 사용
    global min_result
    global max_result

    # 얕은 복사를 피하기 위해 슬라이싱으로 복사
    new_calc = calc[:]

    # 모든 연산자를 할당했다면
    if i == N:
        # 최대, 최소값이 갱신가능하다면 갱신
        if max_result < result:
            max_result = result
        if min_result > result:
            min_result = result
    
    # 아직 모든 연산자를 할당하지 못했다면면
    else:
        # +, -, * 연산자를 사용할 수 있다면 (해당 인덱스가 0보다 크다면)
        # i+1 : 다음 인덱스로 이동
        # result (+, -, *) 현재 값에 각 연산 수행
        # 연산자 우선순위를 무시한다는 조건이 있어서 가능
        if new_calc[0] > 0:
            calculation(i+1, N, result+numbers[i], [new_calc[0]-1, new_calc[1], new_calc[2]])
        if new_calc[1] > 0:
            calculation(i+1, N, result-numbers[i], [new_calc[0], new_calc[1]-1, new_calc[2]])
        if new_calc[2] > 0:
            calculation(i+1, N, result*numbers[i], [new_calc[0], new_calc[1], new_calc[2]-1])


N = int(input())
numbers = list(map(int, input().split()))
calc = list(map(int, input().split()))

min_result = 10e10
max_result = -10e10

calculation(1, N, numbers[0], calc)

print(f'{min_result} {max_result}')