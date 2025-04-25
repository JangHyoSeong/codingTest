T = int(input())
numbers = [int(input()) for _ in range(T)]

matchsticks = {
    2: '1',
    3: '7',
    4: '4',
    5: '2',
    6: '0',
    7: '8'
}

N = max(numbers)

min_dp = [''] * (N + 1)
min_dp[2] = '1'
min_dp[3] = '7'
min_dp[4] = '4'
min_dp[5] = '2'
min_dp[6] = '6'
min_dp[7] = '8'

for i in range(8, N + 1):
    min_num = None
    for k in matchsticks:
        prev = min_dp[i - k]
        if prev == '':
            continue

        candidate = matchsticks[k] + prev
        candidate = ''.join(sorted(candidate))
        if candidate[0] == '0':
            for j in range(1, len(candidate)):
                if candidate[j] != '0':
                    candidate = candidate[j] + candidate[:j] + candidate[j+1:]
                    break
        
        if min_num is None or int(candidate) < int(min_num):
            min_num = candidate
    min_dp[i] = min_num

for number in numbers:
    min_val = min_dp[number]

    if number % 2 == 0:
        max_val = '1' * (number//2)
    else:
        max_val = '7' + '1' * ((number - 3) // 2)
    
    print(min_val, max_val)