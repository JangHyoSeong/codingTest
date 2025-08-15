king_pos, stone_pos, N = input().split()
N = int(N)

directions = {
    "R":  (0, 1),
    "L":  (0, -1),
    "B":  (-1, 0),
    "T":  (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

def pos_to_coord(pos):
    col = ord(pos[0]) - ord('A')  # 0~7
    row = int(pos[1]) - 1         # 0~7
    return (row, col)

def coord_to_pos(coord):
    row, col = coord
    return chr(col + ord('A')) + str(row + 1)

king = pos_to_coord(king_pos)
stone = pos_to_coord(stone_pos)

for _ in range(N):
    move = input().strip()
    dr, dc = directions[move]

    new_king = (king[0] + dr, king[1] + dc)

    if not (0 <= new_king[0] < 8 and 0 <= new_king[1] < 8):
        continue

    if new_king == stone:
        new_stone = (stone[0] + dr, stone[1] + dc)
        if not (0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8):
            continue
        stone = new_stone

    king = new_king

print(coord_to_pos(king))
print(coord_to_pos(stone))