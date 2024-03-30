numbers = list(map(int, input()))

# 카운팅 정렬을 사용하기 위해 카운팅 배열 선언
counting_arr = [0] * 10

# 카운팅 배열 각 인덱스에 그 숫자가 몇개인지 더해줌
for i in range(len(numbers)):
    counting_arr[numbers[i]] += 1

# 새롭게 정렬할 숫자 리스트
new_num = []

# 30의 배수이려면 무조건 1의 자리는 0이어야 한다
# 따라서 숫자 중에 0이 없었다면 만들수 없음
if counting_arr[0] == 0:
    print(-1)
    
# 숫자 중에 0이 있었다면
else:
    # 가장 큰 수부터 새로운 배열에 삽입 -> 내림차순 정렬
    for i in range(9, -1, -1):
        new_num += [i] * counting_arr[i]
    
    # 3의 배수 판별법 : 각 자릿수에 숫자를 모두 더해서 3의 배수이면 그 숫자도 3의 배수
    if sum(new_num) % 3 == 0:
        print("".join(map(str,new_num)))
    else:
        print(-1)