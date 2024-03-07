from math import sqrt, ceil

def solution(r1, r2):
    answer = 0

    # 한 사분면에 대해서 탐색
    # 모든 사분면에 대해서 점의 개수는 같기 때문
    for i in range(1, r2+1):

        # i를 x좌표라 했을 때, 큰 원안에 포함되는 가장 큰 y좌표
        big = int(sqrt(r2**2 - i**2))

        

        '''
        int가 아니라 ceil(올림)을 쓴 이유
        sqrt의 경우 sqrt(5^2 - 4^2)같은 상황에서
        정확히 3이 나오지 않고, 2.99999와 같이 나올 수 있다
        3이 정확히 나왔다면 올려도 3이고, 2.999인 경우 올림하면 3이 나오니
        원하는 값을 얻을 수 있다.
        '''
        # 제곱근 안에 음수가 들어가는 것을 방지
        # 작은 원 안에 포함되는 가장 큰 y좌표
        if i < r1:
            small = ceil(sqrt(r1**2 - i**2))
        
        # i가 r1보다 큰 경우 -> x축 혹은 y축에 있을 때
        else:
            small = 0

        answer += big - small + 1
    
    return answer * 4