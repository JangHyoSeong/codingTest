N, C, W = map(int, input().split())
trees = [int(input()) for _ in range(N)]

max_money = 0

for target_length in range(1, max(trees) + 1):
    total_money = 0

    for tree in trees:
        if tree < target_length:
            continue

        num_pieces = tree // target_length
        cuts = num_pieces - 1 if tree % target_length == 0 else num_pieces

        money = (num_pieces * target_length * W) - (cuts * C)

        if money > 0:
            total_money += money
    
    max_money = max(max_money, total_money)
print(max_money)