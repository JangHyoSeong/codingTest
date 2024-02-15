w, h = map(int, input().split())
start_x, start_y = map(int, input().split())

moving = int(input())
moving1 = moving

if moving <= w - start_x:
    
    now_x = start_x + moving
else:
    moving -= w - start_x
    how_many = moving // w
    moving_left = moving % w

    if how_many % 2:
        now_x = moving_left
    else:
        now_x = w - moving_left


if moving1 <= h - start_y:
    
    now_y = start_y + moving1

else:
    moving1 -= h - start_y
    how_many = moving1 // h
    up_left = moving1 % h

    if how_many % 2:
        now_y = up_left
    else:
        now_y = h - up_left
print(now_x, now_y)