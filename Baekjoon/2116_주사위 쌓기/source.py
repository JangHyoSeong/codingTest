'''
pair
0, 5
1, 3
2, 4
'''

num = int(input())
dices = [list(map(int, input().split())) for _ in range(num)]

top = dices[0].index(min(dices))

for dice in dices:
    pass