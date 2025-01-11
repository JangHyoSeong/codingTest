T = int(input())
arr = [int(input()) for _ in range(T)]

for n in arr:
    result = [0] * 5

    result[0] += n // 60
    n %= 60

    if n <= 35:
        if n % 10 > 5:
            result[1] += n // 10 + 1
            result[4] += 10 - n % 10
        
        else:
            result[1] += n // 10
            result[3] += n % 10

    else:
        result[0] += 1

        if n%10 >= 5:
            result[2] += 6 - (n//10 + 1)
            result[4] += 10 - n%10

        else:
            result[2] += 6 - n//10
            result[3] += n%10

    print(*result)