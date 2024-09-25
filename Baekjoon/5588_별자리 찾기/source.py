m = int(input())
constellation = [tuple(map(int, input().split())) for _ in range(m)]

n = int(input())
photo = [tuple(map(int, input().split())) for _ in range(n)]

base_x, base_y = constellation[0]
relative_constellation = [(x - base_x, y - base_y) for x, y in constellation]

for star_x, star_y in photo:
    dx = star_x - base_x
    dy = star_y - base_y

    matched = True
    for rx, ry in relative_constellation:
        if (star_x + rx, star_y + ry) not in photo:
            matched = False
            break

    if matched:
        print(dx, dy)
        break