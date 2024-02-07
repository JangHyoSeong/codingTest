T = int(input())

for testcase in range(T):
    N = int(input())

    result = [1, 2, 4]
    for i in range(3, N):
        temp = result[i-1] + result[i-2] + result[i-3]
        result.append(temp)

    print(result[N-1])