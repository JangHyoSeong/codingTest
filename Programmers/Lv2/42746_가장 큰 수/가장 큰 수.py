def solution(numbers):
    answer = ''
    N = len(numbers)
    numbers = list(map(str, numbers))
    new_numbers = []

    for i in range(N):
        new_numbers.append([i, numbers[i]*4])
    
    new_numbers.sort(key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer += numbers[new_numbers[i][0]]


    if answer[0] == '0':
        answer = '0'

    return answer