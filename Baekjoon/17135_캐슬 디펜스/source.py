from itertools import combinations
import copy

def attack(archers, board, D):
    n, m = len(board), len(board[0])
    attacked = set()

    for archer in archers:
        targets = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    distance = abs(n - i) + abs(archer - j)
                    if distance <= D:
                        targets.append((distance, j, i))
        
        if targets:
            targets.sort()
            attacked.add((targets[0][2], targets[0][1]))

    return attacked

def move_enemies(board):
    n, m = len(board), len(board[0])
    new_board = [[0]*m for _ in range(n)]
    
    for i in range(n-1):
        new_board[i+1] = board[i]
    
    return new_board

def simulate(archers, original_board, D):
    board = copy.deepcopy(original_board)
    total_attacked = 0

    while any(1 in row for row in board):
        attacked = attack(archers, board, D)
        total_attacked += len(attacked)
        
        for i, j in attacked:
            board[i][j] = 0

        board = move_enemies(board)

    return total_attacked

def main():
    n, m, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    max_kills = 0
    for archers in combinations(range(m), 3):
        kills = simulate(archers, board, D)
        max_kills = max(max_kills, kills)

    print(max_kills)

if __name__ == "__main__":
    main()
