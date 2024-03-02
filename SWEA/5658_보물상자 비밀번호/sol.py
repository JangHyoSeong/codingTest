import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, K = map(int, input().split())
    password = list(input())


    repeat = N//4
    value = set()

    for i in range(repeat):
        for j in range(0, N, repeat):
            substr = "".join(password[j : j + repeat])
            value.add(substr)
        password.append(password.pop(0))
    
    decimal_value = []
    for num in value:
        decimal_value.append(int(num, 16))

    decimal_value.sort(reverse=True)
    print(f'#{testcase} {decimal_value[K-1]}')