import sys

N = int(sys.stdin.readline().strip())
balls = sys.stdin.readline().strip()

def count_moves(target):
    left_cnt = 0
    for ball in balls:
        if ball == target:
            left_cnt += 1
        else:
            break

    right_cnt = 0
    for ball in reversed(balls):
        if ball == target:
            right_cnt += 1
        else:
            break

    total_cnt = balls.count(target)
    return min(total_cnt - left_cnt, total_cnt - right_cnt)

result = min(count_moves('R'), count_moves('B'))
print(result)