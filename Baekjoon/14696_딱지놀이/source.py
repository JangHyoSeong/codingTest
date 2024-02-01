round = int(input())

for i in range(round):

    A_N, *A_card = list(map(int, input().split()))
    B_N, *B_card = list(map(int, input().split()))

    A_card_count = [0] * 4
    B_card_count = [0] * 4

    # card_count = [세모, 네모, 원, 별]

    for j in range(A_N):
        A_card_count[A_card[j]-1] += 1

    for j in range(B_N):
        B_card_count[B_card[j]-1] += 1

    for j in range(3, -1, -1):
        if A_card_count[j] > B_card_count[j]:
            print('A')
            break
        elif A_card_count[j] < B_card_count[j]:
            print('B')
            break
    else:
        print('D')

