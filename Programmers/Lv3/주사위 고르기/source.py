from itertools import combinations
from bisect import bisect_left

def get_possible_sums(dices):
    result = [0]
    for dice in dices:
        result = [r + d for r in result for d in dice]
    return result

def solution(dice):
    N = len(dice)
    max_win = -1
    
    best_choice = []
    for a_dice in combinations(range(N), N//2):
        b_dice = list(set(range(N)) - set(a_dice))
        
        a_dices = [dice[i] for i in a_dice]
        b_dices = [dice[i] for i in b_dice]
        
        a_sums = get_possible_sums(a_dices)
        b_sums = get_possible_sums(b_dices)
        
        b_sums.sort()
        
        win = 0
        for a in a_sums:
            win += bisect_left(b_sums, a)
        
        if win > max_win:
            max_win = win
            best_choice = sorted([i + 1 for i in a_dice])
        
    
    return best_choice