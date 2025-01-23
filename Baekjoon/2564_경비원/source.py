W, H = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))

P = 2 * (W + H)

def convert_position(direction, distance):
    if direction == 1:
        return distance
    elif direction == 2:
        return W + H + (W - distance)
    elif direction == 3:
        return W + H + W + (H - distance)
    else:
        return W + distance
    
position = convert_position(start[0], start[1])
total_distance = 0
for direction, distance in stores:
    store_position = convert_position(direction, distance)
    total_distance += min(abs(position - store_position), P - abs(position - store_position))

print(total_distance)