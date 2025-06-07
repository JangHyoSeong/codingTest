N = int(input())

moves = []
def hanoi(n, start, end, temp):
    if n == 1:
        moves.append((start, end))
        return
    
    hanoi(n-1, start, temp, end)
    moves.append((start, end))
    hanoi(n-1, temp, end, start)

hanoi(N, 1, 3, 2)
print(len(moves))
for move in moves:
    print(" ".join(map(str, move)))