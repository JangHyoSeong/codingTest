for testcase in range(3):
    N = int(input())
    coins = [list(map(int, input().split())) for _ in range(N)]  # 동전 정보 입력 받기

    # 총 동전 금액을 계산
    coins_sum = 0
    for coin in coins:
        coins_sum += coin[0] * coin[1]
    
    # 총 금액이 홀수면 두 사람에게 똑같이 나눌 수 없으므로 0을 출력
    if coins_sum % 2 == 1:
        print(0)
        continue
    
    # 목표 금액은 전체 금액의 절반
    target_coin = coins_sum // 2
    
    # DP 배열 선언 (0 ~ target_coin까지)
    dp = [False] * (target_coin + 1)
    dp[0] = True  # 0원을 만드는 것은 항상 가능

    # 각 동전 종류별로 처리 (Bounded Knapsack)
    for V, C in coins:
        total_use = min(C, target_coin // V)
        current_amount = 1
        while total_use > 0:
            used_coins = min(current_amount, total_use)
            total_use -= used_coins
            for idx in range(target_coin, V * used_coins - 1, -1):
                if dp[idx - V * used_coins]:
                    dp[idx] = True
            current_amount *= 2
    
    # 목표 금액(target_coin)을 만들 수 있으면 1, 없으면 0 출력
    if dp[target_coin]:
        print(1)
    else:
        print(0)
